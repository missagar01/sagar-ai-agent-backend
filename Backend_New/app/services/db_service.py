"""
Database Service
===============
Direct query execution and metadata loading for LLM-guided SQL generation
"""

from typing import List, Dict, Any, Optional
import psycopg2
from psycopg2.extras import RealDictCursor
import json
import os
from pathlib import Path
from app.core.config import settings
from app.core.column_restrictions import ALLOWED_COLUMNS, filter_schema_columns


# ============================================================================
# METADATA LOADING
# ============================================================================

_metadata_cache: Optional[Dict[str, Any]] = None

def load_metadata() -> Dict[str, Any]:
    """
    Load metadata.json with table schemas, column statistics, and business rules
    
    Returns:
        Dictionary with database metadata
    """
    global _metadata_cache
    
    if _metadata_cache is not None:
        return _metadata_cache
    
    # Find metadata.json (should be in Backend_New root)
    metadata_path = Path(__file__).parent.parent.parent / "metadata.json"
    
    if not metadata_path.exists():
        print(f"[WARNING] metadata.json not found at {metadata_path}")
        return {"tables": {}, "database": {}}
    
    try:
        with open(metadata_path, 'r', encoding='utf-8') as f:
            _metadata_cache = json.load(f)
        print(f"[SUCCESS] Loaded metadata from {metadata_path}")
        return _metadata_cache
    except Exception as e:
        print(f"[ERROR] Failed to load metadata: {e}")
        return {"tables": {}, "database": {}}


def get_table_metadata(table_name: str) -> Dict[str, Any]:
    """
    Get metadata for a specific table
    
    Args:
        table_name: Name of table (checklist, delegation, users, ticket_book, leave_request, plant_visitor, request, resume_request)
        
    Returns:
        Table metadata dictionary
    """
    metadata = load_metadata()
    return metadata.get("tables", {}).get(table_name, {})


def get_column_description(table_name: str, column_name: str) -> str:
    """
    Get business description for a column
    
    Args:
        table_name: Table name
        column_name: Column name
        
    Returns:
        Column description or empty string
    """
    table_meta = get_table_metadata(table_name)
    columns = table_meta.get("columns", {})
    col_info = columns.get(column_name, {})
    return col_info.get("description", "")


def get_column_restrictions_summary() -> str:
    """
    Get formatted summary of column restrictions for LLM prompts
    
    Returns:
        Formatted string with allowed columns per table
    """
    metadata = load_metadata()
    restrictions = metadata.get("database", {}).get("column_restrictions", {})
    
    # Build restrictions summary dynamically for all known tables
    table_icons = {
        "checklist": "📋",
        "delegation": "📌",
        "users": "👤",
        "ticket_book": "🎫",
        "leave_request": "🏖️",
        "plant_visitor": "🏭",
        "request": "✈️",
        "resume_request": "📄"
    }
    
    lines = []
    for table_name, icon in table_icons.items():
        cols = restrictions.get(table_name, "")
        if cols:
            lines.append(f"{icon} {table_name.upper()}: {cols}")
    
    forbidden = restrictions.get("forbidden_global", "")
    if forbidden:
        lines.append(f"\n❌ FORBIDDEN (DO NOT USE): {forbidden}")
    
    return "\n".join(lines) if lines else "No column restrictions found in metadata."


# ============================================================================
# QUERY EXECUTION
# ============================================================================

def execute_query(sql: str) -> List[Dict[str, Any]]:
    """
    Execute SELECT query and return results as list of dicts
    
    Args:
        sql: SQL SELECT query
        
    Returns:
        List of row dictionaries
    """
    conn = None
    try:
        # Connect to database
        conn = psycopg2.connect(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            database=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD
        )
        
        # Use RealDictCursor to get results as dictionaries
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()
            
            # Convert RealDictRow to regular dict
            return [dict(row) for row in results]
            
    except Exception as e:
        print(f"[DB ERROR] Query execution failed: {e}")
        raise
    finally:
        if conn:
            conn.close()


def get_table_row_count(table_name: str) -> int:
    """
    Get row count for a table
    
    Args:
        table_name: Table name
        
    Returns:
        Number of rows
    """
    try:
        results = execute_query(f"SELECT COUNT(*) as count FROM {table_name}")
        return results[0]['count'] if results else 0
    except Exception as e:
        print(f"[ERROR] Failed to get row count for {table_name}: {e}")
        return 0
