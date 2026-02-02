"""
Universal DB Schema Generator
=============================
A standalone tool to inspect databases and save their schemas as Markdown and Text files.

Usage:
    python schema_generator_tool.py <db_name> <connection_url>
    
    Example:
    python schema_generator_tool.py checklist postgresql://user:pass@host/checklist_db
"""

import sys
import os
import argparse
from datetime import datetime
from sqlalchemy import create_engine, inspect, text

def generate_schema_report(db_name, connection_url, output_dir):
    """Connects to DB and generates Markdown and Text reports"""
    
    print(f"🔌 Connecting to: {db_name}...")
    try:
        engine = create_engine(connection_url)
        inspector = inspect(engine)
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return

    table_names = inspector.get_table_names()
    if not table_names:
        print("⚠️ No tables found!")
        return

    # Prepare Content
    lines = []
    lines.append(f"# 🗄️ Schema Report: {db_name.upper()}")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("\n---\n")

    for table in table_names:
        lines.append(f"## 📋 Table: `{table}`")
        
        # Columns
        columns = inspector.get_columns(table)
        lines.append(f"### Columns:")
        lines.append("| Name | Type | Nullable |")
        lines.append("| :--- | :--- | :--- |")
        
        for col in columns:
            lines.append(f"| **{col['name']}** | `{col['type']}` | {col['nullable']} |")
        
        lines.append("\n")
        
        lines.append("\n")

        # -------------------------------------------------------------
        # 🏷️ CATEGORICAL ANALYSIS (Low Cardinality Columns)
        # -------------------------------------------------------------
        lines.append(f"### 🏷️ Categorical / Allowed Values:")
        
        has_categories = False
        with engine.connect() as conn:
            for col in columns:
                col_name = col['name']
                col_type = str(col['type']).lower()
                
                # Check Text, Varchar, Enum, or Boolean types
                if any(t in col_type for t in ['char', 'text', 'string', 'bool', 'enum']):
                    try:
                        # Check cardinality (number of unique values)
                        count_query = text(f"SELECT COUNT(DISTINCT \"{col_name}\") FROM \"{table}\"")
                        unique_count = conn.execute(count_query).scalar()
                        
                        # If low cardinality (<= 25), fetch distinct values
                        if unique_count and 0 < unique_count <= 25:
                            distinct_query = text(f"SELECT DISTINCT \"{col_name}\" FROM \"{table}\" ORDER BY 1 LIMIT 25")
                            values_result = conn.execute(distinct_query)
                            values = [str(row[0]) for row in values_result if row[0] is not None]
                            
                            # Clean up values (remove newlines, truncate)
                            clean_values = [v.replace('\n', ' ').strip() for v in values]
                            
                            lines.append(f"- **`{col_name}`** ({len(clean_values)} values): `{clean_values}`")
                            has_categories = True
                    except Exception as e:
                        # Ignore errors on complex types or if permission denied
                        pass
        
        if not has_categories:
            lines.append("_No categorical columns detected (all high cardinality or empty)_")
            
        lines.append("\n")
        
        # Sample Data
        lines.append(f"### 🔍 Sample Data (First 3 rows):")
        try:
            with engine.connect() as conn:
                query = text(f"SELECT * FROM \"{table}\" LIMIT 3")
                result = conn.execute(query)
                rows = [dict(row._mapping) for row in result]
                
                if rows:
                    keys = rows[0].keys()
                    # Markdown Table
                    header = "| " + " | ".join(keys) + " |"
                    sep = "| " + " | ".join(["---"] * len(keys)) + " |"
                    lines.append(header)
                    lines.append(sep)
                    for row in rows:
                        vals = [str(v).replace("\n", " ")[:50] for v in row.values()]
                        lines.append("| " + " | ".join(vals) + " |")
                else:
                    lines.append("_No data_")
        except Exception as e:
            lines.append(f"> Error fetching samples: {e}")
            
        lines.append("\n---\n")
    
    content = "\n".join(lines)
    
    # Save Files
    os.makedirs(output_dir, exist_ok=True)
    
    md_path = os.path.join(output_dir, "schema_report.md")
    txt_path = os.path.join(output_dir, "schema_report.txt")
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"✅ Reports Saved:")
    print(f"   - {md_path}")
    print(f"   - {txt_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate DB Schema Reports")
    parser.add_argument("name", help="Database Name (e.g., 'checklist')")
    parser.add_argument("url", help="Connection URL")
    
    args = parser.parse_args()
    
    # Define output folder based on name
    folder = os.path.join(os.getcwd(), "Database_Schemas", args.name)
    
    generate_schema_report(args.name, args.url, folder)
