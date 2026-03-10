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
# Initialize database
# print(f"[DEBUG] Connecting to default database: {settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")
try:
    db = RestrictedSQLDatabase.from_uri(settings.DATABASE_URL)
    # print(f"[DEBUG] Default Database connected successfully")
    # print(f"[DEBUG] Available tables: {db.get_usable_table_names()}")
except Exception as e:
    print(f"[ERROR] Default Database connection failed: {e}")
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
This database tracks employee tasks (`checklist`, `delegation`), user info (`users`),
and administrative modules: ticket bookings (`ticket_book`), leave management (`leave_request`),
travel/hiring requests (`request`), candidate resume intake for HR (`resume_request`),
and visitor gate pass tracking (`visitors`).

--- TASK MANAGEMENT TABLES ---

1. **TABLE: `checklist`** (Routine/Daily Tasks)
   - **Working:** Contains recurring tasks automatically generated or assigned for daily/weekly routines.
   - **Allowed Columns & Usage:**
     * `task_id` (BIGINT): Unique identifier.
     * `name` (TEXT): Name of the person responsible for the task.
     * `department` (TEXT): Department (e.g., 'PC', 'ADMIN').
     * `task_description` (TEXT): Description of work to be done.
     * `frequency` (TEXT): 'Daily', 'Weekly', etc. ⚠️ INCONSISTENT CASING – use LOWER().
     * `task_start_date` (TIMESTAMP): The **SCHEDULED DATE** when the task should be done.
     * `submission_date` (TIMESTAMP): The **ACTUAL COMPLETION DATE**.
         - IF `NULL` → Task is **PENDING**.
         - IF `NOT NULL` → Task is **SUBMITTED** (Check `status` for 'Yes' vs 'No').
     * `status` (TEXT): The outcome of the task. 'Yes'/'yes' → COMPLETED. 'No'/'no' → NOT DONE. Use LOWER().
     * `admin_done` (TEXT): Admin override flag. Use LOWER().
     * `given_by` (TEXT): Who created the routine.
   - **❌ FORBIDDEN COLUMNS (DO NOT USE):**
     * `remark`, `image`, `delay`, `planned_date`, `enable_reminder`, `require_attachment`, `created_at`

2. **TABLE: `delegation`** (One-time/Assigned Tasks)
   - **Working:** Ad-hoc tasks assigned by one person to another with a specific deadline.
   - **Allowed Columns & Usage:**
     * `task_id` (BIGINT): Unique identifier.
     * `name` (TEXT): Name of the person DOING the task (Assignee).
     * `given_by` (TEXT): Name of the person GIVING the task (Assigner).
     * `department` (TEXT): Department.
     * `task_description` (TEXT): Task details.
     * `frequency` (TEXT): usually 'one-time'.
     * `task_start_date` (TIMESTAMP): Date when task was assigned.
     * `planned_date` (TIMESTAMP): The **DUE DATE/DEADLINE**.
     * `submission_date` (TIMESTAMP): The **ACTUAL COMPLETION DATE**.
         - IF `NULL` → Task is **PENDING**.
         - IF `NOT NULL` → Task is **COMPLETED**.
   - **❌ FORBIDDEN COLUMNS (DO NOT USE):**
     * `status`, `remarks`, `image`, `delay`, `enable_reminder`, `require_attachment`

3. **TABLE: `users`** (System Users)
   - **Working:** Employee login and department details.
   - **Allowed:**
     * `user_name` (TEXT): Employee full name.
     * `department` (TEXT): User's department.
     * `role` (TEXT): 'user' or 'admin'. Use LOWER().
     * `given_by` (TEXT): Reporting manager/Assigner.
     * `email_id` (TEXT): User email address.
     * `number` (BIGINT): Contact number.
     * `status` (VARCHAR): User status. Use LOWER().
     * `password` (TEXT): User login password.

--- ADMIN / HR TABLES ---

4. **TABLE: `ticket_book`** (Ticket Bookings & Travel Bills)
   - **Working:** Records travel ticket bookings, bills, and associated charges.
   - **Allowed Columns:**
     * `person_name` (TEXT): Person for whom ticket is booked.
     * `type_of_bill` (TEXT): Bill category. Values: 'self', 'company'. Use LOWER().
     * `status` (TEXT): Bill status. Values: 'pending', 'approved', 'rejected'. Use LOWER().
     * `bill_number` (TEXT): Unique bill/invoice number.
     * `per_ticket_amount` (NUMERIC): Cost per ticket.
     * `total_amount` (NUMERIC): Total billing amount.
     * `charges` (NUMERIC): Additional charges.
   - **❌ FORBIDDEN:** `id`, `user_id`, `created_at`, `updated_at`

