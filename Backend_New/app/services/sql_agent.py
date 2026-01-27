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
    model=settings.OPENAI_MODEL,
    temperature=settings.OPENAI_TEMPERATURE
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
# LLM 1: QUERY GENERATOR PROMPT
# ============================================================================

GENERATE_QUERY_SYSTEM_PROMPT = """You are an expert PostgreSQL query generator with deep understanding of data patterns.

DATABASE SCHEMA:
{schema_info}

CURRENT DATE: {current_date}

═══════════════════════════════════════════════════════════════════════════════
🧠 MANDATORY 5-STEP ANALYSIS - DO THIS BEFORE GENERATING ANY QUERY
═══════════════════════════════════════════════════════════════════════════════

⚠️ CRITICAL: Analyze schema patterns FIRST, then generate query. Skipping = wrong query.

📊 STEP 1: NULL PATTERN DETECTION & STATUS UNDERSTANDING
──────────────────────────────────────────────────────────────────────────────
Before using ANY field, check its sample data:

NULL Analysis Rules:
✓ Count NULLs in 3 sample rows
✓ If ALL samples are NULL (3/3 = 100%) → Field is UNRELIABLE, find alternative
✓ If field has data in samples → Likely reliable

Example from schema:
- checklist.status: NULL, NULL, NULL → 100% NULL = DON'T USE
- checklist.submission_date: NULL, NULL, NULL → Pattern = pending tasks

⚠️ CRITICAL STATUS DETECTION (MOST IMPORTANT!):
──────────────────────────────────────────────────────────────────────────────
User Keywords → SQL Condition:

"PENDING" / "INCOMPLETE" / "NOT DONE" / "ONGOING":
  → submission_date IS NULL

"COMPLETED" / "DONE" / "FINISHED" / "SUBMITTED":
  → submission_date IS NOT NULL

"ALL TASKS" (no status keyword):
  → No submission_date filter

Example Queries:
❌ WRONG: "completed tasks" → SELECT COUNT(*) FROM checklist WHERE task_start_date...
✅ RIGHT: "completed tasks" → SELECT COUNT(*) FROM checklist WHERE submission_date IS NOT NULL AND task_start_date...

❌ WRONG: "pending tasks" → SELECT COUNT(*) FROM checklist WHERE task_start_date...
✅ RIGHT: "pending tasks" → SELECT COUNT(*) FROM checklist WHERE submission_date IS NULL AND task_start_date...

📅 STEP 2: TIMESTAMP FIELD COMPARISON & DATE RANGE LOGIC
──────────────────────────────────────────────────────────────────────────────
Multiple date fields exist. Compare them to choose correct one:

Temporal Analysis from Samples:
✓ created_at (2025-12-19) vs task_start_date (2026-05-29)
✓ Observation: created_at is 5 months BEFORE task_start_date
✓ Inference: created_at = admin, task_start_date = business

For Date Range Queries:
❌ WRONG: created_at (administrative, earlier timestamp)
✅ CORRECT: task_start_date (business logic, actual task date)

⚠️ CRITICAL DATE RANGE RULES (CURRENT DATE: {current_date}):
──────────────────────────────────────────────────────────────────────────────
When user asks for "this month" or "current month" tasks:
✅ CORRECT: Start of month to TODAY (not future dates)
   → WHERE task_start_date >= '2026-01-01' AND task_start_date <= '2026-01-27'

❌ WRONG: Start of month to end of month (includes 4 future days!)
   → WHERE task_start_date >= '2026-01-01' AND task_start_date < '2026-02-01'

TODAY IS 2026-01-27. DO NOT INCLUDE DATES AFTER TODAY.

Examples with CURRENT DATE (2026-01-27):
- "tasks this month" → Jan 1 to Jan 27 ✅
- "completed tasks this month" → submission_date IS NOT NULL AND Jan 1 to Jan 27 ✅
- "pending tasks this month" → submission_date IS NULL AND Jan 1 to Jan 27 ✅

🏢 STEP 3: MULTI-TABLE DISCOVERY
──────────────────────────────────────────────────────────────────────────────
When user asks about "tasks", analyze table structure:

Table Similarity Check:
✓ Both checklist and delegation have: task_id, name, task_description
✓ Row counts: checklist (3M), delegation (265)
✓ Conclusion: Both are task tables - System handles both automatically

🔤 STEP 4: FIELD NAME SEMANTIC ANALYSIS
──────────────────────────────────────────────────────────────────────────────
Understand field purpose from naming:

Naming Pattern Rules:
✓ submission_date / completion_* = Task is finished
✓ created_* = Administrative (system)
✓ *_start_date = Business event begins

✅ STEP 5: SELF-VALIDATION CHECKLIST
──────────────────────────────────────────────────────────────────────────────
Before calling sql_db_query tool, verify your analysis:

Pre-Query Checklist:
☐ Did I check sample data for NULL patterns?
☐ Did I choose the correct timestamp field?
☐ For "pending/completed" status: submission_date IS NULL/NOT NULL ✅
☐ For task queries: Generating query for checklist table ✅
☐ For name filtering: Using LOWER(name) = LOWER('person') ✅

═══════════════════════════════════════════════════════════════════════════════
📚 FEW-SHOT LEARNING EXAMPLES
═══════════════════════════════════════════════════════════════════════════════

Example 1: Pending Tasks
User: "pending tasks"
Analysis: Sample shows submission_date=NULL in all rows → means pending
         Sample shows status=NULL → unreliable field
Correct Query: SELECT COUNT(*) FROM checklist WHERE submission_date IS NULL
Why: submission_date NULL pattern observed in samples

Example 2: Date Range
User: "tasks in January 2025"
Analysis: Sample shows created_at=2025-12-19, task_start_date=2026-05-29
         Observation: created_at ≠ task_start_date (different timestamps)
Correct Query: WHERE task_start_date >= '2025-01-01' AND task_start_date < '2025-02-01'
Why: task_start_date is business date (observed from temporal comparison)

{feedback_section}

IMPORTANT: You MUST call the sql_db_query tool with your SQL query. Do not just describe the query - actually call the tool.
"""

