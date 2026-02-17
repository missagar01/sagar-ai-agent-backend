"""
LangGraph SQL Agent - Part 2: Node Implementations
===================================================
"""

from app.services.sql_agent import *
from app.core.column_restrictions import get_columns_description
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import time

# ============================================================================
# NATURAL LANGUAGE ANSWER GENERATOR
# ============================================================================

def generate_natural_answer(user_question: str, query_result: str, sql_query: str) -> str:
    """Convert raw SQL results to natural language answer using LLM with STREAMING"""
    
    # Parse query result to check for source_table column (UNION ALL results)
    has_source_breakdown = False
    checklist_count = 0
    delegation_count = 0
    
    try:
        # Try to detect if result has source_table column (from UNION ALL queries)
        result_str = str(query_result)
        if "'checklist'" in result_str or "'delegation'" in result_str or "'source_table'" in result_str.lower():
            has_source_breakdown = True
            # Extract counts if visible
            import re
            # Look for patterns like ('checklist', 123) or {'source_table': 'checklist', 'count': 123}
            checklist_matches = re.findall(r"checklist.*?(\d+)", result_str, re.IGNORECASE)
            delegation_matches = re.findall(r"delegation.*?(\d+)", result_str, re.IGNORECASE)
            if checklist_matches:
                checklist_count = int(checklist_matches[0])
            if delegation_matches:
                delegation_count = int(delegation_matches[0])
    except Exception as e:
        print(f"[DEBUG] Result parsing for source breakdown: {e}")
    
    # Build enhanced prompt with source breakdown metrics (pure data only)
    breakdown_info = ""
    if has_source_breakdown and (checklist_count > 0 or delegation_count > 0):
        breakdown_info = f"""
[Source Breakdown Data]:
- Checklist: {checklist_count:,}
- Delegation: {delegation_count:,}
- Total: {checklist_count + delegation_count:,}
"""
    
    # STEP 1: Generate the Data Answer (The "What")
    answer_prompt = f"""You are a Database Analyst. Summarize the following query results for the user.

User Question: "{user_question}"
SQL Query: {sql_query}
Results: {query_result}{breakdown_info}

INSTRUCTIONS:
- Provide a clear, helpful summary of the numbers.
- Use emojis 📋, 📌, 📊.
- Explain "Pending" (submission_date is NULL) vs "Completed".
- Do NOT talk about the SQL logic here, just the data.

Generate the summary now:"""

    # STEP 2: Generate the Technical Note (The "How")
    note_prompt = f"""You are a SQL Expert. Explain the logic of the following SQL query in a single natural language note.

SQL Query: 
{sql_query}

INSTRUCTIONS:
- Output a single parenthetical note.
- Format: `(Note: ...)`
- Explain which tables were queried.
- **CRITICAL:** Explicitly name the columns used (e.g. `task_start_date`, `submission_date`).
- Example: "(Note: To find this, I queried the `checklist` table, filtered `task_start_date` for this month, and checks `submission_date` to determine status.)"

Generate ONLY the note:"""

    try:
        from langchain_openai import ChatOpenAI
        # Helper to run non-streaming call
        llm_direct = ChatOpenAI(model=settings.LLM_MODEL, temperature=0, openai_api_key=settings.OPENAI_API_KEY)
        
        # 1. Get Main Answer (Streaming if possible, but for simplicity here we do blocking or parallel)
        # We will keep streaming for the main answer validity feeling, but we need to append.
        
        # Parallel Execution for speed? sequential for now.
        full_answer_msg = llm_direct.invoke(answer_prompt)
        main_answer = full_answer_msg.content.strip()
        
        technical_note_msg = llm_direct.invoke(note_prompt)
        technical_note = technical_note_msg.content.strip()
        
        # Combine
        final_response = f"{main_answer}\n\n{technical_note}"
        
        return final_response
        
    except Exception as e:
        print(f"[ERROR] Answer generation failed: {e}")
        # Fallback
        return f"Query Results: {query_result}\n\n(Note: SQL Logic explanation failed to generate.)"


# ============================================================================
# GRAPH NODES
# ============================================================================

