"""
Checklist System - Workflow Logic
=================================
Defines the LangGraph Agent, nodes, and tools for the Checklist Database.
"""

from typing import Literal, TypedDict, Annotated, AsyncGenerator, Dict, Any, List
from datetime import datetime
import json
import re

from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.graph import END, START, StateGraph, MessagesState
from langgraph.checkpoint.memory import MemorySaver

from app.core.config import settings
from app.core.security import validate_sql_security

# Local Imports
from .connection import get_db_instance
from . import config
from . import prompts

# ============================================================================
# INITIALIZATION (DB & TOOLS)
# ============================================================================

# Initialize DB connection specific to this module
db = get_db_instance()

# Initialize LLM
model = ChatOpenAI(
    model=settings.LLM_MODEL,
    temperature=settings.LLM_TEMPERATURE,
    openai_api_key=settings.OPENAI_API_KEY
)

# Initialize Toolkit & Tools
toolkit = SQLDatabaseToolkit(db=db, llm=model)
tools = toolkit.get_tools()

get_schema_tool = next(t for t in tools if t.name == "sql_db_schema")
list_tables_tool = next(t for t in tools if t.name == "sql_db_list_tables")
run_query_tool = next(t for t in tools if t.name == "sql_db_query")


# ============================================================================
# STATE DEFINITION
# ============================================================================

class EnhancedState(MessagesState):
    """Enhanced state to track validation loops"""
    validation_attempts: int = 0
    last_feedback: str = ""
    schema_info: str = ""
    original_question: str = ""


# ============================================================================
# HELPER: NATURAL ANSWER GENERATOR
# ============================================================================
# This is exported so the API/Router can call it after the graph finishes.

def generate_natural_answer(user_question: str, query_result: str, sql_query: str) -> str:
    """Convert raw SQL results to natural language answer using LLM"""
    
    # Parse query result to check for source_table column logic (UNION ALL)
    # (Same logic as original)
    has_source_breakdown = False
    checklist_count = 0
    delegation_count = 0
    
    try:
        result_str = str(query_result)
        if "'checklist'" in result_str or "'delegation'" in result_str or "'source_table'" in result_str.lower():
            has_source_breakdown = True
            checklist_matches = re.findall(r"checklist.*?(\d+)", result_str, re.IGNORECASE)
            delegation_matches = re.findall(r"delegation.*?(\d+)", result_str, re.IGNORECASE)
            if checklist_matches: checklist_count = int(checklist_matches[0])
            if delegation_matches: delegation_count = int(delegation_matches[0])
    except Exception as e:
        print(f"[DEBUG] Result parsing error: {e}")
    
    breakdown_info = ""
    if has_source_breakdown and (checklist_count > 0 or delegation_count > 0):
        breakdown_info = f"\n[Source Breakdown Data]:\n- Checklist: {checklist_count:,}\n- Delegation: {delegation_count:,}\n- Total: {checklist_count + delegation_count:,}\n"

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
        llm_direct = ChatOpenAI(model=settings.LLM_MODEL, temperature=0, openai_api_key=settings.OPENAI_API_KEY)
        
        full_answer_msg = llm_direct.invoke(answer_prompt)
        main_answer = full_answer_msg.content.strip()
        
        technical_note_msg = llm_direct.invoke(note_prompt)
        technical_note = technical_note_msg.content.strip()
        
        return f"{main_answer}\n\n{technical_note}"
        
    except Exception as e:
        print(f"[ERROR] Answer generation failed: {e}")
        return f"Query Results: {query_result}\n\n(Note: SQL Logic explanation failed to generate.)"


# ============================================================================
# GRAPH NODES
# ============================================================================

def list_tables(state: EnhancedState):
    """Get available table names"""
    # Simply invoke tool. In future, we could filter strictly for this DB.
    tables = list_tables_tool.invoke("")
    return {"messages": [AIMessage(content=f"Available tables: {tables}")]}