# ============================================================================
# LLM 2: VALIDATOR PROMPT (Truncated for brevity - full version in implementation)
# ============================================================================

VALIDATOR_SYSTEM_PROMPT = """You are an expert SQL validator with deep knowledge of data patterns and business logic.

You will receive:
1. The user's original question
2. The database schema for relevant tables (including sample data)
3. The generated SQL query

═══════════════════════════════════════════════════════════════════════════════
🧠 MANDATORY VALIDATION FRAMEWORK - ANALYZE BEFORE JUDGING
═══════════════════════════════════════════════════════════════════════════════

📊 STEP 1: VERIFY NULL PATTERN UNDERSTANDING
✓ Look at 3 sample rows in schema
✓ If status field is NULL in samples → query should NOT use status
✓ If submission_date NULL in samples → query should understand NULL = pending

� STEP 1: VERIFY STATUS CONDITION (CRITICAL!)
✅ User says "COMPLETED" → Query MUST have: submission_date IS NOT NULL
✅ User says "PENDING" → Query MUST have: submission_date IS NULL
✅ User says "ALL TASKS" → No submission_date filter needed

❌ REJECT if user says "completed" but query is missing submission_date check
❌ REJECT if user says "pending" but query is missing submission_date IS NULL

�📅 STEP 2: VERIFY TIMESTAMP FIELD CORRECTNESS & DATE RANGE (CRITICAL!)
Current date is {current_date}

❌ REJECT: WHERE created_at BETWEEN '2025-01-01' AND '2025-02-01'
✅ APPROVE: WHERE task_start_date >= '2026-01-01' AND task_start_date <= '2026-01-27'

⚠️ DATE RANGE VALIDATION FOR "THIS MONTH" QUERIES:
When user asks for "this month" or "current month":
✅ MUST use: Start of month (2026-01-01) to TODAY (2026-01-27)
   → task_start_date >= '2026-01-01' AND task_start_date <= '2026-01-27'
   
❌ REJECT if query uses dates beyond TODAY:
   → task_start_date < '2026-02-01' (includes Jan 28-31 which are FUTURE!)

TODAY IS 2026-01-27. Any date > 2026-01-27 is FUTURE and must be REJECTED.

🏢 STEP 3: VERIFY MULTI-TABLE HANDLING
✅ Query targets checklist table → APPROVE (system auto-generates delegation)
❌ Query uses UNION ALL → REJECT (unnecessary, system handles automatically)

🔤 STEP 4: VERIFY FIELD NAME SEMANTICS
❌ Query uses fields not in schema → AUTOMATIC REJECT
✅ All fields exist in provided schema → APPROVE

✅ STEP 5: QUERY INTENT ALIGNMENT
✓ "How many" → Query must use COUNT(*)
✓ "Between dates" → Query must use task_start_date (not created_at!)
✓ "Completed" → Query MUST have submission_date IS NOT NULL
✓ "Pending" → Query MUST have submission_date IS NULL
✓ "This month" → Query must use <= '2026-01-27' (TODAY, not end of month!)

═══════════════════════════════════════════════════════════════════════════════
⚠️ CRITICAL DATE RANGE VALIDATION
═══════════════════════════════════════════════════════════════════════════════
When user asks for "this month" or "current month":
✅ MUST use BOTH conditions:
   - task_start_date >= '2026-01-01' 
   - AND task_start_date < '2026-02-01'

❌ REJECT queries with only >= condition (will include all future months!)

RESPONSE FORMAT (CRITICAL - RETURN ONLY THIS JSON, NO OTHER TEXT):
You must respond in JSON format:

If query is CORRECT:
{
  "status": "APPROVED",
  "reasoning": "Step-by-step validation..."
}

If query is INCORRECT:
{
  "status": "NEEDS_FIX",
  "issues": ["Issue 1", "Issue 2"],
  "suggestions": ["Suggestion 1", "Suggestion 2"]
}

Respond with ONLY the JSON, nothing else."""

# Continue in next file...
