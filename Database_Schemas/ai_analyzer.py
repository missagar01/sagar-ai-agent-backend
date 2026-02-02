"""
AI Schema Analyzer
==================
Shared utility to analyze database schemas using LLM (GPT).
It takes a Markdown schema report and outputs a rich semantic analysis in JSON.
"""

import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# Load env from Root (assuming this script is in Database_Schemas/)
# We'll use a relative path trick or assume caller loads it.
# Better to load it here safely.
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir) # Go up to DB_Assistant
env_path = os.path.join(root_dir, ".env")
load_dotenv(env_path)

SYSTEM_PROMPT = """
You are a Senior Database Architect & Business Analyst.
Your goal is to "reverse engineer" the business logic and semantic meaning of a database schema.

INPUT:
A raw technical schema (Tables, Columns, Sample Data).

TASK:
Analyze the schema and output a detailed JSON object containing:
1. "business_summary": A high-level description of what this database is for.
2. "table_insights": A dictionary where keys are table names, containing:
   - "description": What this table represents (e.g., "Stores daily employee tasks").
   - "primary_keys": inferred PKs.
   - "foreign_keys": inferred relationships (e.g., "Links to users table via user_id").
   - "important_columns": A list of columns that seem critical for analytics (dates, status, amounts).
   - "column_descriptions": A dictionary mapping column names to inferred meanings (e.g. "submission_date" -> "When the task was completed").
3. "suggested_semantic_schema": A text block representing how you would document this for a Text-to-SQL agent.

OUTPUT FORMAT:
Return ONLY valid JSON.
"""

def analyze_schema(schema_text: str):
    """
    Sends the schema report to the LLM and returns the JSON analysis.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    model_name = os.getenv("MODEL_NAME", "gpt-4o") # Fallback if empty in env
    
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in .env")
        return None

    print(f"🧠 Analyzing Schema with AI ({model_name})... This may take a minute.")
    
    llm = ChatOpenAI(
        model=model_name,
        temperature=0,
        openai_api_key=api_key,
        model_kwargs={"response_format": {"type": "json_object"}}
    )
    
    try:
        response = llm.invoke([
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=f"Here is the database schema report:\n\n{schema_text}")
        ])
        
        # Parse JSON
        analysis = json.loads(response.content)
        return analysis
        
    except Exception as e:
        print(f"❌ AI Analysis Failed: {e}")
        return None