def call_get_schema(state: EnhancedState):
    """Fetch complete schema with samples and add type warnings"""
    # All allowed tables in the checklist database
    target_tables = [
        "checklist", "delegation", "users",
        "ticket_book", "leave_request", "plant_visitor",
        "request", "resume_request",
        "master", "all_loans", "request_forclosure", "collect_noc",
        "subscription", "approval_history", "payment_history", "subscription_renewals",
        "documents", "sharedocuments", "payment_fms"
    ]
    
    tables_str = ", ".join(target_tables)
    schema = get_schema_tool.invoke({"table_names": tables_str})
    
    # Build description string dynamically from config for each table
    desc_checklist = config.get_columns_description('checklist')
    desc_delegation = config.get_columns_description('delegation')
    desc_users = config.get_columns_description('users')
    desc_ticket_book = config.get_columns_description('ticket_book')
    desc_leave_request = config.get_columns_description('leave_request')
    desc_plant_visitor = config.get_columns_description('plant_visitor')
    desc_request = config.get_columns_description('request')
    desc_resume_request = config.get_columns_description('resume_request')
    desc_master = config.get_columns_description('master')
    desc_all_loans = config.get_columns_description('all_loans')
    desc_request_forclosure = config.get_columns_description('request_forclosure')
    desc_collect_noc = config.get_columns_description('collect_noc')
    desc_subscription = config.get_columns_description('subscription')
    desc_approval_history = config.get_columns_description('approval_history')
    desc_payment_history = config.get_columns_description('payment_history')
    desc_subscription_renewals = config.get_columns_description('subscription_renewals')
    desc_documents = config.get_columns_description('documents')
    desc_sharedocuments = config.get_columns_description('sharedocuments')
    desc_payment_fms = config.get_columns_description('payment_fms')

    column_restrictions = f"""
🔒 COLUMN RESTRICTIONS (Client Requirement):
═══════════════════════════════════════════════════════════════════════════════
ONLY use these columns in your queries:

📋 CHECKLIST table: {desc_checklist}
📌 DELEGATION table: {desc_delegation}
👤 USERS table: {desc_users}
🎫 TICKET_BOOK table: {desc_ticket_book}
🏖️ LEAVE_REQUEST table: {desc_leave_request}
🏭 PLANT_VISITOR table: {desc_plant_visitor}
✈️ REQUEST table: {desc_request}
📄 RESUME_REQUEST table: {desc_resume_request}
🔧 MASTER table: {desc_master}
🏦 ALL_LOANS table: {desc_all_loans}
📝 REQUEST_FORCLOSURE table: {desc_request_forclosure}
📜 COLLECT_NOC table: {desc_collect_noc}
📑 SUBSCRIPTION table: {desc_subscription}
✅ APPROVAL_HISTORY table: {desc_approval_history}
💳 PAYMENT_HISTORY table: {desc_payment_history}
🔄 SUBSCRIPTION_RENEWALS table: {desc_subscription_renewals}
📂 DOCUMENTS table: {desc_documents}
📤 SHAREDOCUMENTS table: {desc_sharedocuments}
💰 PAYMENT_FMS table: {desc_payment_fms}

❌ DO NOT query or SELECT any other columns from these tables.
═══════════════════════════════════════════════════════════════════════════════
"""
    # Warning block (could also be moved to config/prompts, but hardcoding for safety)
    enhanced_schema = f"""{column_restrictions}

{schema}

⚠️ CRITICAL DATA TYPE WARNINGS:
═══════════════════════════════════════════════════════════════════════════════
🔴 TEXT DATE COLUMNS (Require ::DATE casting):
   - checklist.planned_date (TEXT) -> Use: planned_date::DATE
   - delegation.planned_date (TEXT) -> Use: planned_date::DATE

🟢 NATIVE DATE/TIMESTAMP COLUMNS:
   - checklist.task_start_date (TIMESTAMP)
   - checklist.submission_date (TIMESTAMP)
   - leave_request.from_date (DATE), leave_request.to_date (DATE)
   - plant_visitor.from_date (DATE), plant_visitor.to_date (DATE)
   - request.from_date (DATE), request.to_date (DATE), request.departure_date (DATE)
   - ticket_book.created_at (TIMESTAMP)
   - resume_request.interviewer_planned (TIMESTAMP), resume_request.interviewer_actual (TIMESTAMP)

🔵 NUMERIC COLUMNS:
   - ticket_book: per_ticket_amount, total_amount, charges (NUMERIC)
   - resume_request: experience (NUMERIC(4,1)), previous_salary (NUMERIC(12,2))
═══════════════════════════════════════════════════════════════════════════════
"""
    return {"messages": [AIMessage(content=enhanced_schema)]}

def store_schema(state: EnhancedState):
    """Store schema in state"""
    last_msg = state["messages"][-1]
    schema_content = last_msg.content
    
    original_q = None
    for msg in reversed(state["messages"]):
        if isinstance(msg, HumanMessage):
            original_q = msg.content
            break
            
    return {
        "schema_info": schema_content,
        "original_question": original_q or "Unknown",
        "validation_attempts": 0,
        "last_feedback": ""
    }

def generate_query(state: EnhancedState):
    """LLM 1: Generate Query"""
    # Use local prompts
    feedback_section = ""
    if state.get("last_feedback"):
        feedback_section = f"\n⚠️ PREVIOUS ATTEMPT ISSUES:\n{state['last_feedback']}\n\nREGENERATE WITH FIXES.\n"
    
    system_content = prompts.GENERATOR_SYSTEM_PROMPT.format(
        current_date=datetime.now().strftime("%Y-%m-%d"),
        schema=config.SEMANTIC_SCHEMA,
        feedback_section=feedback_section
    )
    
    messages_to_send = [SystemMessage(content=system_content)]
    
    # Add User Question
    user_question = None
    for msg in reversed(state["messages"]):
        if isinstance(msg, HumanMessage):
            user_question = msg
            break
    if user_question:
        messages_to_send.append(user_question)
        
    # Inject Feedback explicitly
    if state.get("last_feedback"):
        messages_to_send.append(HumanMessage(content=f"❌ REJECTED. FIX: {state['last_feedback']}"))
        
    # Bind tool
    llm_with_tools = model.bind_tools([run_query_tool], tool_choice="required")
    response = llm_with_tools.invoke(messages_to_send)
    
    return {
        "messages": [response],
        "validation_attempts": state.get("validation_attempts", 0) + 1
    }

