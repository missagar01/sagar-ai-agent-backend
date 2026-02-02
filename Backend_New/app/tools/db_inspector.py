"""
Database Schema Inspector
=========================
A reusable utility to inspect any PostgreSQL database and generate
a rich Markdown report for LLM Context.

Usage:
    from app.tools.db_inspector import inspect_database
    report = inspect_database("postgresql://user:pass@host/db")
    print(report)
"""

from sqlalchemy import create_engine, inspect, text
import json
from datetime import datetime

def inspect_database(connection_url: str) -> str:
    """
    Connects to the database and produces a detailed markdown schema report.
    Includes: Tables, Columns, Data Types, and 3 Sample Rows per table.
    """
    try:
        engine = create_engine(connection_url)
        inspector = inspect(engine)
        
        report = []
        report.append(f"# 🗄️ Database Schema Report")
        report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        report.append(f"**Source:** {connection_url.split('@')[-1]}") # Hide password in output
        report.append("\n---\n")
        
        table_names = inspector.get_table_names()
        
        if not table_names:
            return "⚠️ No tables found in the public schema."

        for table in table_names:
            report.append(f"## 📋 Table: `{table}`")
            
            # 1. Column Details
            columns = inspector.get_columns(table)
            report.append(f"### Columns:")
            report.append("| Name | Type | Nullable | Description |")
            report.append("| :--- | :--- | :--- | :--- |")
            
            for col in columns:
                col_name = col['name']
                col_type = str(col['type'])
                nullable = "✅" if col['nullable'] else "❌"
                # Try to get comment if exists (Postgres)
                report.append(f"| **{col_name}** | `{col_type}` | {nullable} | |")
            
            report.append("\n")
            
            # 2. Sample Data
            report.append(f"### 🔍 Sample Data (First 3 Rows):")
            try:
                with engine.connect() as conn:
                    # Safe query with limit
                    query = text(f"SELECT * FROM {table} LIMIT 3")
                    result = conn.execute(query)
                    rows = [dict(row._mapping) for row in result]
                    
                    if rows:
                        # Create generic markdown table for data
                        keys = rows[0].keys()
                        header = "| " + " | ".join(keys) + " |"
                        separator = "| " + " | ".join(["---"] * len(keys)) + " |"
                        report.append(header)
                        report.append(separator)
                        
                        for row in rows:
                            # Truncate long text for readability
                            vals = []
                            for v in row.values():
                                sv = str(v)
                                if len(sv) > 50: sv = sv[:47] + "..."
                                vals.append(sv.replace("\n", " "))
                            report.append("| " + " | ".join(vals) + " |")
                    else:
                        report.append("_No data found in table._")
                        
            except Exception as e:
                report.append(f"> ⚠️ Could not fetch sample data: {e}")
            
            report.append("\n---\n")
            
        return "\n".join(report)

    except Exception as e:
        return f"❌ Critical Error Inspecting DB: {e}"

if __name__ == "__main__":
    print("This is a module. Import 'inspect_database' to use it.")