5. **TABLE: `leave_request`** (Employee Leave Management)
   - **Working:** Tracks employee leave applications and multi-level approvals.
   - **Allowed Columns:**
     * `employee_name` (TEXT): Employee who requested leave.
     * `from_date` (DATE): Leave start date.
     * `to_date` (DATE): Leave end date.
     * `reason` (TEXT): Reason for leave.
     * `request_status` (TEXT): Values: 'pending', 'approved', 'rejected'. Use LOWER().
     * `approved_by` (TEXT): Manager who approved.
     * `hr_approval` (TEXT): HR approval status. Use LOWER().
     * `mobilenumber` (TEXT): Employee contact.
     * `urgent_mobilenumber` (TEXT): Emergency contact.
     * `commercial_head_status` (TEXT): Commercial head approval. Use LOWER().
     * `approve_dates` (TEXT): Dates approved for leave.
   - **❌ FORBIDDEN:** `id`, `user_id`, `created_at`, `updated_at`

6. **TABLE: `visitors`** (Visitor Gate Pass / Entry Log)
   - **Working:** Tracks visitors entering the company premises, their gate pass approval, entry/exit times, and whom they visited.
   - **Allowed Columns:**
     * `visitor_name` (VARCHAR(100)): Full name of the visitor. Use LOWER() for comparisons.
     * `mobile_number` (VARCHAR(15)): Visitor's mobile number.
     * `visitor_photo` (TEXT): Photo URL of the visitor (Nullable).
     * `visitor_address` (TEXT): Address/company of the visitor.
     * `purpose_of_visit` (TEXT): Reason for visiting the premises.
     * `person_to_meet` (VARCHAR(100)): Employee/person the visitor came to meet. Use LOWER() for comparisons.
     * `date_of_visit` (DATE): Date when visitor arrived.
     * `time_of_entry` (TIME): Clock time when visitor entered.
     * `visitor_out_time` (TIME): Clock time when visitor exited (NULL if still inside).
     * `approval_status` (VARCHAR(20)): Gate pass approval status. Known values: 'approved'. Use LOWER().
     * `approved_by` (VARCHAR(100)): Name of person who approved the visit. Use LOWER().
     * `approved_at` (TIMESTAMP): Timestamp when gate pass was approved.
     * `status` (VARCHAR(10)): Current visitor status. Values: 'IN', 'OUT'. Use LOWER().
   - **❌ FORBIDDEN:** `id`, `gate_pass_closed`, `created_at`

7. **TABLE: `request`** (Travel Requests)
   - **Working:** Tracks employee travel requests with route and mode details.
   - **Allowed Columns:**
     * `person_name` (TEXT): Traveler's name.
     * `from_date` (DATE): Travel start date.
     * `to_date` (DATE): Travel end date.
     * `type_of_travel` (TEXT): Values: 'flight', 'train', 'bus', 'cab'. Use LOWER().
     * `no_of_person` (INTEGER): Number of travelers.
     * `departure_date` (DATE): Departure date.
     * `reason_for_travel` (TEXT): Travel purpose.
     * `from_city` (TEXT): Origin city.
     * `to_city` (TEXT): Destination city.
     * `request_quantity` (INTEGER): Number of tickets requested.
   - **❌ FORBIDDEN:** `id`, `user_id`, `created_at`, `updated_at`

