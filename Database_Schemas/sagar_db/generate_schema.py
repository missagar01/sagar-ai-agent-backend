"""
Sagar001122 Schema Generator
============================
Run this script to regenerate the schema report for the Sagar001122 System.
It connects to the database and overwrites 'schema_report.md'.
"""
import sys
import os
from sqlalchemy import create_engine, inspect, text
from datetime import datetime

# CONFIGURATION
DB_NAME = "Sagar001122 System"
# Using the specific URL for this DB
DB_URL = "postgresql://postgres:Sagar00112233@database-2-mumbai.c1wm8i46kcmm.ap-south-1.rds.amazonaws.com/Sagar001122"

def generate():
    print(f"🔌 Connecting to: {DB_NAME}...")
    try:
        engine = create_engine(DB_URL)
        inspector = inspect(engine)
    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return

    table_names = inspector.get_table_names()
    if not table_names:
        print("⚠️ No tables found!")
        return

    lines = []
    lines.append(f"# 🗄️ Schema Report: {DB_NAME}")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("\n---\n")

    for table in table_names:
        lines.append(f"## 📋 Table: `{table}`")
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
                            clean_values = [v.replace('\n', ' ').strip() for v in values]
                            
                            lines.append(f"- **`{col_name}`** ({len(clean_values)} values): `{clean_values}`")
                            has_categories = True
                    except Exception as e:
                        pass
        
        if not has_categories:
            lines.append("_No categorical columns detected_")
            
        lines.append("\n")
        
        lines.append(f"### 🔍 Sample Data (First 3 rows):")
        try:
            with engine.connect() as conn:
                query = text(f"SELECT * FROM \"{table}\" LIMIT 3")
                result = conn.execute(query)
                rows = [dict(row._mapping) for row in result]
                if rows:
                    keys = rows[0].keys()
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
            lines.append(f"> Error: {e}")
        lines.append("\n---\n")
    
    # Save in SCRIPT directory (not CWD)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(script_dir, "schema_report.md")
    txt_path = os.path.join(script_dir, "schema_report.txt")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
        
    print(f"✅ Generated in {script_dir}:")
    print(f"   - schema_report.md")
    print(f"   - schema_report.txt")

    # ----------------------------------------------------
    # AI ANALYSIS STEP
    # ----------------------------------------------------
    try:
        # Import shared logic from parent folder
        parent_dir = os.path.dirname(script_dir)
        if parent_dir not in sys.path:
            sys.path.append(parent_dir)
            
        from ai_analyzer import analyze_schema
        
        # Read the report we just made
        with open(md_path, "r", encoding="utf-8") as f:
            full_report = f.read()
            
        # Run AI
        analysis = analyze_schema(full_report)
        
        if analysis:
            json_path = os.path.join(script_dir, "metadata_analysis.json")
            import json
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(analysis, f, indent=2)
            print(f"   - metadata_analysis.json (🧠 AI Output)")
            print("\n👉 You can now use 'metadata_analysis.json' to build your 'config.py'.")
            
    except ImportError:
        print("⚠️ Could not import 'ai_analyzer.py'. Make sure it exists in the parent directory.")
    except Exception as e:
        print(f"⚠️ AI Analysis skipped: {e}")

if __name__ == "__main__":
    generate()
