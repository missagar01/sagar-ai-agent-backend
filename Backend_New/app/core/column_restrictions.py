"""
Column Restrictions Configuration
==================================
Defines which columns are allowed for each table based on client requirements.
"""

# Allowed columns per table (client requirement)
# ⚠️ Keep in sync with app/databases/checklist/config.py ALLOWED_COLUMNS
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