def validate_query(state: EnhancedState):
    """LLM 2: Validate Query"""
    generated_query = None
    original_question = state.get("original_question", "")
    
    for msg in reversed(state["messages"]):
        if hasattr(msg, 'tool_calls') and msg.tool_calls:
            generated_query = msg.tool_calls[0]['args']['query']
            break
            
    if not generated_query:
        return {"last_feedback": "ERROR: No query generated.", "messages": []}

    validation_request = f"""
USER'S QUESTION:
{original_question}

GENERATED SQL QUERY:
```sql
{generated_query}
```

Validate this query against the SEMANTIC SCHEMA. Provide JSON response only.
"""
    try:
        system_content = prompts.VALIDATOR_SYSTEM_PROMPT.format(
            semantic_schema=config.SEMANTIC_SCHEMA
        )
        validator_response = model.invoke([
            SystemMessage(content=system_content),
            HumanMessage(content=validation_request)
        ])
        
        # Parse logic (simplified from original for brevity, but logically identical)
        content = validator_response.content.strip()
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
            
        result = json.loads(content)
        
        if result.get("status") == "APPROVED":
            print(f"[DEBUG-Checklist] Query APPROVED")
            return {"last_feedback": "", "messages": []}
        else:
            print(f"[DEBUG-Checklist] Query REJECTED")
            errors = "\n".join([f"- {e}" for e in result.get("errors", [])])
            fixes = "\n".join([f"- {f}" for f in result.get("improvement_steps", [])])
            feedback = f"VALIDATION FAILED:\nErrors:\n{errors}\n\nRequired Fixes:\n{fixes}"
            return {"last_feedback": feedback, "messages": []}
            
    except Exception as e:
        print(f"[WARN] Validator error: {e}. Allowing query.")
        return {"last_feedback": "", "messages": []}

def run_query_node(state: EnhancedState):
    """Execute Query"""
    query = None
    tool_call_id = None
    for msg in reversed(state["messages"]):
        if hasattr(msg, 'tool_calls') and msg.tool_calls:
            query = msg.tool_calls[0]['args']['query']
            tool_call_id = msg.tool_calls[0]['id']
            break
            
    if not query:
        return {"messages": [AIMessage(content="Error: No query logic found.")]}
        
    print(f"[DEBUG-Checklist] Executing: {query}")
    
    # Security Check
    is_valid, error_msg, sanitized = validate_sql_security(query)
    if not is_valid:
        return {"messages": [ToolMessage(content=f"Security Block: {error_msg}", tool_call_id=tool_call_id)]}
        
    query = sanitized
    
    # Handle Separated Results for Checklist/Delegation (Specific to this system)
    is_complex = 'checklist' in query.lower() and 'delegation' in query.lower() and 'union' not in query.lower()
    
    if is_complex:
         # Split execution logic (Simplified for port)
         res = run_query_tool.invoke({"query": query})
         # Note: Full split logic omitted for brevity as UNION ALL is preferred by new prompts
         tool_resp = ToolMessage(content=str(res), tool_call_id=tool_call_id)
    else:
        res = run_query_tool.invoke({"query": query})
        tool_resp = ToolMessage(content=str(res), tool_call_id=tool_call_id)
        
    return {"messages": [tool_resp]}


# ============================================================================
# CONDITIONAL EDGES
# ============================================================================

def should_validate_or_execute(state: EnhancedState) -> str:
    # Logic to loop based on attempts
    attempts = state.get("validation_attempts", 0)
    if attempts == 1 or (state.get("last_feedback") and attempts <= settings.MAX_VALIDATION_ATTEMPTS):
        return "validate_query"
    return "run_query"

def should_regenerate_or_approve(state: EnhancedState) -> str:
    if state.get("last_feedback"):
        return "generate_query"
    return "run_query"


# ============================================================================
# BUILD & COMPILE APP
# ============================================================================

def build_workflow():
    builder = StateGraph(EnhancedState)
    
    builder.add_node("list_tables", list_tables)
    builder.add_node("call_get_schema", call_get_schema)
    builder.add_node("store_schema", store_schema)
    builder.add_node("generate_query", generate_query)
    builder.add_node("validate_query", validate_query)
    builder.add_node("run_query", run_query_node)
    
    builder.add_edge(START, "list_tables")
    builder.add_edge("list_tables", "call_get_schema")
    builder.add_edge("call_get_schema", "store_schema")
    builder.add_edge("store_schema", "generate_query")
    
    builder.add_conditional_edges(
        "generate_query", should_validate_or_execute,
        {"validate_query": "validate_query", "run_query": "run_query", END: END}
    )
    
    builder.add_conditional_edges(
        "validate_query", should_regenerate_or_approve,
        {"generate_query": "generate_query", "run_query": "run_query"}
    )
    
    builder.add_edge("run_query", END)
    
    checkpointer = MemorySaver()
    return builder.compile(checkpointer=checkpointer)

# EXPORTED APP
workflow_app = build_workflow()
