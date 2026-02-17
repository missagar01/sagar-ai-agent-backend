"""
Checklist System - Configuration
================================
Defines schema, allowed columns, and business rules.
"""

# Router Metadata (Used for Auto-Discovery)
ROUTER_METADATA = {
    "name": "checklist",
    "description": "A comprehensive Task, Employee, HR & Admin Operations System. It tracks recurring daily/weekly routines (checklist), one-time assigned duties (delegation), employee leave requests (leave_request), travel/ticket bookings (ticket_book, request), plant visitor approvals (plant_visitor), and candidate/resume intake for hiring (resume_request). Use this database for queries related to employee task completion rates, pending daily duties, ad-hoc task delegation, leave applications, travel requests, visitor passes, hiring pipeline, and departmental task summaries.",
    "keywords": [
        "task", "pending", "completed", "late", "given by", "department", 
        "users", "report", "summary", "checklist system", "task db", 
        "employee", "delegation", "performance", "attendance", "routine",
        "ticket", "booking", "travel", "bill", "ticket amount", "charges",
        "leave", "leave request", "hr approval", "approved", "absent",
        "plant visitor", "visit", "visitor", "visitor approval",
        "request", "travel request", "departure", "city",
        "resume", "candidate", "hiring", "interview", "joined", "designation"
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
        "submission_date",
        "status"
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
    ],
    "ticket_book": [
        "person_name",
        "type_of_bill",
        "status",
        "bill_number",
        "per_ticket_amount",
        "total_amount",
        "charges"
    ],
    "leave_request": [
        "employee_name",
        "from_date",
        "to_date",
        "reason",
        "request_status",
        "approved_by",
        "hr_approval",
        "mobilenumber",
        "urgent_mobilenumber",
        "commercial_head_status",
        "approve_dates"
    ],
    "plant_visitor": [
        "person_name",
        "reason_for_visit",
        "no_of_person",
        "from_date",
        "to_date",
        "requester_name",
        "request_status",
        "approve_by_name"
    ],
    "request": [
        "person_name",
        "from_date",
        "to_date",
        "type_of_travel",
        "no_of_person",
        "departure_date",
        "reason_for_travel",
        "from_city",
        "to_city",
        "request_quantity"
    ],
    "resume_request": [
        "id",
        "candidate_name",
        "candidate_email",
        "candidate_mobile",
        "applied_for_designation",
        "req_id",
        "experience",
        "previous_company",
        "previous_salary",
        "reason_for_changing",
        "marital_status",
        "reference",
        "address_present",
        "resume",
        "interviewer_planned",
        "interviewer_actual",
        "interviewer_status",
        "candidate_status",
        "joined_status",
        "created_at",
        "updated_at"
    ]
}

