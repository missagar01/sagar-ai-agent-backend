"""
Sagar001122 Database Configuration
==================================
Defines the schema, allowed tables, and column restrictions for the Sagar001122 system.
RESTRICTED to specific tables and columns as per user requirements.
"""

# 1. Table & Column Restrictions
ALLOWED_TABLES = ["maintenance_task_assign"]

# Router Metadata (Used for Auto-Discovery)
ROUTER_METADATA = {
    "name": "sagar_db",
    "description": "A specialized Maintenance & Facility Management System designed to track machine repairs and operational tasks. It records 'who' (Doer_Name) performed maintenance on 'what' (Machine_Name), 'when' it was scheduled (Task_Start_Date), and 'when' it was actually completed (Actual_Date). Use this database for questions regarding machine uptime, pending repairs, technician performance (Doers), and maintenance schedules. It is strictly focused on physical machine/facility maintenance.",
    "keywords": [
        "maintenance", "machine", "repair", "task", "assign", "doer", 
        "start date", "actual date", "completion", "pending", "status", "sagar",
        "technician", "breakdown", "schedule", "facility"
    ]
}

COLUMNS_RESTRICTION = {
    "maintenance_task_assign": [
        "Machine_Name", 
        "Doer_Name", 
        "Task_Start_Date", 
        "Actual_Date"
    ]
}

# 2. Schema Definition for LLM Context
# (We only include the allowed columns to save tokens and focus the LLM)
DB_SCHEMA = """
Table: maintenance_task_assign
Columns:
- "Machine_Name" (TEXT): Name/Identifier of the machine being maintained.
- "Doer_Name" (TEXT): Person responsible for the task.
- "Task_Start_Date" (DATE/TIMESTAMP): Scheduled start date for the maintenance.
- "Actual_Date" (DATE/TIMESTAMP): Actual date when the task was completed.
  (NOTE: If "Actual_Date" is NULL, the task is considered PENDING/OPEN).
"""
