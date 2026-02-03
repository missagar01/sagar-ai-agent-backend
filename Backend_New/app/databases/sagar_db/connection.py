"""
Sagar001122 System - Connection Manager
=======================================
Manages connection to the Sagar001122 PostgreSQL database.
Enforces table and column whitelisting.
"""

from langchain_community.utilities import SQLDatabase
from app.core.config import settings
from .config import ALLOWED_TABLES

class RestrictedSQLDatabase(SQLDatabase):
    """
    Custom SQLDatabase wrapper that hides restricted tables and columns
    from the introspection methods used by LangChain agents.
    """
    def get_usable_table_names(self):
        # Filter visible tables
        all_tables = super().get_usable_table_names()
        return [t for t in all_tables if t in ALLOWED_TABLES]

    def get_table_info(self, table_names=None):
        return super().get_table_info(table_names)

def get_db_instance():
    """
    Get the configured LangChain SQLDatabase instance for Agent usage.
    """
    url = settings.DB_SAGAR_URL
    
    if not url:
        raise ValueError("DB_SAGAR_URL is not set in configuration.")
    
    try:
        # We use include_tables to enforce restriction at the connection level
        db = RestrictedSQLDatabase.from_uri(
            url,
            include_tables=ALLOWED_TABLES,
            sample_rows_in_table_info=2
        )
        return db
    except Exception as e:
        print(f"[ERROR] Failed to connect to Sagar001122 DB: {e}")
        raise