def list_tables(state: EnhancedState, db=None):
    """Get available table names. Accepts optional 'db' for multi-database support."""
    if db:
        # Use the specific DB instance if provided
        tables = ", ".join(db.get_usable_table_names())
    else:
        # Default fallback
        tables = list_tables_tool.invoke("")
        
    return {"messages": [AIMessage(content=f"Available tables: {tables}")]}

def call_get_schema(state: EnhancedState, db=None, allowed_tables=None):
    """Fetch complete schema with samples and add type warnings.
       Accepts 'db' and 'allowed_tables' for multi-db support.
    """
    if db and allowed_tables:
        # Custom DB Schema Retrieval
        schema = db.get_table_info(allowed_tables)
        tables_str = ", ".join(allowed_tables)
        restriction_note = f"🔒 RESTRICTED TO TABLES: {tables_str}"
        enhanced_schema = f"{restriction_note}\n\n{schema}"
        return {"messages": [AIMessage(content=enhanced_schema)]}

    # Default / Legacy Logic (Checklist)
    tables = ", ".join(settings.ALLOWED_TABLES)
    schema = get_schema_tool.invoke({"table_names": tables})
    
    # Add column restrictions notice (All Checklist DB Tables)
    column_restrictions = f"""
🔒 COLUMN RESTRICTIONS (Client Requirement):
═══════════════════════════════════════════════════════════════════════════════
ONLY use these columns in your queries:

📋 CHECKLIST table: {get_columns_description('checklist')}
📌 DELEGATION table: {get_columns_description('delegation')}
👤 USERS table: {get_columns_description('users')}
🎫 TICKET_BOOK table: {get_columns_description('ticket_book')}
🏖️ LEAVE_REQUEST table: {get_columns_description('leave_request')}
🏭 PLANT_VISITOR table: {get_columns_description('plant_visitor')}
✈️ REQUEST table: {get_columns_description('request')}
📄 RESUME_REQUEST table: {get_columns_description('resume_request')}

❌ DO NOT query or SELECT any other columns from these tables.
═══════════════════════════════════════════════════════════════════════════════
"""
    
    # Add critical type casting warnings
    enhanced_schema = f"""{column_restrictions}

{schema}

⚠️ CRITICAL DATA TYPE WARNINGS (Checklist System):
...
"""
    
    return {"messages": [AIMessage(content=enhanced_schema)]}


def store_schema(state: EnhancedState):
    """Store schema in state for both LLMs and reset validation counter"""
    last_msg = state["messages"][-1]
    schema_content = last_msg.content
    
    original_q = None
    original_q = None
    for msg in reversed(state["messages"]):
        if isinstance(msg, HumanMessage):
            original_q = msg.content
            break
    
    return {
        "schema_info": schema_content,
        "original_question": original_q or "Unknown",
        "validation_attempts": 0,  # Reset counter for new query
        "last_feedback": ""  # Clear previous feedback
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
            schema=SEMANTIC_SCHEMA,
            feedback_section=feedback_section
        )
    )
    
    messages_to_send = [system_message]
    
    # 1. Add relevant conversation history
    user_question = None
    for msg in reversed(state["messages"]):
        if isinstance(msg, HumanMessage):
            user_question = msg
            break
            
    if user_question:
        messages_to_send.append(user_question)
        
    # 2. INJECT FEEDBACK AS DIRECT INSTRUCTION
    if state.get("last_feedback"):
        feedback_msg = HumanMessage(content=f"""
❌ YOUR PREVIOUS QUERY WAS REJECTED BY THE VALIDATOR.

🔍 FEEDBACK & REQUIRED FIXES:
{state['last_feedback']}

👉 ACTION REQUIRED:
Regenerate the SQL query strictly following the VALIDATOR'S instructions.
""")
        messages_to_send.append(feedback_msg)
    
    # 3. Invoke Model
    llm_with_tools = model.bind_tools([run_query_tool], tool_choice="required")
    response = llm_with_tools.invoke(messages_to_send)
    
    # 4. Update State
    current_attempts = state.get("validation_attempts", 0)
    
    return {
        "messages": [response],
        "validation_attempts": current_attempts + 1
    }

