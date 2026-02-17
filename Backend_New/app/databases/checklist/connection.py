"""
Checklist System - Connection Manager
=====================================
Manages connection to the Checklist/Delegation PostgreSQL database.
"""

from langchain_community.utilities import SQLDatabase
from app.core.config import settings
import os

class RestrictedSQLDatabase(SQLDatabase):
    """Database with table restrictions"""
    def get_usable_table_names(self):
        all_tables = super().get_usable_table_names()
        # Allowed tables: task management + admin/HR modules
        allowed = [
            "checklist", "delegation", "users",
            "ticket_book", "leave_request", "plant_visitor",
            "request", "resume_request"
        ] 
        return [t for t in all_tables if t.lower() in allowed]

def get_db_instance():
    """
    Get the configured LangChain SQLDatabase instance for Agent usage.
    """
    # Use the dedicated URL from settings
    url = settings.DB_CHECKLIST_URL
    
    try:
        db = RestrictedSQLDatabase.from_uri(url)
        return db
    except Exception as e:
        print(f"[ERROR] Failed to connect to Checklist DB: {e}")
        raise