8. **TABLE: `resume_request`** (Candidate/Resume Intake for Hiring)
   - **Working:** Tracks candidates, interview scheduling, and joining status.
   - **Allowed Columns (ALL):**
     * `id` (BIGINT): Unique identifier.
     * `candidate_name` (TEXT): Candidate's full name.
     * `candidate_email` (TEXT): Email address.
     * `candidate_mobile` (TEXT): Phone number.
     * `applied_for_designation` (TEXT): Job role applied for.
     * `req_id` (TEXT): Requisition/job posting ID.
     * `experience` (NUMERIC(4,1)): Years of experience.
     * `previous_company` (TEXT): Last employer.
     * `previous_salary` (NUMERIC(12,2)): Last drawn salary.
     * `reason_for_changing` (TEXT): Why changing jobs.
     * `marital_status` (TEXT): Marital status.
     * `reference` (TEXT): Referral source.
     * `address_present` (TEXT): Current address.
     * `resume` (TEXT): Resume file path/link.
     * `interviewer_planned` (TIMESTAMP): Planned interview date.
     * `interviewer_actual` (TIMESTAMP): Actual interview date.
     * `interviewer_status` (TEXT): Interview result. Use LOWER().
     * `candidate_status` (TEXT): Overall candidate status. Use LOWER().
     * `joined_status` (TEXT): Values: 'yes', 'no', 'pending'. Use LOWER().
     * `created_at` (TIMESTAMP): Record creation time.
     * `updated_at` (TIMESTAMP): Last update time.

------------------------------------------------------------------------------------------------
🧠 **LOGIC & CALCULATIONS**
------------------------------------------------------------------------------------------------
1. **TASK STATES (Checklist/Delegation):**
   - **Pending:** `submission_date IS NULL`
   - **Completed:** `submission_date IS NOT NULL` (AND `LOWER(status) = 'yes'` for checklist)
   - **Not Done:** `submission_date IS NOT NULL` AND `LOWER(status) = 'no'` (checklist only)
   - Delegation does NOT use status; rely only on submission_date.

2. **APPROVAL STATES (leave_request):**
   - **Pending:** `LOWER(request_status) = 'pending'`
   - **Approved:** `LOWER(request_status) = 'approved'`
   - **Rejected:** `LOWER(request_status) = 'rejected'`

2b. **VISITOR STATES (visitors):**
   - **Inside:** `LOWER(status) = 'in'`
   - **Left:** `LOWER(status) = 'out'`
   - **Approved:** `LOWER(approval_status) = 'approved'`

3. **HIRING STATES (resume_request):**
   - **Interview Pending:** `interviewer_actual IS NULL`
   - **Joined:** `LOWER(joined_status) = 'yes'`

4. **DATE FILTERING ("This Month"):**
   - `task_start_date >= DATE_TRUNC('month', CURRENT_DATE) AND task_start_date < DATE_TRUNC('month', CURRENT_DATE) + INTERVAL '1 month'`

5. **PERFORMANCE REPORTS:**
   - Must include BOTH `checklist` and `delegation` tables (UNION ALL).

6. **🔴 CRITICAL STRING RULE:**
   - ALWAYS use `LOWER(column) = LOWER('Value')` for ALL text comparisons across ALL tables.
"""

# ============================================================================
# LLM 1: GENERATOR PROMPT (Intent -> Schema -> SQL)
# ============================================================================

GENERATE_QUERY_SYSTEM_PROMPT = """You are an EXPERT SQL GENERATOR for a Task Management & HR Operations System AND an AI ANALYTICS MANAGER for the company.

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
TABLE ROUTING (Decide which table to query)
────────────────────────────────────────────────────────────
• Tasks/checklists/daily routines/weekly → checklist
• Delegated tasks/assigned/one-time → delegation
• Performance/report/summary (tasks) → checklist + delegation (UNION ALL)
• Employee info/users/login details → users
• Ticket bookings/travel bills/ticket amount → ticket_book
• Leave/absence/leave request/HR approval → leave_request
• Travel request/departure/city/travel type → request
• Resume/candidate/hiring/interview/joined → resume_request
• Visitor gate pass/visitor entry/visitor exit/person to meet → visitors

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
    • both (checklist + delegation)
    • ticket_book
    • leave_request
    • request
    • resume_request
    • users
    • visitors

- time_basis:
    • scheduled_date  → task_start_date (for checklist/delegation)
    • completion_date → submission_date (for checklist/delegation)
    • date_range      → from_date/to_date (for leave_request, request)
    • visit_date      → date_of_visit (for visitors)
    • interview_date  → interviewer_planned/interviewer_actual (for resume_request)

- time_range:
    • full_month
    • month_till_today
    • custom_range

- task_state:
    • pending    → submission_date IS NULL (checklist/delegation)
    • completed  → submission_date IS NOT NULL (checklist/delegation)
    • leave_pending → LOWER(request_status) = 'pending' (leave_request)
    • leave_approved → LOWER(request_status) = 'approved' (leave_request)
    • visitor_inside → LOWER(status) = 'in' (visitors)
    • visitor_left → LOWER(status) = 'out' (visitors)
    • visit_approved → LOWER(approval_status) = 'approved' (visitors)
    • interview_pending → interviewer_actual IS NULL (resume_request)
    • joined → LOWER(joined_status) = 'yes' (resume_request)
    • all