def validate_query_with_retry(validation_request: str, question: str, sql: str):
    """Validate query with retry logic for API errors"""
    try:
        validator_response = model.invoke([
            SystemMessage(content=VALIDATOR_SYSTEM_PROMPT.format(
                semantic_schema=SEMANTIC_SCHEMA  # Pass schema to validator
            )),
            HumanMessage(content=validation_request + "\n\nRETURN ONLY JSON: {\"status\": \"APPROVED\" or \"NEEDS_FIX\", ...}")
        ])
        return validator_response.content
    except Exception as e:
        # ... (error handling remains same) ...
        raise

def validate_query(state: EnhancedState):
    """LLM 2: Validate generated query with retry logic"""
    generated_query = None
    original_question = state.get("original_question", "")
    
    # 1. Extract the generated query from the last message
    for msg in reversed(state["messages"]):
        if hasattr(msg, 'tool_calls') and msg.tool_calls:
            generated_query = msg.tool_calls[0]['args']['query']
            break
            
    if not generated_query:
        return {
            "last_feedback": "ERROR: No query was generated to validate.",
            "messages": []
        }

    # 2. Prepare validation request
    validation_request = f"""
USER'S QUESTION:
{original_question}

GENERATED SQL QUERY:
```sql
{generated_query}
```

Validate this query against the SEMANTIC SCHEMA. Provide JSON response only."""
    
    try:
        # 3. Call Validator Model
        validator_response_content = validate_query_with_retry(
            validation_request,
            original_question,
            generated_query
        )
        
        # 4. Parse JSON Response
        content = validator_response_content.strip()
        content = content.replace('```json', '').replace('```', '')
        content = content.strip()
        
        if '{' in content:
            json_start = content.find('{')
            json_end = content.rfind('}') + 1
            json_str = content[json_start:json_end]
        else:
            json_str = content
            
        print(f"[DEBUG] Extracted JSON: {json_str}")
        try:
            validation_result = json.loads(json_str)
            # Handle double-encoded JSON (common LLM error)
            if isinstance(validation_result, str):
                print(f"[DEBUG] Detected double-encoded JSON, parsing again...")
                validation_result = json.loads(validation_result)
        except json.JSONDecodeError:
            # Fallback: try to fix common JSON errors (like unescaped quotes)
            # For now, just raise to trigger retry or fallback
            raise

        if not isinstance(validation_result, dict):
            raise ValueError(f"Validator returned {type(validation_result)}, expected dict")

        # 5. Process Result
        if validation_result.get("status") == "APPROVED":
            print(f"[DEBUG] ✅ Query APPROVED")
            return {
                "last_feedback": "",
                "messages": []
            }
        else:
            # Extract simplified feedback fields
            user_intent = validation_result.get("user_intent_analysis", "")
            sql_logic = validation_result.get("sql_logic_analysis", "")
            errors = validation_result.get("errors", [])
            improvement_steps = validation_result.get("improvement_steps", [])
            
            # Build feedback message
            feedback = "🔍 INTELLIGENT VALIDATION FEEDBACK\n\n"
            if user_intent: feedback += f"🎯 USER'S INTENT:\n{user_intent}\n\n"
            if sql_logic: feedback += f"📊 CURRENT SQL LOGIC:\n{sql_logic}\n\n"
            
            if errors:
                feedback += "❌ ERRORS FOUND:\n"
                for i, error in enumerate(errors, 1):
                    feedback += f"{i}. {error}\n"
                feedback += "\n"
                
            if improvement_steps:
                feedback += "🔧 HOW TO FIX (Step-by-Step):\n"
                for step in improvement_steps:
                    feedback += f"  • {step}\n"
                feedback += "\n"
            
            print(f"[DEBUG] ❌ Query REJECTED")
            return {
                "last_feedback": feedback,
                "messages": []
            }
            
    except json.JSONDecodeError as e:
        print(f"[ERROR] JSON parse error: {e}")
        print(f"[ERROR] Raw content: {validator_response_content[:300]}")
        return {
            "last_feedback": f"Validator returned invalid JSON. Approving query to proceed.",
            "messages": []
        }
    except Exception as e:
        print(f"[ERROR] Validation process failed: {e}")
        # FAIL-SAFE: If validation crashes (e.g. bad JSON), force approval to let query run
        print("[WARN] Validator crashed. Bypassing validation to allow execution.")
        return {
            "last_feedback": "",
            "messages": []
        }
        print(f"[ERROR] Validation failed after retries: {str(e)}")
        # After all retries failed, approve to proceed (fail-open strategy)
        return {
            "last_feedback": f"Validation error after retries: {str(e)}. Approving query to proceed.",
            "messages": []
        }
        print(f"[ERROR] Validation error: {e}")
        return {
            "last_feedback": f"Validation error: {str(e)}. Approving query to proceed.",
            "messages": []
        }

