"""
Lead-To-Order Workflow
======================
LangGraph workflow for the Lead-To-Order System.
Handles Query Generation -> Validation -> Execution -> Answer Synthesis.
"""

from typing import Dict, Any, List
import json
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END

from app.core.config import settings
from .config import ALLOWED_TABLES
from app.services.agent_nodes import (
    EnhancedState, 
    list_tables, 
    call_get_schema, 
    store_schema, 
    run_query_node
)
from .connection import get_db_instance
from .prompts import GENERATE_QUERY_SYSTEM_PROMPT, ANSWER_SYNTHESIS_SYSTEM_PROMPT, REFORMULATE_QUESTION_PROMPT
from app.services.session_manager import session_manager

from langchain_core.runnables import RunnableConfig

# Initialize Services
db = get_db_instance()
llm = ChatOpenAI(model=settings.LLM_MODEL, temperature=0, openai_api_key=settings.OPENAI_API_KEY)

# ------------------------------------------------------------------
# NODE: Reformulate Question (Context Awareness)
# ------------------------------------------------------------------
def reformulate_question_node(state: EnhancedState, config: RunnableConfig):
    """
    Rewrites the user query based on chat history to include context 
    or ignore it if topic switched.
    """
    messages = state["messages"]
    current_q = messages[0].content
    
    # Get Session ID from config
    session_id = config.get("configurable", {}).get("thread_id")
    
    # Fetch History
    history_msgs = []
    if session_id:
        all_msgs = session_manager.get_session_messages(session_id)
        # Exclude the very last one if it duplicates current_q
        history_msgs = all_msgs[:-1] if all_msgs else []
    
    # Format history as text block
    history_text = "\n".join([f"{m['role']}: {m['content']}" for m in history_msgs[-6:]]) 
    
    # Prompt
    prompt = [
        SystemMessage(content=REFORMULATE_QUESTION_PROMPT),
        HumanMessage(content=f"Chat History:\n{history_text}\n\nCurrent Question:\n{current_q}")
    ]
    
    # Invoke
    response = llm.invoke(prompt)
    rewritten_q = response.content.strip()
    
    print(f"[CONTEXT REFORMULATION] Original: '{current_q}' -> Rewritten: '{rewritten_q}'")
    
    # Update State with Rewritten Query
    return {"messages": [HumanMessage(content=rewritten_q)]}

# ------------------------------------------------------------------
# NODE: Generate Query (Custom for Lead-To-Order)
# ------------------------------------------------------------------
def generate_query_node(state: EnhancedState):
    """Generates SQL query based on Lead-To-Order schema"""
    messages = state["messages"]
    user_query = messages[0].content if messages else ""
    
    # Construct Prompt
    prompt = [
        SystemMessage(content=GENERATE_QUERY_SYSTEM_PROMPT),
        HumanMessage(content=user_query)
    ]
    
    # Invoke LLM
    response = llm.invoke(prompt)
    generated_sql = response.content.strip().replace("```sql", "").replace("```", "")
    
    return {
        "messages": [AIMessage(content=generated_sql)], 
        "validation_attempts": 0,
        "last_feedback": None
    }

# ------------------------------------------------------------------
# NODE: Validate Query
# ------------------------------------------------------------------
def validate_query_node(state: EnhancedState):
    """Basic validation: checking for restricted keywords or obvious errors"""
    messages = state["messages"]
    sql_query = messages[-1].content
    
    # Security Check (Basic) - prevent drop/delete
    if "DROP" in sql_query.upper() or "DELETE" in sql_query.upper() or "UPDATE" in sql_query.upper():
        return {"last_feedback": "SECURITY ERROR: Modification queries are not allowed."}
        
    # We assume 'config.py' allowed columns are enforced by the LLM prompt.
    # In a stricter version, we would parse the SQL here and check columns against config.COLUMNS_RESTRICTION.
    
    return {"last_feedback": None} # None means Approved

# ------------------------------------------------------------------
# CONDITIONAL EDGES
# ------------------------------------------------------------------
def should_continue_validation(state: EnhancedState):
    feedback = state.get("last_feedback")
    attempts = state.get("validation_attempts", 0)
    
    if feedback is None:
        return "approved"  # Go to run_query
        
    if attempts >= 3:
        return "give_up"
        
    return "retry" # Not implemented in this simple loop, effectively fails

# ------------------------------------------------------------------
# GRAPH CONSTRUCTION
# ------------------------------------------------------------------
workflow = StateGraph(EnhancedState)

workflow.add_node("reformulate_question", reformulate_question_node)
workflow.add_node("list_tables", lambda state: list_tables(state, db))
workflow.add_node("get_schema", lambda state: call_get_schema(state, db, ALLOWED_TABLES))
workflow.add_node("generate_query", generate_query_node)
workflow.add_node("validate_query", validate_query_node)
workflow.add_node("run_query", lambda state: run_query_node(state, db))

# Define Flow
workflow.set_entry_point("reformulate_question") 
workflow.add_edge("reformulate_question", "generate_query")
workflow.add_edge("generate_query", "validate_query")

workflow.add_conditional_edges(
    "validate_query",
    should_continue_validation,
    {
        "approved": "run_query",
        "give_up": END, 
        "retry": END # Simple fail-fast for now
    }
)
workflow.add_edge("run_query", END)

# Compile
lead_to_order_app = workflow.compile()