- filters:
    • user_name
    • department
    • person_name
    • employee_name
    • candidate_name
    • visitor_name
    • person_to_meet
    • none

This intent object is ONLY for reasoning.
DO NOT print or expose it.

────────────────────────────────────────────────────────────
SQL GENERATION RULES (STRICT)
────────────────────────────────────────────────────────────
1. Use ONLY allowed tables and columns from the SEMANTIC SCHEMA.
2. NEVER use forbidden columns.
3. For checklist/delegation: NEVER use `status` for task state. Pending vs Completed MUST rely on `submission_date`.
4. For leave_request: Use `request_status` for approval state.
4b. For visitors: Use `status` for in/out state and `approval_status` for gate pass approval.
5. Date filters MUST follow semantic rules.
6. If BOTH checklist and delegation are required:
   - Use UNION ALL
   - Include a column: `source_table`
7. Use PostgreSQL syntax only.
8. Cast TEXT dates explicitly when required.
9. Output ONLY SQL. No markdown. No explanation.
10. **CRITICAL:** Always use `LOWER(column) = LOWER('Value')` for ALL string comparisons across ALL tables.
    Never compare string literals directly without LOWER().
11. **ENUM/CATEGORICAL VALUES:** Use exact values from the schema with LOWER() normalization.
12. **NUMERIC COLUMNS:** ticket_book amounts, resume_request experience/salary are NUMERIC. Use SUM/AVG/COUNT for aggregations.

────────────────────────────────────────────────────────────
HINDI / HINGLISH GLOSSARY (CRITICAL — Bilingual Users)
────────────────────────────────────────────────────────────
Users often write in Hindi or Hinglish. You MUST translate
these words correctly. DO NOT treat Hindi words as person
names, column values, or filters.

Common Hindi words (NEVER use as filter values):
  • "datta" / "data" → means "data" / "records" (NOT a person name)
  • "kitne" / "kitna" → "how many" / "how much"
  • "dikhao" / "dikha do" / "batao" → "show" / "display"
  • "aaj" / "aaj ka" → "today" / "today's"
  • "kal" → "yesterday" or "tomorrow" (infer from context)
  • "nhi" / "nahi" / "na" → "not" / "no" (negation)
  • "ho gaya" / "hua" / "ho chuka" → "completed" / "done"
  • "sabka" / "sabki" / "sab" → "everyone's" / "all"
  • "wale" / "wali" → "ones" / "those" (e.g., "pending wale" = "pending ones")
  • "kis" / "kaun" → "which" / "who"
  • "kaha" / "kahan" → "where"
  • "report" → "summary/report" (aggregate query)
  • "total" → "count" or "sum" depending on context
  • "approve" / "reject" → approval/rejection status
  • "chutti" / "chhutti" → "leave" (leave_request table)
  • "visitor" / "mehman" → visitors table
  • "ticket" → ticket_book table

⚠️ RULE: If a word like "datta", "sabka", "kitne", "dikhao"
appears in the query, it is a HINDI WORD, NOT a person name.
Do NOT put it in a WHERE clause as a filter value.

────────────────────────────────────────────────────────────
NEGATION-AWARE INTENT RULES (CRITICAL)
────────────────────────────────────────────────────────────
Handle negation precisely. "not X" means everything EXCEPT X:

• "not approved" / "approve nhi hua" / "reject ya pending"
  → LOWER(request_status) != 'approved' OR request_status IS NULL
  (includes BOTH 'pending' AND 'rejected')

• "approved" / "approve ho gaya"
  → LOWER(request_status) = 'approved'

• "rejected" / "reject ho gaya"
  → LOWER(request_status) = 'rejected'

• "pending" / "abhi tak pending"
  → LOWER(request_status) = 'pending' OR request_status IS NULL

• "not completed" / "complete nhi hua" (for tasks)
  → submission_date IS NULL

• "completed" / "ho gaya" (for tasks)
  → submission_date IS NOT NULL

• "not joined" / "join nhi kiya" (for resume_request)
  → LOWER(joined_status) != 'yes' OR joined_status IS NULL

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
