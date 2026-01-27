"""
LangGraph SQL Agent - Part 2: Node Implementations
===================================================
"""

from app.services.sql_agent import *

# ============================================================================
# NATURAL LANGUAGE ANSWER GENERATOR
# ============================================================================

def generate_natural_answer(user_question: str, query_result: str, sql_query: str) -> str:
    """Convert raw SQL results to natural language answer using LLM with STREAMING"""
    
    answer_prompt = f"""You are a helpful database assistant. Convert the query results into a natural language answer.

User Question: {user_question}

SQL Query: {sql_query}

Query Results: {query_result}

IMPORTANT FORMATTING RULES:
1. Start with a clear, direct answer to the user's question
2. If showing counts, format clearly: "**155,013 completed tasks** were found in January 2026"
3. If showing multiple tables, explain the breakdown: "Total of 188,038 tasks: 188,029 from checklist and 9 from delegation"
4. Add context about what the numbers mean
5. Use bullet points or markdown formatting for readability
6. Be conversational and helpful
7. Do NOT include raw SQL results like [(188029,)]
8. Do NOT say "undefined" or show technical errors

Generate a natural, human-readable answer:"""

    try:
        answer_llm = ChatOpenAI(model=settings.OPENAI_MODEL, temperature=0, streaming=True)
        
        # Stream the response
        full_answer = ""
        for chunk in answer_llm.stream(answer_prompt):
            full_answer += chunk.content
        
        return full_answer.strip()
    except Exception as e:
        print(f"[ERROR] Answer generation failed: {e}")
        # Fallback: at least parse the result somewhat
        try:
            # Try to extract numbers from result
            import re
            numbers = re.findall(r'\d+', str(query_result))
            if numbers:
                return f"Found {numbers[0]} results for your query."
            return f"Query executed successfully. Result: {query_result}"
        except:
            return f"Query executed successfully. Result: {query_result}"

# ============================================================================
# GRAPH NODES
# ============================================================================

def list_tables(state: EnhancedState):
    """Get available table names"""
    tables = list_tables_tool.invoke("")
    return {"messages": [AIMessage(content=f"Available tables: {tables}")]}

def call_get_schema(state: EnhancedState):
    """Fetch complete schema with samples"""
    tables = ", ".join(settings.ALLOWED_TABLES)
    schema = get_schema_tool.invoke({"table_names": tables})
    return {"messages": [AIMessage(content=schema)]}

def store_schema(state: EnhancedState):
    """Store schema in state for both LLMs"""
    last_msg = state["messages"][-1]
    schema_content = last_msg.content
    
    original_q = None
    for msg in state["messages"]:
        if isinstance(msg, HumanMessage):
            original_q = msg.content
            break
    
    return {
        "schema_info": schema_content,
        "original_question": original_q or "Unknown"
    }

def generate_query(state: EnhancedState):
    """LLM 1: Generate SQL query with 5-step analysis"""
    schema_info = state.get("schema_info", "Schema not yet loaded")
    
    feedback_section = ""
    if state.get("last_feedback"):
        feedback_section = f"""
⚠️ PREVIOUS ATTEMPT HAD ISSUES - PLEASE READ CAREFULLY:
{state['last_feedback']}

REGENERATE THE QUERY WITH THESE FIXES APPLIED.
"""
    
    system_message = SystemMessage(
        content=GENERATE_QUERY_SYSTEM_PROMPT.format(
            current_date=datetime.now().strftime("%Y-%m-%d"),
            schema_info=schema_info,
            feedback_section=feedback_section
        )
    )
    
    user_question = None
    for msg in reversed(state["messages"]):
        if isinstance(msg, HumanMessage):
            user_question = msg
            break
    
    messages_to_send = [system_message]
    if user_question:
        messages_to_send.append(user_question)
    
    llm_with_tools = model.bind_tools([run_query_tool], tool_choice="required")
    response = llm_with_tools.invoke(messages_to_send)
    
    new_attempts = state.get("validation_attempts", 0) + 1
    
    return {
        "messages": [response],
        "validation_attempts": new_attempts
    }

def validate_query(state: EnhancedState):
    """LLM 2: Validate generated query"""
    generated_query = None
    tool_call_id = None
    for msg in reversed(state["messages"]):
        if hasattr(msg, 'tool_calls') and msg.tool_calls:
            generated_query = msg.tool_calls[0]['args']['query']
            tool_call_id = msg.tool_calls[0]['id']
            break
    
    if not generated_query:
        return {
            "last_feedback": "ERROR: No query was generated. Please generate a valid SQL query.",
            "messages": []
        }
    
    schema_info = state.get('schema_info', 'Schema not available')
    
    validation_request = f"""
USER'S QUESTION:
{state.get('original_question', 'Unknown')}

DATABASE SCHEMA:
{schema_info}

GENERATED SQL QUERY:
```sql
{generated_query}
```

Validate this query using the 5-step mandatory framework. Provide JSON response only."""
    
    try:
        validator_llm = ChatOpenAI(
            model=settings.OPENAI_MODEL,
            temperature=0
        )
        
        response = validator_llm.invoke([
            SystemMessage(content=VALIDATOR_SYSTEM_PROMPT),
            HumanMessage(content=validation_request)
        ])
        
        # Extract JSON from response (handle cases where LLM adds explanation)
        content = response.content.strip()
        
        # Try to find JSON in the response
        if '{' in content:
            json_start = content.find('{')
            json_end = content.rfind('}') + 1
            json_str = content[json_start:json_end]
        else:
            json_str = content
        
        print(f"[DEBUG] Validator response: {json_str[:200]}...")
        validation_result = json.loads(json_str)
        
        if validation_result.get("status") == "APPROVED":
            print(f"[DEBUG] ✅ Query APPROVED")
            return {
                "last_feedback": "",
                "messages": []
            }
        else:
            issues = validation_result.get("issues", [])
            suggestions = validation_result.get("suggestions", [])
            
            feedback = "❌ VALIDATION FAILED:\n\n"
            feedback += "Issues:\n" + "\n".join(f"- {issue}" for issue in issues)
            feedback += "\n\nSuggestions:\n" + "\n".join(f"- {sug}" for sug in suggestions)
            
            print(f"[DEBUG] ❌ Query REJECTED: {feedback[:150]}...")
            
            return {
                "last_feedback": feedback,
                "messages": []
            }
    except json.JSONDecodeError as e:
        print(f"[ERROR] JSON parse error: {e}")
        print(f"[ERROR] Raw content: {response.content[:300]}")
        return {
            "last_feedback": f"Validator returned invalid JSON. Approving query to proceed.",
            "messages": []
        }
    except Exception as e:
        print(f"[ERROR] Validation error: {e}")
        return {
            "last_feedback": f"Validation error: {str(e)}. Approving query to proceed.",
            "messages": []
        }

