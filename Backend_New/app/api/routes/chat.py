"""
Chat API Routes
===============
Streaming chat endpoint with LangGraph agent, cache, and context
"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import Optional, AsyncGenerator
import json
import uuid
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

from app.services.agent_nodes import sql_agent
from app.services.session_manager import session_manager
from app.services.cache_service import query_cache
from app.services.context_manager import context_manager
from app.core.config import settings

router = APIRouter()

class ChatRequest(BaseModel):
    question: str  # Frontend sends 'question' not 'message'
    session_id: Optional[str] = None

async def stream_natural_answer(question: str, raw_result: str, sql_query: str, is_sample: bool = False, total_count: int = 0) -> AsyncGenerator[str, None]:
    """Stream natural language answer generation word by word"""
    
    sample_note = ""
    if is_sample and total_count > 0:
        sample_note = f"\n\n⚠️ IMPORTANT: The results show a SAMPLE of 15 rows out of {total_count:,} total records. Mention this prominently in your answer."
    
    answer_prompt = f"""You are a Database Analyst. Your job is to fill out the Report Template below based on the query results.

Basic Information:
- User Question: "{question}"
- SQL Query: {sql_query}
- Results: {raw_result}{sample_note}

────────────────────────────────────────────────────────────
REQUIRED RESPONSE TEMPLATE (Fill this out):
────────────────────────────────────────────────────────────

### 1. 📊 Executive Summary
[Write a natural language summary of the answer here. Use bold numbers. Explain "Pending" (submission_date is NULL) vs "Completed".]

### 2. 📝 Technical Note
(Note: To derive this answer, I queried the `[insert table names]` table(s). I filtered `[insert column]` to match the date range, used `[insert column]` to determine status, and filtered `[insert column]` to match the user.)

────────────────────────────────────────────────────────────
RULES:
1. You MUST explicitly name the SQL columns used in the Technical Note.
2. Do NOT leave the Technical Note empty.
3. Do NOT output the identifiers "### 1." or "### 2." - just the content.
4. Put the Note in a new paragraph at the very end.

