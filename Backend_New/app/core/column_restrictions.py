"""
Column Restrictions Configuration
==================================
Defines which columns are allowed for each table based on client requirements.
"""

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
