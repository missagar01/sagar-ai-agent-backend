"""
LangGraph SQL Agent with Dual-LLM Validation
=============================================
Complete port of sagar.ipynb logic:
- LLM 1: Query Generator with 5-step mandatory analysis
- LLM 2: Query Validator with schema-evidence validation
- LangGraph state machine with validation loop
- Human-in-the-loop via interrupt points
"""

from typing import Literal, TypedDict, Annotated, AsyncGenerator
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.graph import END, START, StateGraph, MessagesState
from langgraph.checkpoint.memory import MemorySaver
import json

from app.core.config import settings
from app.core.security import validate_sql_security

# ============================================================================
# RESTRICTED DATABASE ACCESS
# ============================================================================

class RestrictedSQLDatabase(SQLDatabase):
    """Database with table restrictions"""
    def get_usable_table_names(self):
        all_tables = super().get_usable_table_names()
        return [t for t in all_tables if t.lower() in [x.lower() for x in settings.ALLOWED_TABLES]]

# Initialize database
print(f"[DEBUG] Connecting to database: {settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")
try:
    db = RestrictedSQLDatabase.from_uri(settings.DATABASE_URL)
    print(f"[DEBUG] Database connected successfully")
    print(f"[DEBUG] Available tables: {db.get_usable_table_names()}")
except Exception as e:
    print(f"[ERROR] Database connection failed: {e}")
    raise

# Initialize OpenAI model
model = ChatOpenAI(
    model=settings.LLM_MODEL,
    temperature=settings.LLM_TEMPERATURE,
    openai_api_key=settings.OPENAI_API_KEY
)

# Initialize toolkit
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
# SEMANTIC SCHEMA DEFINITION (The "Brain" of the System)
# ============================================================================

SEMANTIC_SCHEMA = """
📊 **DATABASE SEMANTIC SCHEMA & WORKING RULES**
------------------------------------------------------------------------------------------------
This database tracks employee tasks across two main tables (`checklist`, `delegation`) and user info in (`users`).

1. **TABLE: `checklist`** (Routine/Daily Tasks)
   - **Working:** Contains recurring tasks automatically generated or assigned for daily/weekly routines.
   - **Allowed Columns & Usage:**
     * `task_id` (BIGINT): Unique identifier.
     * `name` (TEXT): Name of the person responsible for the task.
     * `department` (TEXT): Department (e.g., 'PC', 'ADMIN').
     * `task_description` (TEXT): Description of work to be done.
     * `frequency` (TEXT): 'Daily', 'Weekly', etc.
     * `task_start_date` (TIMESTAMP): The **SCHEDULED DATE** when the task should be done.
     * `submission_date` (TIMESTAMP): The **ACTUAL COMPLETION DATE**.
         - IF `NULL` → Task is **PENDING**.
         - IF `NOT NULL` → Task is **COMPLETED**.
     * `admin_done` (TEXT): Admin override flag ('Yes'/'No') - rarely used but allowed.
     * `given_by` (TEXT): Who created the routine (usually system or admin).
   - **❌ FORBIDDEN COLUMNS (DO NOT USE):**
     * `status` (Unreliable/Mixed types), `remark`, `image`, `delay`, `planned_date` (Checklist does NOT use planned_date).

2. **TABLE: `delegation`** (One-time/Assigned Tasks)
   - **Working:** Ad-hoc tasks assigned by one person to another with a specific deadline.
   - **Allowed Columns & Usage:**
     * `task_id` (BIGINT): Unique identifier.
     * `name` (TEXT): Name of the person DOING the task (Assignee).
     * `given_by` (TEXT): Name of the person GIVING the task (Assigner).
     * `department` (TEXT): Department.
     * `task_description` (TEXT): Task details.
     * `frequency` (TEXT): usually 'One-time'.
     * `task_start_date` (TIMESTAMP): Date when task was assigned.
     * `planned_date` (TIMESTAMP): The **DUE DATE/DEADLINE**.
     * `submission_date` (TIMESTAMP): The **ACTUAL COMPLETION DATE**.
         - IF `NULL` → Task is **PENDING**.
         - IF `NOT NULL` → Task is **COMPLETED**.
   - **❌ FORBIDDEN COLUMNS (DO NOT USE):**
     * `status`, `remarks`, `image`, `delay` (Calculate delay using SQL instead).

3. **TABLE: `users`** (System Users)
   - **Working:** Employee login and department details.
   - **Allowed:** 
     * `user_name` (TEXT): Employee full name.
     * `department` (TEXT): User's department.
     * `role` (TEXT): 'user' or 'admin'.
     * `given_by` (TEXT): Reporting manager/Assigner.
   - **Forbidden:** `status`, `email_id` (contains PII), `number`.

------------------------------------------------------------------------------------------------
🧠 **LOGIC & CALCULATIONS**
------------------------------------------------------------------------------------------------
1. **PENDING vs COMPLETED:**
   - Always check `submission_date IS NULL` for Pending.
   - Always check `submission_date IS NOT NULL` for Completed.
   - **NEVER** use the `status` column.

2. **DATE FILTERING ("This Month"):**
   - **Standard "This Month":** (Past & Future in month)
     `task_start_date >= DATE_TRUNC('month', CURRENT_DATE) AND task_start_date < DATE_TRUNC('month', CURRENT_DATE) + INTERVAL '1 month'`
   - **"This Month Till Today":** (Dashboard Style)
     `task_start_date >= DATE_TRUNC('month', CURRENT_DATE) AND task_start_date < CURRENT_DATE + INTERVAL '1 day'`

3. **PERFORMANCE REPORTS:**
   - Must include BOTH `checklist` and `delegation` tables (UNION ALL).
   - Metrics: Total, Completed, Pending, Overdue (Delegation only), On-time.
"""