Generate the response now:"""

    try:
        from langchain_openai import ChatOpenAI
        answer_llm = ChatOpenAI(model=settings.LLM_MODEL, temperature=0, openai_api_key=settings.OPENAI_API_KEY, streaming=True)
        
        # Stream response word by word
        async for chunk in answer_llm.astream(answer_prompt):
            if chunk.content:
                yield chunk.content
    except Exception as e:
        print(f"[ERROR] Answer generation failed: {e}")
        # Fallback
        yield "Query executed successfully. "
        yield f"Result: {raw_result}"

async def stream_agent_response(question: str, session_id: str) -> AsyncGenerator[str, None]:
    """Stream agent responses with cache and context"""
    
    try:
        # Check cache first
        yield f"data: {json.dumps({'type': 'status', 'message': '🔍 Checking cache...'})}\n\n"
        
        cached = query_cache.find_similar_query(question)
        if cached:
            print(f"[CACHE HIT] Using cached SQL for '{question[:50]}...'")
            yield f"data: {json.dumps({'type': 'cache_hit', 'value': True})}\n\n"
            yield f"data: {json.dumps({'type': 'status', 'message': '⚡ Using cached query'})}\n\n"
            yield f"data: {json.dumps({'type': 'query', 'content': cached['sql']})}\n\n"
            
            # Execute cached query directly
            from app.services.db_service import execute_query
            try:
                result = execute_query(cached['sql'])
                
                # Handle row sampling for large results
                total_count = len(result) if result else 0
                is_sample = False
                display_result = result
                
                if total_count > 15:
                    display_result = result[:15]
                    is_sample = True
                    yield f"data: {json.dumps({'type': 'status', 'message': f'📊 Showing 15/{total_count:,} rows...'})}\n\n"
                
                # Generate answer with cached result
                yield f"data: {json.dumps({'type': 'status', 'message': '💬 Generating answer...'})}\n\n"
                async for word in stream_natural_answer(question, str(display_result), cached['sql'], is_sample, total_count):
                    yield f"data: {json.dumps({'type': 'chunk', 'content': word})}\n\n"
                
                # Store context
                context_manager.extract_and_store(session_id, question, cached['sql'])
                
                yield f"data: {json.dumps({'type': 'done'})}\n\n"
                return
            except Exception as e:
                print(f"[CACHE ERROR] Cached query failed: {e}")
                query_cache.invalidate(question)
                yield f"data: {json.dumps({'type': 'status', 'message': '🔄 Cache failed, generating new query...'})}\n\n"
        else:
            yield f"data: {json.dumps({'type': 'cache_hit', 'value': False})}\n\n"
        
        # Get context hints for follow-up queries
        context_hint = context_manager.build_context_hint(session_id, question)
        if context_hint:
            print(f"[CONTEXT] {context_hint[:100]}...")
        
        # Send initial status
        yield f"data: {json.dumps({'type': 'status', 'message': '🔄 Analyzing schema...'})}\n\n"
        
        print(f"[DEBUG] Starting agent for question: {question[:50]}...")
        print(f"[DEBUG] Session ID: {session_id}")
        
        config = {"configurable": {"thread_id": session_id}}
        
        # Track final result and generated SQL
        final_result = None
        generated_sql = None
        is_sample = False
        total_count = 0
        
        # Stream through the graph
        node_count = 0
        
        # Inject context into the conversation
        agent_input_message = question
        if context_hint:
             agent_input_message = f"{context_hint}\n\nUser Question: {question}"

        for event in sql_agent.stream(
            {"messages": [HumanMessage(content=agent_input_message)]},
            config,
            stream_mode="updates"
        ):
            node_count += 1
            print(f"[DEBUG] Event {node_count}: {list(event.keys())}")
            
            for node_name, node_state in event.items():
                print(f"[DEBUG] Node '{node_name}' state keys: {list(node_state.keys()) if isinstance(node_state, dict) else 'not a dict'}")
                
                # Send progress updates
                if node_name == "list_tables":
                    yield f"data: {json.dumps({'type': 'status', 'message': '📊 Loading tables...'})}\n\n"
                
                elif node_name == "call_get_schema":
                    yield f"data: {json.dumps({'type': 'status', 'message': '🔍 Fetching schema...'})}\n\n"
                
                elif node_name == "store_schema":
                    yield f"data: {json.dumps({'type': 'status', 'message': '💾 Storing schema context...'})}\n\n"
                
                elif node_name == "generate_query":
                    yield f"data: {json.dumps({'type': 'status', 'message': '🤖 LLM 1: Generating query...'})}\n\n"
                    
                    # Check if query was generated and capture it
                    if "messages" in node_state and node_state["messages"]:
                        last_msg = node_state["messages"][-1]
                        if hasattr(last_msg, 'tool_calls') and last_msg.tool_calls:
                            generated_sql = last_msg.tool_calls[0]['args']['query']
                            print(f"[DEBUG] Generated query: {generated_sql[:100]}...")
                            
                            # Show generated query
                            yield f"data: {json.dumps({'type': 'query', 'content': generated_sql})}\n\n"
                
                elif node_name == "validate_query":
                    yield f"data: {json.dumps({'type': 'status', 'message': '🔍 LLM 2: Validating query...'})}\n\n"
                    
                    # Check validation result
                    if "last_feedback" in node_state:
                        feedback = node_state.get("last_feedback", "")
                        if feedback:
                            print(f"[DEBUG] Validation feedback: {feedback[:100]}...")
                            yield f"data: {json.dumps({'type': 'status', 'message': '❌ Validation failed - regenerating...'})}\n\n"
                        else:
                            yield f"data: {json.dumps({'type': 'status', 'message': '✅ Query approved!'})}\n\n"
                
                elif node_name == "run_query":
                    yield f"data: {json.dumps({'type': 'status', 'message': '🔒 Security check...'})}\n\n"
                    yield f"data: {json.dumps({'type': 'status', 'message': '⚡ Executing query...'})}\n\n"
                    
                    # Capture raw result
                    print(f"[DEBUG] run_query node_state keys: {list(node_state.keys())}")
                    if "messages" in node_state and node_state["messages"]:
                        print(f"[DEBUG] Messages found: {len(node_state['messages'])} messages")
                        last_msg = node_state["messages"][-1]
                        final_result = last_msg.content
                        print(f"[DEBUG] Captured final result: {final_result[:200]}...")
                        
                        # Parse result to handle row sampling
                        try:
                            # Check if result contains row data (list of dicts)
                            if "SEPARATE RESULTS" in final_result:
                                # Multiple table results
                                pass  # Keep as is
                            elif isinstance(eval(final_result), list) and len(eval(final_result)) > 15:
                                result_list = eval(final_result)
                                total_count = len(result_list)
                                display_result = result_list[:15]
                                final_result = str(display_result)
                                is_sample = True
                                yield f"data: {json.dumps({'type': 'status', 'message': f'📊 Showing 15/{total_count:,} rows...'})}\n\n"
                        except:
                            pass  # Keep raw result if parsing fails
                    else:
                        print(f"[DEBUG] No messages in run_query state!")
        
        # Now stream the answer generation with typing effect
        if final_result:
            # Check if result is an error
            is_error = any([
                "Error:" in str(final_result),
                "psycopg2" in str(final_result),
                "operator does not exist" in str(final_result),
                "UndefinedFunction" in str(final_result),
                "syntax error" in str(final_result).lower()
            ])
            
            if is_error:
                print(f"[ERROR] Query execution failed: {final_result[:200]}...")
                yield f"data: {json.dumps({'type': 'error', 'message': 'Query execution failed. Please try rephrasing your question.'})}\n\n"
                # DON'T cache failed queries!
                return
            
            print(f"[DEBUG] Generating natural language answer with streaming...")
            yield f"data: {json.dumps({'type': 'status', 'message': '💬 Generating answer...'})}\n\n"
            
            # Stream answer generation with captured SQL
            async for word in stream_natural_answer(question, final_result, generated_sql or "", is_sample, total_count):
                yield f"data: {json.dumps({'type': 'chunk', 'content': word})}\n\n"
            
            # Cache ONLY successful queries
            if generated_sql:
                query_cache.cache_query(question, generated_sql)
            
            # Store context for follow-ups
            if generated_sql:
                context_manager.extract_and_store(session_id, question, generated_sql)
        else:
            print(f"[DEBUG] ERROR: No result captured!")
            yield f"data: {json.dumps({'type': 'error', 'message': 'No result returned'})}\n\n"
        
        # Send completion
        yield f"data: {json.dumps({'type': 'done'})}\n\n"
        
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        yield f"data: {json.dumps({'type': 'error', 'message': error_msg})}\n\n"

@router.post("/stream")
async def chat_stream(request: ChatRequest):
    """
    Stream chat responses with LangGraph agent
    
    Response format (SSE):
    - type: 'status' -> Progress updates
    - type: 'cache_hit' -> Cache hit/miss indicator
    - type: 'query' -> Generated SQL query
    - type: 'chunk' -> Answer content (word by word)
    - type: 'done' -> Completion signal
    - type: 'error' -> Error message
    """
    
    # Get or create session
    session_id = request.session_id or str(uuid.uuid4())
    
    # Check if session exists
    sessions = session_manager.get_sessions()
    session_exists = any(s["session_id"] == session_id for s in sessions)
    
    if not session_exists:
        # Auto-create session with first message as title
        title = request.question[:50] + "..." if len(request.question) > 50 else request.question
        session_manager.create_session(session_id, title)
    
    # Store user message
    session_manager.add_message(session_id, "user", request.question)
    
    # Stream response
    async def generate():
        full_response = []
        
        async for chunk in stream_agent_response(request.question, session_id):
            yield chunk
            
            # Collect full response for storage
            try:
                data = json.loads(chunk.split("data: ")[1])
                if data.get("type") == "chunk":
                    full_response.append(data["content"])
            except:
                pass
        
        # Store bot response
        if full_response:
            bot_message = "".join(full_response)
            session_manager.add_message(session_id, "assistant", bot_message)
    
    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Session-ID": session_id
        }
    )

@router.get("/cache/stats")
async def get_cache_stats():
    """Get cache statistics"""
    stats = query_cache.get_stats()
    return {
        "total_entries": stats.get("total_queries", 0),
        "cache_hits": stats.get("cache_hits", 0),
        "cache_misses": stats.get("cache_misses", 0),
        "hit_rate": stats.get("hit_rate", 0.0),
        "similarity_threshold": stats.get("threshold", 0.85),
        "enabled": stats.get("enabled", False)
    }

@router.post("/cache/clear")
async def clear_cache():
    """Clear cache"""
    success = query_cache.clear()
    return {
        "status": "success" if success else "failed",
        "message": "Cache cleared" if success else "Cache clear failed"
    }

@router.post("/cache/invalidate/{session_id}")
async def invalidate_session_cache(session_id: str):
    """Clear cache entries related to a session"""
    try:
        from app.services.session_manager import session_manager
        messages = session_manager.get_session_messages(session_id)
        invalidated = 0
        for msg in messages:
            if msg['role'] == 'user':
                if query_cache.invalidate(msg['content']):
                    invalidated += 1
        return {
            "status": "success",
            "invalidated_count": invalidated,
            "message": f"Invalidated {invalidated} cache entries"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
