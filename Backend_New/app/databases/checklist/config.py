"""
Checklist System - Configuration
================================
Defines schema, allowed columns, and business rules.
"""

# Router Metadata (Used for Auto-Discovery)
ROUTER_METADATA = {
    "name": "checklist",
    "description": "A comprehensive Task & Employee Performance System. It tracks recurring daily/weekly routines (checklist) and one-time assigned duties (delegation). Use this database for queries related to employee task completion rates, pending daily duties, ad-hoc task delegation between staff, user attendance/performance reports, and departmental task summaries. It focuses on the 'workforce' and their 'to-do lists'.",
    "keywords": [
        "task", "pending", "completed", "late", "given by", "department", 
        "users", "report", "summary", "checklist system", "task db", 
        "employee", "delegation", "performance", "attendance", "routine"
    ]
}

# Allowed columns per table (client requirement)
ALLOWED_COLUMNS = {
    "checklist": [
        "task_id",
        "department",
        "given_by",
        "name",
        "task_description",
        "frequency",
        "admin_done",
        "task_start_date",
        "submission_date"
    ],
    "delegation": [
        "task_id",
        "department",
        "name",
        "task_description",
        "frequency",
        "task_start_date",
        "given_by",
        "planned_date",
        "submission_date"
    ],
    "users": [
        "user_name",
        "password",
        "given_by",
        "role",
        "department",
        "email_id",
        "number",
        "status"
    ]
}

# Semantic Schema Description
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
         - IF `NULL` -> Task is **PENDING**.
         - IF `NOT NULL` -> Task is **COMPLETED**.
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
         - IF `NULL` -> Task is **PENDING**.
         - IF `NOT NULL` -> Task is **COMPLETED**.
   - **❌ FORBIDDEN COLUMNS (DO NOT USE):**
     * `status`, `remarks`, `image`, `delay` (Calculate delay using SQL instead).

3. **TABLE: `users`** (System Users)
   - **Working:** Employee login and department details.
   - **Allowed:** 
     * `user_name` (TEXT): Employee full name.
     * `department` (TEXT): User's department.
     * `role` (TEXT): 'user' or 'admin'.
     * `given_by` (TEXT): Reporting manager/Assigner.
     * `email_id` (TEXT): User email address (Nullable).
     * `number` (BIGINT): Contact number (Nullable).
     * `status` (USER-DEFINED/ENUM): User status (e.g. 'active').
     * `password` (TEXT): User login password (Manager Access Only).
   - **Forbidden:** None (Manager has full access).

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

def get_column_list(table_name: str) -> list:
    """Get allowed columns for a table"""
    return ALLOWED_COLUMNS.get(table_name.lower(), [])

def filter_schema_columns(table_name: str, columns: list) -> list:
    """Filter schema columns to only allowed ones"""
    allowed = get_column_list(table_name)
    if not allowed:
        return columns
    
    return [col for col in columns if col.get('column_name', '').lower() in [a.lower() for a in allowed]]

def get_columns_description(table_name: str) -> str:
    """Get formatted column list for prompts"""
    cols = get_column_list(table_name)
    return ", ".join(cols) if cols else "all columns"
# (No Change Needed - SEMANTIC_SCHEMA is already there)
# Just a placeholder to ensure the tool call valid