def run_query_node(state: EnhancedState):
    """Execute query after validation with security checks"""
    query = None
    tool_call_id = None
    for msg in reversed(state["messages"]):
        if hasattr(msg, 'tool_calls') and msg.tool_calls:
            query = msg.tool_calls[0]['args']['query']
            tool_call_id = msg.tool_calls[0]['id']
            break
    
    if not query:
        return {"messages": [AIMessage(content="Error: No query found to execute")]}
    
    # 🔒 SECURITY VALIDATION
    is_valid, error_msg, sanitized_query = validate_sql_security(query)
    
    if not is_valid:
        error_response = f"""
🚨 SECURITY VALIDATION FAILED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❌ Query blocked by security validation:
   {error_msg}

This query does not meet security requirements for execution.

Allowed Query Types:
- SELECT statements only
- WITH ... SELECT (CTEs) only
- Maximum length: {settings.MAX_QUERY_LENGTH} characters
- No dangerous keywords or patterns allowed
- No multiple statements

Please try a different query.
"""
        tool_response = ToolMessage(
            content=error_response,
            tool_call_id=tool_call_id
        )
        return {"messages": [tool_response]}
    
    query = sanitized_query
    
    # Detect multi-table handling
    is_task_query = 'checklist' in query.lower() or 'delegation' in query.lower()
    has_both_tables = (
        'checklist_metrics' in query.lower() or 
        'delegation_metrics' in query.lower() or 
        'checklist_agg' in query.lower() or 
        'delegation_agg' in query.lower() or 
        'union' in query.lower() or
        'full outer join' in query.lower()
    )
    
    if is_task_query and 'checklist' in query.lower() and not has_both_tables:
        checklist_query = query
        delegation_query = query.replace('checklist', 'delegation').replace('CHECKLIST', 'DELEGATION')
        
        checklist_result = run_query_tool.invoke({"query": checklist_query})
        delegation_result = run_query_tool.invoke({"query": delegation_query})
        
        combined_result = f"""SEPARATE RESULTS:

📋 CHECKLIST TABLE:
{checklist_result}

📌 DELEGATION TABLE:
{delegation_result}

💡 Note: Results shown separately as requested."""
        
        # Store raw result for streaming answer generation
        tool_response = ToolMessage(
            content=combined_result,
            tool_call_id=tool_call_id
        )
    else:
        result = run_query_tool.invoke({"query": query})
        
        # Store raw result for streaming answer generation
        tool_response = ToolMessage(
            content=str(result),
            tool_call_id=tool_call_id
        )
    
    return {"messages": [tool_response]}

# ============================================================================
# CONDITIONAL EDGES
# ============================================================================

def should_validate_or_execute(state: EnhancedState) -> str:
    """Decide after query generation"""
    last_message = state["messages"][-1]
    
    if not hasattr(last_message, 'tool_calls') or not last_message.tool_calls:
        return END
    
    attempts = state.get("validation_attempts", 0)
    
    if attempts == 1 or (state.get("last_feedback") and attempts < settings.MAX_VALIDATION_ATTEMPTS):
        return "validate_query"
    else:
        return "run_query"

def should_regenerate_or_approve(state: EnhancedState) -> str:
    """Decide after validation"""
    if state.get("last_feedback"):
        return "generate_query"
    else:
        return "run_query"

# ============================================================================
# BUILD GRAPH
# ============================================================================

def build_agent():
    """Build the LangGraph agent"""
    builder = StateGraph(EnhancedState)
    
    # Add nodes
    builder.add_node("list_tables", list_tables)
    builder.add_node("call_get_schema", call_get_schema)
    builder.add_node("store_schema", store_schema)
    builder.add_node("generate_query", generate_query)
    builder.add_node("validate_query", validate_query)
    builder.add_node("run_query", run_query_node)
    
    # Add edges
    builder.add_edge(START, "list_tables")
    builder.add_edge("list_tables", "call_get_schema")
    builder.add_edge("call_get_schema", "store_schema")
    builder.add_edge("store_schema", "generate_query")
    
    # Conditional edges
    builder.add_conditional_edges(
        "generate_query",
        should_validate_or_execute,
        {
            "validate_query": "validate_query",
            "run_query": "run_query",
            END: END
        }
    )
    
    builder.add_conditional_edges(
        "validate_query",
        should_regenerate_or_approve,
        {
            "generate_query": "generate_query",
            "run_query": "run_query"
        }
    )
    
    builder.add_edge("run_query", END)
    
    # Compile with checkpointer
    checkpointer = MemorySaver()
    agent = builder.compile(checkpointer=checkpointer)
    
    return agent

# Create singleton agent instance
sql_agent = build_agent()