# ============================================================================
# LLM 1: GENERATOR PROMPT (Intent -> Schema -> SQL)
# ============================================================================

GENERATE_QUERY_SYSTEM_PROMPT = """You are an EXPERT SQL GENERATOR for a Task Management System.

Your ONLY responsibility:
→ Understand the USER'S INTENT
→ Strictly follow the SEMANTIC SCHEMA and Analyse it
→ Generate the CORRECT PostgreSQL SQL query

You MUST NOT explain anything.
You MUST NOT validate correctness.
You MUST NOT redesign the database.
Output ONLY the SQL query via the tool.

────────────────────────────────────────────────────────────
SEMANTIC SCHEMA (SOURCE OF TRUTH)
────────────────────────────────────────────────────────────
{schema}

Current Date: {current_date}

────────────────────────────────────────────────────────────
CONTEXT AWARENESS (CRITICAL)
────────────────────────────────────────────────────────────
If the input contains "⚠️ CONTEXT FROM PREVIOUS QUERY":
1. You MUST apply the previous filters (e.g., `name`, `department`, `task_start_date`) to the current query UNLESS the user explicitly overrides them.
2. Example:
   - Context says: "Previous user: name = 'Hem Kumar'"
   - User asks: "how many pending tasks?"
   - Your SQL MUST include: `LOWER(name) = LOWER('Hem Kumar')`
3. Failure to carry over context (especially user names) is a CRITICAL ERROR.

────────────────────────────────────────────────────────────
MANDATORY INTERNAL INTENT ANALYSIS (DO NOT OUTPUT)
────────────────────────────────────────────────────────────
Before writing SQL, you MUST internally determine the intent
using the following intent dimensions:

- intent_type:
    • count
    • list
    • performance
    • summary

- tables_required:
    • checklist
    • delegation
    • both

- time_basis:
    • scheduled_date  → task_start_date
    • completion_date → submission_date

- time_range:
    • full_month
    • month_till_today
    • custom_range

- task_state:
    • pending    → submission_date IS NULL
    • completed  → submission_date IS NOT NULL
    • all

- filters:
    • user_name
    • department
    • none

This intent object is ONLY for reasoning.
DO NOT print or expose it.

────────────────────────────────────────────────────────────
SQL GENERATION RULES (STRICT)
────────────────────────────────────────────────────────────
1. Use ONLY allowed tables and columns.
2. NEVER use forbidden columns.
3. NEVER use `status` for task state.
4. Pending vs Completed MUST rely on `submission_date`.
5. Date filters MUST follow semantic rules.
6. If BOTH tables are required:
   - Use UNION ALL
   - Include a column: `source_table`
7. Use PostgreSQL syntax only.
8. Cast TEXT dates explicitly when required.
9. Output ONLY SQL. No markdown. No explanation.
10. **CRITICAL:** Always use `LOWER(column) = LOWER('Value')` for names (e.g., `LOWER(name) = LOWER('Hem Kumar Jagat')`). Never compare string literals directly without LOWER().

────────────────────────────────────────────────────────────
FEEDBACK FROM PREVIOUS ATTEMPT (IF ANY)
────────────────────────────────────────────────────────────
{feedback_section}

Now generate the SQL query.

"""

# ============================================================================
# LLM 2: VALIDATOR PROMPT (Schema Analysis & Feedback)
# ============================================================================

VALIDATOR_SYSTEM_PROMPT = """You are a STRICT SQL VALIDATOR and SCHEMA ENFORCER.

Your ONLY responsibility:
→ Check whether the SQL correctly matches the USER'S INTENT
→ Verify compliance with the SEMANTIC SCHEMA

You MUST NOT rewrite SQL.
You MUST NOT optimize SQL.
You MUST NOT propose alternative designs.

────────────────────────────────────────────────────────────
SEMANTIC SCHEMA (SOURCE OF TRUTH)
────────────────────────────────────────────────────────────
{semantic_schema}

────────────────────────────────────────────────────────────
VALIDATION CHECKS (IN ORDER)
────────────────────────────────────────────────────────────

1. INTENT MATCH
- Does the SQL answer exactly what the user asked?
- Example:
  • "completed tasks" → submission_date IS NOT NULL
  • "pending tasks"   → submission_date IS NULL

2. SCHEMA COMPLIANCE
- Are only allowed tables used?
- Are any FORBIDDEN columns used?
  → If YES, REJECT immediately.

3. DATE LOGIC
- Is "this month" interpreted correctly?
- Is "till today" respected when asked?
- Is the correct date column used
  (task_start_date vs submission_date)?

4. MULTI-TABLE LOGIC
- If BOTH checklist and delegation are required:
  → UNION ALL must be used
  → source_table column must exist

────────────────────────────────────────────────────────────
STRICT RULES (NON-NEGOTIABLE)
────────────────────────────────────────────────────────────
- DO NOT redesign the query.
- DO NOT suggest alternate logic.
- DO NOT optimize performance.
- DO NOT add new filters.

You may ONLY:
1. APPROVE the query, OR
2. REJECT it with precise reasons and fix steps.

────────────────────────────────────────────────────────────
OUTPUT FORMAT (JSON ONLY)
────────────────────────────────────────────────────────────
{{
  "status": "APPROVED" | "NEEDS_FIX",
  "confidence": 0-100,
  "reasoning": "Short explanation",
  "user_intent_analysis": "What the user asked",
  "sql_logic_analysis": "What the SQL does",
  "errors": [
    "Specific schema or intent violation"
  ],
  "improvement_steps": [
    "Exact fix required (no redesign)"
  ]
}}

"""

# Continue in next file...
