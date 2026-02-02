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
from app.core.config import settings
from app.services.session_manager import session_manager
from app.services.cache_service import query_cache
from app.services.context_manager import context_manager

from app.core.router import determine_database, get_agent_for_database, get_answer_generator

router = APIRouter()

class ChatRequest(BaseModel):
    question: str
    session_id: Optional[str] = None

async def stream_agent_response(question: str, session_id: str) -> AsyncGenerator[str, None]:
    """Stream agent responses with cache and context"""

    # 0. Context Fusion (Handle Clarification Replies)
    try:
        messages = session_manager.get_session_messages(session_id)
        # Structure: [..., User_Org, Bot_Ask, User_Current (Added in Line 312)]
        if len(messages) >= 3:
            last_bot_msg = messages[-2]['content']
            original_user_msg = messages[-3]['content']
            
            # Heuristic: Did the bot ask a clarification question?
            if any(phrase in last_bot_msg.lower() for phrase in ["which database", "which list", "which specific", "clarify"]):
                print(f"[CONTEXT FUSION] Detected Clarification Reply!")
                print(f"[CONTEXT FUSION] Original: {original_user_msg}")
                print(f"[CONTEXT FUSION] Clarification: {question}")
                
                # Fuse the intent
                question = f"{original_user_msg} (Context: {question})"
                print(f"[CONTEXT FUSION] Fused Query: {question}")
                
                yield f"data: {json.dumps({'type': 'status', 'message': '🔗 Connecting context...'})}\n\n"
    except Exception as e:
        print(f"[CONTEXT FUSION ERROR] {e}")

    # 1. Determine Target Database (Router)
    db_name, reasoning, clarification_question = determine_database(question)
    
    # Show Router's Thinking
    yield f"data: {json.dumps({'type': 'status', 'message': f'🧠 Router Logic: {reasoning}'})}\n\n"
    
    # Handle Ambiguity / Unsure Router
    if db_name == "AMBIGUOUS":
        print(f"[ROUTER] Ambiguous query. Asking user for clarification.")
        yield f"data: {json.dumps({'type': 'status', 'message': '🤔 Query seems ambiguous...'})}\n\n"
        yield f"data: {json.dumps({'type': 'status', 'message': '❓ Asking for clarification...'})}\n\n"
        
        clarification_msg = clarification_question
        
        # Stream the clarification question
        for word in clarification_msg.split(" "):
            yield f"data: {json.dumps({'type': 'chunk', 'content': word + ' '})}\n\n"
            import asyncio
            await asyncio.sleep(0.01)
            
        yield f"data: {json.dumps({'type': 'done'})}\n\n"
        return

    print(f"[ROUTER] Question routed to: '{db_name}' ({reasoning})")
    
    yield f"data: {json.dumps({'type': 'status', 'message': f'🔀 Routing to {db_name} database...'})}\n\n"

    try:
        # Check cache first (scoped by DB)
        yield f"data: {json.dumps({'type': 'status', 'message': '🔍 Checking cache...'})}\n\n"
        
        cached = query_cache.find_similar_query(question, db_name=db_name)
        if cached:
            print(f"[CACHE HIT] Using cached SQL for '{question[:50]}...'")
            yield f"data: {json.dumps({'type': 'cache_hit', 'value': True})}\n\n"
            yield f"data: {json.dumps({'type': 'status', 'message': '⚡ Using cached query'})}\n\n"
            yield f"data: {json.dumps({'type': 'query', 'content': cached['sql']})}\n\n"
            
            # Execute cached query directly (Using specific DB logic implied by router, but simplified for now)
            # CAUTION: We need to execute against the specific DB here too.
            # Ideally the cache metadata stores connection string, but for now we trust the router.
            
            # TODO: Refactor execute_query to accept db_connection or use agent's tool
            # For immediate compatibility, we will allow the agent to re-validate if we can't easily execute directly
            # OR better: Use the generic execute_query which (currently) defaults to env vars.
            # To be 100% correct, we should use the same connection as the agent.
            
            # Temporary Fix: Use the agent's run_query node logic or global execute if env matches.
            # Since we only have checklist now (global env), execute_query works.
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
                
                # Generate answer with cached result using DB-specific generator
                yield f"data: {json.dumps({'type': 'status', 'message': '💬 Generating answer...'})}\n\n"
                
                # Dynamic Answer Streaming
                # For now using the logic from router helper (blocking), but to keep streaming we might inline specific logic
                # To keep it simple and safe for this port: we use the blocking call from router then yield chunks (simulated)
                answer_func = get_answer_generator(db_name)
                answer_gen = answer_func(question, str(display_result), cached['sql'])
                
                # Stream the result
                full_answer = ""
                async for chunk in answer_gen:
                    full_answer += chunk
                    yield f"data: {json.dumps({'type': 'chunk', 'content': chunk})}\n\n"
                
                # Store context
                context_manager.extract_and_store(session_id, question, cached['sql'])
                
                yield f"data: {json.dumps({'type': 'done'})}\n\n"
                return
            except Exception as e:
                print(f"[CACHE ERROR] Cached query failed: {e}")
                query_cache.invalidate(question, db_name=db_name)
                yield f"data: {json.dumps({'type': 'status', 'message': '🔄 Cache failed, generating new query...'})}\n\n"
        else:
            yield f"data: {json.dumps({'type': 'cache_hit', 'value': False})}\n\n"
        
        # Get context hints for follow-up queries
        context_hint = context_manager.build_context_hint(session_id, question)
        if context_hint:
            print(f"[CONTEXT] {context_hint[:100]}...")
        
        # Send initial status
        yield f"data: {json.dumps({'type': 'status', 'message': f'🔄 Analyzing {db_name} schema...'})}\n\n"
        
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

        # DYNAMIC AGENT RETRIEVAL
        target_agent = get_agent_for_database(db_name)

        for event in target_agent.stream(
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
                        
                        # Case A: Tool Call (Checklist Agent)
                        if hasattr(last_msg, 'tool_calls') and last_msg.tool_calls:
                            generated_sql = last_msg.tool_calls[0]['args']['query']
                        
                        # Case B: Content (Lead-To-Order Agent)
                        elif hasattr(last_msg, 'content') and "SELECT" in str(last_msg.content).upper():
                            generated_sql = last_msg.content.strip().replace("```sql", "").replace("```", "")
                            
                        if generated_sql:
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
            
            # Use Dynamic Answer Generator (Blocking for now, simulated streaming)
            # Use Dynamic Answer Generator (Real Streaming)
            answer_func = get_answer_generator(db_name)
            answer_gen = answer_func(question, final_result, generated_sql or "")

            # Stream answer generation with captured SQL
            full_answer = ""
            async for chunk in answer_gen:
                full_answer += chunk
                yield f"data: {json.dumps({'type': 'chunk', 'content': chunk})}\n\n"
            
            # Cache ONLY successful queries (Scoped)
            
            # Cache ONLY successful queries (Scoped)
            if generated_sql:
                query_cache.cache_query(question, generated_sql, db_name=db_name)
            
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