def run_query_node(state: EnhancedState, db=None):
    """Execute query after validation with security checks. 
       Accepts optional 'db' for multi-database support.
    """
    query = None
    tool_call_id = None
    for msg in reversed(state["messages"]):
        if hasattr(msg, 'tool_calls') and msg.tool_calls:
            query = msg.tool_calls[0]['args']['query']
            tool_call_id = msg.tool_calls[0]['id']
            break
            
    # Fallback to content if no tool call (for some agent types)
    if not query:
        # Check if the last message is an AIMessage with content being the SQL
        last_msg = state["messages"][-1]
        if isinstance(last_msg, AIMessage) and "SELECT" in last_msg.content.upper():
            query = last_msg.content
    
    if not query:
        return {"messages": [AIMessage(content="Error: No query found to execute")]}
    
    # 🔒 SECURITY VALIDATION
    is_valid, error_msg, sanitized_query = validate_sql_security(query)
    
    if not is_valid:
        error_response = f"🚨 SECURITY VALIDATION FAILED: {error_msg}"
        return {"messages": [AIMessage(content=error_response)]}
    
    query = sanitized_query
    print(f"[DEBUG] Executing SQL on {'Custom DB' if db else 'Default DB'}: {query}")

    try:
        if db:
            # Direct execution on the passed DB instance
            result = db.run(query)
        else:
            # Logic for default/legacy system (splitting checklist/delegation if needed)
            # ... (Rest of legacy formatting logic if needed, or simple exec)
            result = run_query_tool.invoke({"query": query})
            
        return {"messages": [AIMessage(content=str(result))]}
        
    except Exception as e:
        print(f"[ERROR] Query Execution Failed: {e}")
        return {"messages": [AIMessage(content=f"Error executing query: {str(e)}")]}

# ============================================================================
# CONDITIONAL EDGES
# ============================================================================

def should_validate_or_execute(state: EnhancedState) -> str:
    """Decide after query generation - ALWAYS validate first attempt"""
    last_message = state["messages"][-1]
    
    if not hasattr(last_message, 'tool_calls') or not last_message.tool_calls:
        return END
    
    attempts = state.get("validation_attempts", 0)
    has_feedback = bool(state.get("last_feedback"))
    
    print(f"[DEBUG] Routing decision: attempts={attempts}, has_feedback={has_feedback}, max={settings.MAX_VALIDATION_ATTEMPTS}")
    
    # ALWAYS validate on first attempt (attempts == 1)
    if attempts == 1:
        print(f"[DEBUG] First attempt (1) - routing to validation")
        return "validate_query"
    
    # If we have feedback and haven't exceeded max attempts, validate again
    if has_feedback and attempts <= settings.MAX_VALIDATION_ATTEMPTS:
        print(f"[DEBUG] Attempt {attempts} (max {settings.MAX_VALIDATION_ATTEMPTS}) with feedback - routing to validation")
        return "validate_query"
    
    # If exceeded max attempts or no issues, execute
    if attempts > settings.MAX_VALIDATION_ATTEMPTS:
        print(f"[DEBUG] Exceeded max attempts ({attempts} > {settings.MAX_VALIDATION_ATTEMPTS}) - routing to execution")
    else:
        print(f"[DEBUG] No feedback after attempt {attempts} - routing to execution")
    
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
