"""
Checklist System - Configuration
================================
Defines schema, allowed columns, and business rules.
"""

# Router Metadata (Used for Auto-Discovery)
ROUTER_METADATA = {
    "name": "checklist",
    "description": "A comprehensive Task, Employee, HR, Admin, Finance & Subscription Operations System. It tracks recurring daily/weekly routines (checklist), one-time assigned duties (delegation), employee leave requests (leave_request), travel/ticket bookings (ticket_book, request), plant visitor approvals (plant_visitor), candidate/resume intake for hiring (resume_request), company subscriptions & renewals (subscription, subscription_renewals, approval_history, payment_history), company/personal document management (documents, sharedocuments), loan & finance tracking (all_loans, request_forclosure, collect_noc), payment processing (payment_fms), and maintenance task master data (master). Use this database for queries related to employee task completion, delegation, leave, travel, visitor passes, hiring, subscription status, renewal tracking, approval history, payment records, loan details, EMI, NOC collection, document management, and maintenance task priorities.",
    "keywords": [
        "task", "pending", "completed", "late", "given by", "department", 
        "users", "report", "summary", "checklist system", "task db", 
        "employee", "delegation", "performance", "attendance", "routine",
        "ticket", "booking", "travel", "bill", "ticket amount", "charges",
        "leave", "leave request", "hr approval", "approved", "absent",
        "plant visitor", "visit", "visitor", "visitor approval",
        "request", "travel request", "departure", "city",
        "resume", "candidate", "hiring", "interview", "joined", "designation",
        "subscription", "renewal", "subscriber", "company subscription", "approval history",
        "payment", "payment history", "UPI", "bank transfer", "transaction",
        "loan", "EMI", "bank", "loan amount", "foreclosure", "NOC", "closure",
        "document", "certificate", "document type", "category", "shared document",
        "payment fms", "pay to", "fms", "payment type",
        "master", "maintenance", "priority", "doer", "task type"
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
    ],
    "master": [
        "id",
        "doer_name",
        "department1",
        "given_by",
        "task_status",
        "task_type",
        "priority",
        "created_at",
        "department"
    ],
    "all_loans": [
        "id",
        "loan_name",
        "bank_name",
        "amount",
        "emi",
        "loan_start_date",
        "loan_end_date",
        "provided_document_name",
        "upload_document",
        "remarks",
        "created_at"
    ],
    "request_forclosure": [
        "id",
        "serial_no",
        "loan_name",
        "bank_name",
        "amount",
        "emi",
        "loan_start_date",
        "loan_end_date",
        "request_date",
        "requester_name",
        "created_at"
    ],
    "collect_noc": [
        "id",
        "serial_no",
        "loan_name",
        "bank_name",
        "loan_start_date",
        "loan_end_date",
        "closure_request_date",
        "collect_noc",
        "created_at"
    ],
    "subscription": [
        "id",
        "timestamp",
        "subscription_no",
        "company_name",
        "subscriber_name",
        "subscription_name",
        "price",
        "frequency",
        "purpose",
        "planned_1",
        "actual_1",
        "time_delay_1",
        "renewal_status",
        "renewal_count",
        "planned_2",
        "actual_2",
        "time_delay_2",
        "approval_status",
        "planned_3",
        "actual_3",
        "time_delay_3",
        "start_date",
        "end_date",
        "document_copy",
        "updated_price",
        "created_at",
        "updated_at",
        "planned2_days",
        "planned3_days",
        "planned1_days",
        "reason_for_renewal"
    ],
    "approval_history": [
        "id",
        "approval_no",
        "subscription_no",
        "approval_status",
        "note",
        "approved_by",
        "requested_on",
        "timestamp"
    ],
    "payment_history": [
        "id",
        "subscription_no",
        "payment_mode",
        "transaction_id",
        "start_date",
        "insurance_document",
        "timestamp"
    ],
    "subscription_renewals": [
        "id",
        "renewal_no",
        "subscription_no",
        "renewal_status",
        "approved_by",
        "price",
        "timestamp"
    ],
    "documents": [
        "document_id",
        "created_at",
        "serial_no",
        "document_name",
        "document_type",
        "category",
        "company_department",
        "tags",
        "person_name",
        "need_renewal",
        "renewal_date",
        "image",
        "email",
        "mobile",
        "is_deleted"
    ],
    "sharedocuments": [
        "id",
        "timestamp",
        "email",
        "name",
        "document_name",
        "document_type",
        "category",
        "serial_no",
        "image",
        "source_sheet",
        "share_method",
        "number"
    ],
    "payment_fms": [
        "id",
        "unique_no",
        "fms_name",
        "pay_to",
        "amount",
        "remarks",
        "attachment",
        "created_at",
        "planned1",
        "actual1",
        "status",
        "stage_remarks",
        "planned2",
        "actual2",
        "payment_type",
        "planned3",
        "actual3",
        "delay1",
        "delay2",
        "delay3"
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

--- FINANCE, SUBSCRIPTION & DOCUMENT MANAGEMENT TABLES ---

9. **TABLE: `master`** (Maintenance Task Master)
   - **Working:** Master data for maintenance task assignments with doer, department, priority.
   - **ALL COLUMNS ALLOWED:**
     * `id` (BIGINT): Unique identifier.
     * `doer_name` (TEXT): Person assigned to do the task.
     * `department1` (TEXT): Doer's own department.
     * `given_by` (TEXT): Person who assigned the task.
     * `task_status` (TEXT): Task status. Values: 'In House'. Use LOWER().
     * `task_type` (TEXT): Type of task. Values: 'Maintence'. Use LOWER().
     * `priority` (TEXT): Priority level.
         - Values: 'High', 'Low', 'Urgent'. Use LOWER() for comparisons.
     * `created_at` (TIMESTAMP): Record creation timestamp.
     * `department` (TEXT): Target department.
         - 14 values: 'ALL ELECTRICAL', 'CCM', 'CCM MAINTENANCE', 'LAB AND QUALITY CONTROL', 'PIPE MILL ELECTRICAL', 'PIPE MILL MAINTENANCE', 'PIPE MILL PRODUCTION', 'SMS ELECTRICAL', 'SMS MAINTENANCE', 'STORE', 'STRIP MILL ELECTRICAL', 'STRIP MILL MAINTENANCE', 'STRIP MILL PRODUCTION', 'TRANSPORT'. Use LOWER().
   - **❌ FORBIDDEN COLUMNS:** None (All columns are allowed).

10. **TABLE: `all_loans`** (Loan Master)
    - **Working:** Master list of company loans with principal, EMI, dates, and documents.
    - **ALL COLUMNS ALLOWED:**
      * `id` (BIGINT): Loan record ID.
      * `loan_name` (VARCHAR(255)): Loan name/type.
      * `bank_name` (VARCHAR(255)): Bank providing the loan.
      * `amount` (NUMERIC(15,2)): Loan principal amount.
      * `emi` (NUMERIC(12,2)): Monthly EMI amount.
      * `loan_start_date` (DATE): Loan start date.
      * `loan_end_date` (DATE): Loan end/maturity date.
      * `provided_document_name` (VARCHAR(255)): Document name.
      * `upload_document` (TEXT): Document URL.
      * `remarks` (TEXT): Remarks.
      * `created_at` (TIMESTAMP): Record creation timestamp.
    - **❌ FORBIDDEN COLUMNS:** None.
    - **LOGIC:**
      * Active loans: loan_end_date >= CURRENT_DATE
      * Expired loans: loan_end_date < CURRENT_DATE
      * Total exposure: SUM(amount). Total EMI burden: SUM(emi).

11. **TABLE: `request_forclosure`** (Loan Foreclosure Requests)
    - **Working:** Tracks requests to foreclose/close loans early.
    - **ALL COLUMNS ALLOWED:**
      * `id` (BIGINT): Foreclosure request ID.
      * `serial_no` (VARCHAR(50)): Business serial number.
      * `loan_name` (VARCHAR(255)): Loan name.
      * `bank_name` (VARCHAR(255)): Bank name.
      * `amount` (NUMERIC(15,2)): Outstanding amount.
      * `emi` (NUMERIC(12,2)): EMI amount.
      * `loan_start_date` (DATE): Loan start date.
      * `loan_end_date` (DATE): Loan end date.
      * `request_date` (DATE): Foreclosure request date.
      * `requester_name` (VARCHAR(255)): Requester name.
      * `created_at` (TIMESTAMP): Record creation timestamp.
    - **❌ FORBIDDEN COLUMNS:** None.

12. **TABLE: `collect_noc`** (NOC Collection Tracking)
    - **Working:** Tracks NOC collection status after loan closure.
    - **ALL COLUMNS ALLOWED:**
      * `id` (BIGINT): NOC tracking ID.
      * `serial_no` (VARCHAR(50)): Serial reference.
      * `loan_name` (VARCHAR(255)): Loan name.
      * `bank_name` (VARCHAR(255)): Bank name.
      * `loan_start_date` (DATE): Loan start date.
      * `loan_end_date` (DATE): Loan end date.
      * `closure_request_date` (DATE): Date closure/NOC requested.
      * `collect_noc` (BOOLEAN): Whether NOC collected (true/false).
      * `created_at` (TIMESTAMP): Record creation timestamp.
    - **❌ FORBIDDEN COLUMNS:** None.
    - **LOGIC:**
      * NOC Collected: collect_noc = true
      * NOC Pending: collect_noc = false OR collect_noc IS NULL

13. **TABLE: `subscription`** (Subscription Management)
    - **Working:** Company subscriptions/services with multi-stage approval workflow.
    - **ALL COLUMNS ALLOWED:**
      * `id` (INTEGER): Subscription row ID.
      * `timestamp` (TIMESTAMP): Submission timestamp.
      * `subscription_no` (VARCHAR(50)): Business key (SUB-xxxx).
      * `company_name` (VARCHAR(255)): Company name.
          - Values: 'Acme Corp', 'Alankar Alloys', 'Pankaj Ispat', 'Sourabh Rolling Mills' (case variants exist). Use LOWER().
      * `subscriber_name` (VARCHAR(255)): Internal subscriber/contact.
      * `subscription_name` (VARCHAR(255)): Subscription/service name.
      * `price` (NUMERIC(12,2)): Subscription price.
      * `frequency` (VARCHAR(50)): Billing frequency.
          - Values: 'Annually', 'Monthly', 'Quarterly', 'Yearly'. Use LOWER().
      * `purpose` (TEXT): Purpose/description.
      * `planned_1` (DATE): Stage 1 planned date.
      * `actual_1` (DATE): Stage 1 actual date.
      * `time_delay_1` (INTERVAL): Stage 1 delay.
      * `renewal_status` (VARCHAR(50)): Renewal status. Values: 'Approved'. Use LOWER().
      * `renewal_count` (INTEGER): Number of renewals.
      * `planned_2` (DATE): Stage 2 planned date.
      * `actual_2` (DATE): Stage 2 actual date.
      * `time_delay_2` (INTERVAL): Stage 2 delay.
      * `approval_status` (VARCHAR(50)): Values: 'Approved', 'Rejected'. Use LOWER().
      * `planned_3` (DATE): Stage 3 planned date.
      * `actual_3` (DATE): Stage 3 actual date.
      * `time_delay_3` (INTERVAL): Stage 3 delay.
      * `start_date` (DATE): Subscription start date.
      * `end_date` (DATE): Subscription end/expiry date.
      * `document_copy` (TEXT): Contract/invoice URL.
      * `updated_price` (NUMERIC(12,2)): Revised price after renewal.
      * `created_at` (TIMESTAMP): Created timestamp.
      * `updated_at` (TIMESTAMP): Updated timestamp.
      * `planned2_days` (INTEGER): SLA days for stage 2.
      * `planned3_days` (INTEGER): SLA days for stage 3.
      * `planned1_days` (INTEGER): SLA days for stage 1.
      * `reason_for_renewal` (VARCHAR): Reason for renewal.
    - **❌ FORBIDDEN COLUMNS:** None.
    - **LOGIC:**
      * Active: end_date >= CURRENT_DATE. Expired: end_date < CURRENT_DATE.
      * Approved: LOWER(approval_status) = 'approved'. Rejected: LOWER(approval_status) = 'rejected'.
      * JOIN KEY: subscription_no links to approval_history, payment_history, subscription_renewals.

14. **TABLE: `approval_history`** (Subscription Approval Audit)
    - **Working:** Audit trail for subscription approvals/rejections.
    - **ALL COLUMNS ALLOWED:**
      * `id` (INTEGER): Row ID.
      * `approval_no` (VARCHAR(50)): Approval number (APG-xxxx).
      * `subscription_no` (VARCHAR(50)): Links to subscription.subscription_no.
      * `approval_status` (VARCHAR(50)): 'Approved' or 'Rejected'. Use LOWER().
      * `note` (TEXT): Approver note.
      * `approved_by` (VARCHAR(255)): Approver name (e.g. 'Admin').
      * `requested_on` (TIMESTAMP): When requested.
      * `timestamp` (TIMESTAMP): When recorded.
    - **❌ FORBIDDEN COLUMNS:** None.

15. **TABLE: `payment_history`** (Subscription Payment Records)
    - **Working:** Payments made against subscriptions.
    - **ALL COLUMNS ALLOWED:**
      * `id` (INTEGER): Payment row ID.
      * `subscription_no` (VARCHAR(50)): Links to subscription.subscription_no.
      * `payment_mode` (VARCHAR(50)): 'Bank Transfer', 'Credit Card', 'UPI'. Use LOWER().
      * `transaction_id` (VARCHAR(255)): Transaction reference ID.
      * `start_date` (DATE): Payment effective date.
      * `insurance_document` (TEXT): Proof/document URL.
      * `timestamp` (TIMESTAMP): Payment timestamp.
    - **❌ FORBIDDEN COLUMNS:** None.

16. **TABLE: `subscription_renewals`** (Subscription Renewal Events)
    - **Working:** Renewal events with approver and price.
    - **ALL COLUMNS ALLOWED:**
      * `id` (INTEGER): Renewal row ID.
      * `renewal_no` (VARCHAR(50)): Renewal number (REN-xxxx).
      * `subscription_no` (VARCHAR(50)): Links to subscription.subscription_no.
      * `renewal_status` (VARCHAR(50)): 'Approved' or 'Renewed'. Use LOWER().
      * `approved_by` (VARCHAR(255)): Approver name.
      * `price` (NUMERIC(12,2)): Renewal price.
      * `timestamp` (TIMESTAMP): Renewal timestamp.
    - **❌ FORBIDDEN COLUMNS:** None.

17. **TABLE: `documents`** (Document Repository)
    - **Working:** Company/personal document management with renewal tracking.
    - **ALL COLUMNS ALLOWED:**
      * `document_id` (BIGINT): Document record ID.
      * `created_at` (TIMESTAMP): When added.
      * `serial_no` (BIGINT): Internal serial number.
      * `document_name` (TEXT): Document title.
      * `document_type` (TEXT): 'Certificate', 'Other', 'Report'. Use LOWER().
      * `category` (TEXT): 'Company' or 'Personal'. Use LOWER().
      * `company_department` (TEXT): Owning department.
      * `tags` (ARRAY): Array of tags. Use 'value' = ANY(tags) for filtering.
      * `person_name` (TEXT): Associated person/entity.
      * `need_renewal` (VARCHAR(3)): 'yes' or 'no'. Use LOWER().
      * `renewal_date` (DATE): Renewal/expiry date.
      * `image` (TEXT): Document file URL.
      * `email` (TEXT): Associated email.
      * `mobile` (VARCHAR(15)): Associated mobile.
      * `is_deleted` (BOOLEAN): Soft delete flag.
    - **❌ FORBIDDEN COLUMNS:** None.
    - **LOGIC:**
      * Active: is_deleted = false OR is_deleted IS NULL
      * Needs renewal: LOWER(need_renewal) = 'yes' AND renewal_date IS NOT NULL
      * Expired: renewal_date < CURRENT_DATE AND LOWER(need_renewal) = 'yes'

18. **TABLE: `sharedocuments`** (Document Sharing Log)
    - **Working:** Outbound document sharing audit log.
    - **ALL COLUMNS ALLOWED:**
      * `id` (BIGINT): Share event ID.
      * `timestamp` (TIMESTAMP): When shared.
      * `email` (VARCHAR(255)): Recipient email.
      * `name` (VARCHAR(255)): Recipient name.
      * `document_name` (VARCHAR(255)): Document name shared.
      * `document_type` (VARCHAR(100)): Document type.
      * `category` (VARCHAR(100)): Category.
      * `serial_no` (VARCHAR(100)): Document serial reference.
      * `image` (TEXT): Document link.
      * `source_sheet` (VARCHAR(255)): Origin system label.
      * `share_method` (VARCHAR(100)): Method (email/whatsapp).
      * `number` (BIGINT): Recipient phone.
    - **❌ FORBIDDEN COLUMNS:** None.

19. **TABLE: `payment_fms`** (Payment FMS / Finance Processing)
    - **Working:** Finance payment request/approval tracker with 3-stage workflow.
    - **ALL COLUMNS ALLOWED:**
      * `id` (UUID): Payment request ID. ⚠️ UUID type, NOT integer.
      * `unique_no` (TEXT): Business reference number.
      * `fms_name` (TEXT): Module/process name.
      * `pay_to` (TEXT): Payee name.
      * `amount` (NUMERIC(12,2)): Amount to pay.
      * `remarks` (TEXT): Remarks.
      * `attachment` (TEXT): Attachment URL.
      * `created_at` (TIMESTAMP): Created timestamp.
      * `planned1` (DATE): Stage 1 planned date.
      * `actual1` (DATE): Stage 1 actual date.
      * `status` (TEXT): Current payment status.
      * `stage_remarks` (TEXT): Stage remarks.
      * `planned2` (DATE): Stage 2 planned date.
      * `actual2` (DATE): Stage 2 actual date.
      * `payment_type` (TEXT): Payment type/category.
      * `planned3` (DATE): Stage 3 planned date.
      * `actual3` (DATE): Stage 3 actual date.
      * `delay1` (INTERVAL): Stage 1 delay.
      * `delay2` (INTERVAL): Stage 2 delay.
      * `delay3` (INTERVAL): Stage 3 delay.
    - **❌ FORBIDDEN COLUMNS:** None.
    - **LOGIC:**
      * Use LOWER(pay_to), LOWER(status), LOWER(payment_type) for filtering.
      * Total payments: SUM(amount). ⚠️ id is UUID - do NOT cast to integer.

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
   - **For subscription:** Use `start_date` and `end_date` for date range.
   - **For all_loans/request_forclosure/collect_noc:** Use `loan_start_date` and `loan_end_date`.

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

6. **SUBSCRIPTION & FINANCE STATES:**
   - **Subscription Approved:** `LOWER(approval_status) = 'approved'` in subscription
   - **Subscription Rejected:** `LOWER(approval_status) = 'rejected'` in subscription
   - **Active Subscription:** `end_date >= CURRENT_DATE` in subscription
   - **Expired Subscription:** `end_date < CURRENT_DATE` in subscription
   - **Renewal Approved:** `LOWER(renewal_status) = 'approved'` in subscription_renewals
   - **Renewed:** `LOWER(renewal_status) = 'renewed'` in subscription_renewals
   - **Active Loan:** `loan_end_date >= CURRENT_DATE` in all_loans
   - **NOC Collected:** `collect_noc = true` in collect_noc
   - **NOC Pending:** `collect_noc = false OR collect_noc IS NULL` in collect_noc
   - **Document Active:** `is_deleted = false OR is_deleted IS NULL` in documents
   - **Document Needs Renewal:** `LOWER(need_renewal) = 'yes'` in documents

7. **SUBSCRIPTION JOIN RULES:**
   - subscription.subscription_no = approval_history.subscription_no
   - subscription.subscription_no = payment_history.subscription_no
   - subscription.subscription_no = subscription_renewals.subscription_no
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
