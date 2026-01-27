"""
Database Service
===============
Direct query execution for cached queries
"""

from typing import List, Dict, Any
import psycopg2
from psycopg2.extras import RealDictCursor
from app.core.config import settings


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
