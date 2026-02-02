"""
Central Router
==============
Decides which database agent to use for a given user query.
Currently defaults to 'checklist', but extensible for multi-db.
"""

from typing import Literal, Optional
from langchain_openai import ChatOpenAI
from app.core.config import settings

# Import the workflow apps from the database modules
from app.databases.checklist.workflow import workflow_app as checklist_app

# ============================================================================
# ROUTER LOGIC (AI-POWERED)
# ============================================================================

from langchain_core.messages import SystemMessage, HumanMessage

# Initialize lightweight router LLM (cheap & fast model preferred)
router_llm = ChatOpenAI(
    model="gpt-4o-mini", # Use fast model for routing
    temperature=0,
    openai_api_key=settings.OPENAI_API_KEY
)

# Import Metadata for Dynamic Discovery
from app.databases.checklist.config import ROUTER_METADATA as CHECKLIST_META
from app.databases.lead_to_order.config import ROUTER_METADATA as L2O_META

# Registry of Available Databases
REGISTERED_DATABASES = [CHECKLIST_META, L2O_META]

def _build_router_prompt() -> str:
    """
    Dynamically constructs the router system prompt based on registered databases.
    """
    db_descriptions = ""
    for i, db in enumerate(REGISTERED_DATABASES, 1):
        keywords = ", ".join(db["keywords"])
        db_descriptions += f"""
{i}. '{db["name"]}'
   - Scope: {db["description"]}
   - Keywords: {keywords}.
"""

    return f"""
You are the Database Router. Classify the user query into one of the available databases.

AVAILABLE DATABASES:
{db_descriptions}

INSTRUCTIONS:
- Analyze the user's intent.
- Return a JSON object with:
  - "database": The selected database name (one of the names above or 'AMBIGUOUS').
  - "reason": A short explanation of WHY you chose this.
  - "clarification_question": (If AMBIGUOUS) A polite question asking the user to clarify (e.g. "Did you mean sales users or task users?").

Example Output:
{{
  "database": "AMBIGUOUS",
  "reason": "Both databases have users.",
  "clarification_question": "I see users in both the Sales and Checklist systems. Which list are you looking for?"
}}
"""

def determine_database(query: str) -> tuple[str, str, str]:
    """
    Analyzes the user query using LLM to determine target database.
    Returns: (db_name, reasoning, clarification_question)
    """
    try:
        # Generate prompt dynamically
        system_prompt = _build_router_prompt()
        
        response = router_llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=query)
        ])
        
        content = response.content.strip()
        
        # Clean markdown if present
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()
            
        import json
        data = json.loads(content)
        
        db_name = data.get("database", "AMBIGUOUS").lower()
        reason = data.get("reason", "No reason provided.")
        clarification_question = data.get("clarification_question", "Could you please clarify which database you mean?")
        
        # Check against registered names
        for db in REGISTERED_DATABASES:
            if db["name"] in db_name:
                return db["name"], reason, ""
            
        return "AMBIGUOUS", reason, clarification_question
        
    except Exception as e:
        print(f"[ROUTER ERROR] Failed to route query: {e}")
        return "checklist", "Router encountered an error, defaulting to main system.", ""

def get_agent_for_database(db_name: str = "checklist"):
    """
    Factory function to return the correct compiled LangGraph agent.
    """
    if db_name == "lead_to_order":
        from app.databases.lead_to_order.workflow import lead_to_order_app
        return lead_to_order_app
        
    # Default
    return checklist_app

# ============================================================================
# HELPER FOR STREAMING RESPONSES
# ============================================================================

# ============================================================================
# HELPER FOR STREAMING RESPONSES (GENERIC)
# ============================================================================

# Initialize a dedicated LLM to avoid import loops
answer_llm = ChatOpenAI(
    model=settings.LLM_MODEL,
    temperature=0,
    openai_api_key=settings.OPENAI_API_KEY
)

def create_answer_generator(system_prompt: str):
    """
    Creates a generic async generator function for answer synthesis.
    Now accepts (query, sql_result, sql_query) to match legacy signature.
    """
    async def answer_gen(query: str, sql_result: str, sql_query: str):
        # ----------------------------------------------------
        # 1. MAIN ANSWER STREAM (The "What")
        # ----------------------------------------------------
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Question: {query}\n\nSQL Query: {sql_query}\n\nSQL Result: {sql_result}")
        ]
        
        try:
            async for chunk in answer_llm.astream(messages):
                yield chunk.content
        except Exception as e:
            yield f"Error generating answer: {e}"

        # ----------------------------------------------------
        # 2. TECHNICAL NOTE (The "How")
        # ----------------------------------------------------
        # We append this at the end, just like the original system.
        note_prompt = f"""You are a SQL Expert. Explain the logic of the following SQL query in a single natural language note.

SQL Query: 
{sql_query}

INSTRUCTIONS:
- Output a single parenthetical note.
- Format: `(Note: ...)`
- Explain which tables were queried.
- **CRITICAL:** Explicitly name the columns used.
- Example: "(Note: To find this, I queried the `enquiry_to_order` table, filtered `timestamp` for last month...)"

Generate ONLY the note:"""

        try:
            yield "\n\n" # Spacing
            technical_note_msg = await answer_llm.ainvoke([HumanMessage(content=note_prompt)])
            yield technical_note_msg.content
        except Exception as e:
            print(f"[NOTE GEN ERROR] {e}")


    return answer_gen

def get_answer_generator(db_name: str = "checklist"):
    """
    Returns the specific answer generator function for the DB.
    Each DB might have different formatting styles.
    """
    if db_name == "lead_to_order":
        from app.databases.lead_to_order.prompts import ANSWER_SYNTHESIS_SYSTEM_PROMPT
        return create_answer_generator(ANSWER_SYNTHESIS_SYSTEM_PROMPT)
    
    # Default Checklist
    from app.databases.checklist.prompts import ANSWER_SYNTHESIS_SYSTEM_PROMPT
    return create_answer_generator(ANSWER_SYNTHESIS_SYSTEM_PROMPT)