# Semantic Schema Description
SEMANTIC_SCHEMA = """
📊 **DATABASE SEMANTIC SCHEMA & WORKING RULES**
------------------------------------------------------------------------------------------------
This database tracks employee tasks (`checklist`, `delegation`), user info (`users`),
and administrative modules: ticket bookings (`ticket_book`), leave management (`leave_request`),
plant visit approvals (`plant_visitor`), travel/hiring requests (`request`), and candidate
resume intake for HR (`resume_request`).

--- TASK MANAGEMENT TABLES ---

1. **TABLE: `checklist`** (Routine/Daily Tasks)
   - **Working:** Contains recurring tasks automatically generated or assigned for daily/weekly routines.
   - **Allowed Columns & Usage:**
     * `task_id` (BIGINT): Unique identifier.
     * `name` (TEXT): Name of the person responsible for the task.
     * `department` (TEXT): Department (e.g., 'PC', 'ADMIN').
     * `task_description` (TEXT): Description of work to be done.
     * `frequency` (TEXT): 'Daily', 'Weekly', etc.
         - ⚠️ INCONSISTENT CASING: Values include 'daily', 'Daily', 'weekly', 'Weekly', 'monthly', 'Monthly', 'one-time', 'one time', etc. Always use LOWER() for comparisons.
     * `task_start_date` (TIMESTAMP): The **SCHEDULED DATE** when the task should be done.
     * `submission_date` (TIMESTAMP): The **ACTUAL COMPLETION DATE**.
         - IF `NULL` -> Task is **PENDING**.
         - IF `NOT NULL` -> Task is **SUBMITTED** (Check `status` for 'Done' vs 'Not Done').
     * `status` (TEXT): The outcome of the task.
         - 'Yes'/'yes' -> **COMPLETED**.
         - 'No'/'no' -> **NOT DONE**.
         - ⚠️ Always use LOWER(status) for comparisons.
     * `admin_done` (TEXT): Admin override flag. Values: 'confirmed', 'Confirmed', 'Done', 'No'. Use LOWER().
     * `given_by` (TEXT): Who created the routine (usually system or admin).
   - **❌ FORBIDDEN COLUMNS (DO NOT USE):**
     * `remark`, `image`, `delay`, `planned_date`, `enable_reminder`, `require_attachment`, `created_at`, `user_status_checklist`

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
         - IF `NULL` -> Task is **PENDING**.
         - IF `NOT NULL` -> Task is **COMPLETED**.
   - **❌ FORBIDDEN COLUMNS (DO NOT USE):**
     * `status`, `remarks`, `image`, `delay`, `enable_reminder`, `require_attachment`, `created_at`, `updated_at`, `color_code_for`

3. **TABLE: `users`** (System Users)
   - **Working:** Employee login and department details.
   - **Allowed:**
     * `user_name` (TEXT): Employee full name.
     * `department` (TEXT): User's department.
     * `role` (TEXT): 'user' or 'admin'. Use LOWER() for comparisons.
     * `given_by` (TEXT): Reporting manager/Assigner.
     * `email_id` (TEXT): User email address (Nullable).
     * `number` (BIGINT): Contact number (Nullable).
     * `status` (VARCHAR): User status. Currently only 'active'. Use LOWER() for comparisons.
     * `password` (TEXT): User login password (Manager Access Only).
   - **Forbidden:** `id`, `created_at`, `user_access`, `leave_date`, `remark`, `leave_end_date`, `employee_id`, `last_punch_time`, `last_punch_device`, `page_access`, `system_access`, `subscription_access_system`, `user_access1`, `store_access`, `emp_image`, `verify_access`, `verify_access_dept`, `store_role_access`, `designation`, `profile_img`, `document_img`

--- ADMIN/HR TABLES ---

4. **TABLE: `ticket_book`** (Ticket Booking / Travel Bills)
   - **Working:** Records travel ticket bookings and billing details for employees.
   - **Allowed Columns & Usage:**
     * `person_name` (VARCHAR(255)): Name of the traveler/person the ticket is for.
     * `type_of_bill` (VARCHAR(50)): Category/type of the bill.
     * `status` (VARCHAR(50)): Workflow/payment status of the ticket booking.
     * `bill_number` (VARCHAR(50)): Invoice/bill reference number.
     * `per_ticket_amount` (NUMERIC): Cost per ticket.
     * `total_amount` (NUMERIC): Total payable amount.
     * `charges` (NUMERIC): Additional charges/fees.
   - **❌ FORBIDDEN COLUMNS (DO NOT USE):**
     * `id`, `travels_name`, `upload_bill_image`, `booked_name`, `created_at`, `updated_at`, `request_employee_code`, `booked_employee_code`
   - **LOGIC:**
     * Use LOWER(person_name) = LOWER('...') for name comparisons.
     * For total cost analysis, SUM(total_amount) or SUM(per_ticket_amount + charges).

5. **TABLE: `leave_request`** (Employee Leave Applications)
   - **Working:** Employee leave application workflow with multi-step approvals (Manager/HOD → HR → Commercial Head).
   - **Allowed Columns & Usage:**
     * `employee_name` (VARCHAR): Full name of the employee requesting leave.
     * `from_date` (DATE): Leave start date.
     * `to_date` (DATE): Leave end date.
     * `reason` (TEXT): Reason for leave.
     * `request_status` (VARCHAR): Overall leave request status.
         - Possible values: 'Pending', 'Approved', 'Rejected', etc. Use LOWER() for comparisons.
     * `approved_by` (VARCHAR): Name of the Manager/HOD who approved.
     * `hr_approval` (VARCHAR): HR approval status label.
     * `mobilenumber` (VARCHAR): Employee mobile number.
     * `urgent_mobilenumber` (VARCHAR): Emergency/alternate contact number.
     * `commercial_head_status` (VARCHAR): Commercial head's approval status (if applicable).
     * `approve_dates` (TIMESTAMP/DATE): Date when fully approved.
   - **❌ FORBIDDEN COLUMNS (DO NOT USE):**
     * `id`, `employee_id`, `designation`, `department`, `user_id`, `approved_by_status`, `approval_hr`, `created_at`, `updated_at`
   - **LOGIC:**
     * **Pending leaves:** LOWER(request_status) = 'pending'
     * **Approved leaves:** LOWER(request_status) = 'approved'
     * **Leave duration:** (to_date - from_date + 1) for number of days.
     * Always use LOWER() for status and name comparisons.

6. **TABLE: `plant_visitor`** (Plant Visit Requests)
   - **Working:** Tracks planned plant visit requests (different from visitor gate pass), including headcount and approval workflow.
   - **Allowed Columns & Usage:**
     * `person_name` (VARCHAR(150)): Name of the visitor/party.
     * `reason_for_visit` (TEXT): Why the visit is needed.
     * `no_of_person` (INTEGER): Number of visitors in the group.
     * `from_date` (DATE): Visit start date.
     * `to_date` (DATE): Visit end date.
     * `requester_name` (VARCHAR(150)): Employee who requested the visit.
     * `request_status` (VARCHAR(50)): Approval/workflow status.
         - Possible values: 'Pending', 'Approved', 'Rejected', etc. Use LOWER() for comparisons.
     * `approve_by_name` (VARCHAR(150)): Name of the person who approved the visit.
   - **❌ FORBIDDEN COLUMNS (DO NOT USE):**
     * `id`, `employee_code`, `request_for`, `remarks`, `approv_employee_code`, `created_at`, `updated_at`
   - **LOGIC:**
     * **Pending visits:** LOWER(request_status) = 'pending'
     * **Approved visits:** LOWER(request_status) = 'approved'
     * Use LOWER() for all name and status comparisons.

7. **TABLE: `request`** (Travel & Generic Requests)
   - **Working:** Handles travel requests, manpower requests, and other generic requests with date ranges and travel details.
   - **Allowed Columns & Usage:**
     * `person_name` (VARCHAR(100)): Primary person related to the request.
     * `from_date` (DATE): Start date of travel/request period.
     * `to_date` (DATE): End date of travel/request period.
     * `type_of_travel` (VARCHAR(50)): Travel type (e.g., 'bus', 'train', 'flight').
     * `no_of_person` (INTEGER): Number of people.
     * `departure_date` (DATE): Departure date.
     * `reason_for_travel` (VARCHAR(255)): Reason/justification for travel.
     * `from_city` (VARCHAR(100)): Origin city.
     * `to_city` (VARCHAR(100)): Destination city.
     * `request_quantity` (INTEGER): Quantity requested (e.g., number of positions or tickets).
   - **❌ FORBIDDEN COLUMNS (DO NOT USE):**
     * `id`, `request_no`, `requester_name`, `requester_designation`, `requester_department`, `request_for`, `experience`, `education`, `remarks`, `request_status`, `created_at`, `updated_at`, `employee_code`
   - **LOGIC:**
     * Use LOWER() for all name and categorical value comparisons.
     * Use LOWER(type_of_travel) for filtering by travel type.

8. **TABLE: `resume_request`** (Candidate/Resume Intake for Hiring)
   - **Working:** Stores candidate applications, interview scheduling, and hiring pipeline status.
   - **ALL COLUMNS ALLOWED:**
     * `id` (BIGINT): Unique candidate record identifier.
     * `candidate_name` (VARCHAR(255)): Candidate's full name.
     * `candidate_email` (VARCHAR(255)): Candidate's email address.
     * `candidate_mobile` (VARCHAR(20)): Candidate's phone number.
     * `applied_for_designation` (VARCHAR(255)): Role/designation applied for.
     * `req_id` (VARCHAR(100)): Associated requisition/request ID.
     * `experience` (NUMERIC(4,1)): Total years of experience.
     * `previous_company` (VARCHAR(255)): Last employer.
     * `previous_salary` (NUMERIC(12,2)): Prior salary.
     * `reason_for_changing` (TEXT): Reason for job change.
     * `marital_status` (VARCHAR(50)): Marital status.
     * `reference` (VARCHAR(255)): Reference source/person.
     * `address_present` (TEXT): Current address.
     * `resume` (TEXT): Resume file URL/path.
     * `interviewer_planned` (TIMESTAMP): Planned interview date/time.
     * `interviewer_actual` (TIMESTAMP): Actual interview date/time.
     * `interviewer_status` (VARCHAR(100)): Interview outcome/status.
     * `candidate_status` (VARCHAR(50)): Candidate pipeline status.
     * `joined_status` (VARCHAR(10)): Whether candidate joined ('yes'/'no'). Use LOWER() for comparisons.
     * `created_at` (TIMESTAMP): Record creation timestamp.
     * `updated_at` (TIMESTAMP): Record last update timestamp.
   - **❌ FORBIDDEN COLUMNS:** None (All columns are allowed).
   - **LOGIC:**
     * **Joined candidates:** LOWER(joined_status) = 'yes'
     * **Pending interviews:** interviewer_planned IS NOT NULL AND interviewer_actual IS NULL
     * **Completed interviews:** interviewer_actual IS NOT NULL
     * Use LOWER() for all status and name comparisons.

------------------------------------------------------------------------------------------------
🧠 **LOGIC & CALCULATIONS**
------------------------------------------------------------------------------------------------
1. **TASK STATES (Valid only for Checklist):**
   - **Pending:** `submission_date IS NULL`
   - **Completed:** `submission_date IS NOT NULL` AND `(LOWER(status) = 'yes' OR LOWER(status) = 'done')`
   - **Not Done:** `submission_date IS NOT NULL` AND `LOWER(status) = 'no'`
   - **Legacy Note:** Delegation table does NOT use status; rely only on submission_date for it.

2. **DATE FILTERING ("This Month"):**
   - **Standard "This Month":** (Past & Future in month)
     `task_start_date >= DATE_TRUNC('month', CURRENT_DATE) AND task_start_date < DATE_TRUNC('month', CURRENT_DATE) + INTERVAL '1 month'`
   - **"This Month Till Today":** (Dashboard Style)
     `task_start_date >= DATE_TRUNC('month', CURRENT_DATE) AND task_start_date < CURRENT_DATE + INTERVAL '1 day'`
   - **For leave_request/plant_visitor/request:** Use `from_date` and `to_date` as the date range columns.

3. **PERFORMANCE REPORTS:**
   - Must include BOTH `checklist` and `delegation` tables (UNION ALL).
   - Metrics: Total, Completed, Pending, Overdue (Delegation only), On-time.

4. **STRING COMPARISON (CRITICAL FOR ALL TABLES):**
   - ⚠️ ALWAYS use `LOWER(column) = LOWER('Value')` for any TEXT/VARCHAR comparisons.
   - Names, statuses, and categorical values have inconsistent casing across all tables.
   - Example: `LOWER(person_name) = LOWER('Hem Kumar')`, `LOWER(request_status) = LOWER('pending')`

5. **ADMIN/HR TABLE STATES:**
   - **Leave Pending:** `LOWER(request_status) = 'pending'`
   - **Leave Approved:** `LOWER(request_status) = 'approved'`
   - **Visit Pending:** `LOWER(request_status) = 'pending'` in plant_visitor
   - **Interview Pending:** `interviewer_actual IS NULL AND interviewer_planned IS NOT NULL` in resume_request
   - **Candidate Joined:** `LOWER(joined_status) = 'yes'` in resume_request
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
