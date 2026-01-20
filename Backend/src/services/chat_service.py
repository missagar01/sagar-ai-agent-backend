"""
Chat Service - Main Orchestration with Caching & Cancellation
=============================================================
Complete flow with:
1. Query caching (90% semantic similarity)
2. Session management
3. Request cancellation support
4. Fixed date format handling

Flow:
1. Check cache for similar query (skip LLM if found)
2. Language Detection
3. Schema Fetching (with ENUMs, relationships, sample data)
4. Intent Analysis (determines tables and query type)
5. SQL Generation (comprehensive prompt)
6. 🔒 HARDCODED Security Validation
7. Query Execution (with cancellation support)
8. Answer Generation
9. Cache the result
"""

import os
import re
import json
import asyncio
from datetime import datetime
from typing import Any, Dict, List, Optional, TypedDict
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import LangChain/LangGraph components
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langgraph.graph import StateGraph, END

# Import our modules
from src.core.security import validate_sql_security, HardcodedSecurityValidator
from src.services.schema_service import SchemaService
from src.services.db_service import DatabaseService
from src.services.cache_service import query_cache
from src.services.session_service import session_service


# =============================================================================
# VERBOSE LOGGING CONFIGURATION
# =============================================================================
VERBOSE_MODE = os.getenv("VERBOSE_MODE", "true").lower() == "true"


def log_step(step_name: str, message: str, data: Any = None):
    """Log internal steps with timestamps."""
    if not VERBOSE_MODE:
        return
    
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"\n{'='*70}")
    print(f"⏱️  [{timestamp}] STEP: {step_name}")
    print(f"{'='*70}")
    print(f"📋 {message}")
    
    if data:
        if isinstance(data, str):
            if len(data) > 1500:
                print(f"\n{data[:1500]}...\n[TRUNCATED - {len(data)} chars total]")
            else:
                print(f"\n{data}")
        elif isinstance(data, (dict, list)):
            try:
                formatted = json.dumps(data, indent=2, default=str, ensure_ascii=False)
                if len(formatted) > 1500:
                    print(f"\n{formatted[:1500]}...\n[TRUNCATED]")
                else:
                    print(f"\n{formatted}")
            except:
                print(f"\n{str(data)[:1500]}")
        else:
            print(f"\n{str(data)[:1500]}")


def log_pipeline_start(question: str):
    """Log the start of a new pipeline execution."""
    if not VERBOSE_MODE:
        return
    
    print(f"\n{'🚀'*30}")
    print(f"🚀 STARTING PIPELINE FOR: '{question}'")
    print(f"{'🚀'*30}")


def log_pipeline_summary(state: Dict[str, Any]):
    """Log a summary at the end of pipeline execution."""
    if not VERBOSE_MODE:
        return
    
    print(f"\n{'='*70}")
    print(f"📊 PIPELINE SUMMARY")
    print(f"{'='*70}")
    print(f"❓ Question: {state.get('user_question', 'N/A')}")
    print(f"🌐 Language: {state.get('detected_language', 'N/A').upper()}")
    print(f"🎯 Cache Hit: {state.get('cache_hit', False)}")
    print(f"📝 Generated SQL: {state.get('generated_sql', 'N/A')}")
    
    query_result = state.get('query_result')
    if query_result:
        print(f"📊 Results: {len(query_result)} rows")
    
    print(f"🚫 Blocked: {state.get('is_blocked', False)}")
    
    if state.get('error'):
        print(f"❌ Error: {state.get('error')}")
    
    answer = state.get('final_answer', '')
    if answer:
        print(f"💬 Answer Preview: {answer[:300]}...")
    
    print(f"{'='*70}\n")


class ChatState(TypedDict):
    """State for the chat workflow."""
    user_question: str
    session_id: Optional[str]
    detected_language: str
    schema_context: str
    enum_context: str
    sample_data_context: str
    relationship_context: str
    intent_analysis: str
    generated_sql: str
    security_result: Dict[str, Any]
    query_result: Any
    final_answer: str
    error: Optional[str]
    is_blocked: bool
    cache_hit: bool
    cancelled: bool


class ChatService:
    """
    Main Chat Service with caching and cancellation support.
    """
    
    # Class-level cancellation tracking
    _active_requests: Dict[str, bool] = {}
    
    def __init__(self):
        log_step("🔧 INIT", "Initializing ChatService...")
        
        self.llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            temperature=0,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        self.schema_service = SchemaService()
        self.db_service = DatabaseService()
        self.security_validator = HardcodedSecurityValidator()
        
        # Hinglish indicators
        self.hinglish_words = [
            'kya', 'hai', 'hain', 'kitne', 'kitna', 'kitni', 'kaun', 'kon', 'kab',
            'kaise', 'kaha', 'kahaan', 'dikha', 'dikhao', 'batao', 'bata',
            'sabhi', 'sab', 'saare', 'koi', 'nahi', 'nahin', 'aur', 'ya', 'mein',
            'ko', 'ka', 'ki', 'ke', 'wala', 'wali', 'wale', 'ho', 'hoga',
            'tha', 'thi', 'the', 'kar', 'karo', 'raha', 'rahi', 'rahe',
            'pura', 'puri', 'jinka', 'jinki', 'jinke', 'unka', 'unki', 'unke'
        ]
        
        self.workflow = self._build_workflow()
        log_step("🔧 INIT ✅", "ChatService initialized successfully!")
    
    @staticmethod
    def set_verbose(enabled: bool):
        """Enable or disable verbose logging."""
        global VERBOSE_MODE
        VERBOSE_MODE = enabled
        print(f"🔊 Verbose mode: {'ON' if enabled else 'OFF'}")
    
    @staticmethod
    def is_verbose() -> bool:
        """Check if verbose mode is enabled."""
        return VERBOSE_MODE
    
    @classmethod
    def cancel_request(cls, request_id: str) -> bool:
        """
        Cancel an active request.
        
        Args:
            request_id: The request ID to cancel
            
        Returns:
            True if request was found and cancelled
        """
        if request_id in cls._active_requests:
            cls._active_requests[request_id] = True
            print(f"🛑 Request {request_id} marked for cancellation")
            return True
        return False
    
    @classmethod
    def is_cancelled(cls, request_id: str) -> bool:
        """Check if a request has been cancelled."""
        return cls._active_requests.get(request_id, False)
    
    @classmethod
    def register_request(cls, request_id: str):
        """Register a new request for cancellation tracking."""
        cls._active_requests[request_id] = False
    
    @classmethod
    def unregister_request(cls, request_id: str):
        """Unregister a completed request."""
        cls._active_requests.pop(request_id, None)
    
    def _build_workflow(self) -> StateGraph:
        """Build the LangGraph workflow."""
        workflow = StateGraph(ChatState)
        
        # Add nodes
        workflow.add_node("check_cache", self._check_cache)
        workflow.add_node("detect_language", self._detect_language)
        workflow.add_node("fetch_schema", self._fetch_schema)
        workflow.add_node("analyze_intent", self._analyze_intent)
        workflow.add_node("generate_sql", self._generate_sql)
        workflow.add_node("validate_security", self._validate_security)
        workflow.add_node("execute_query", self._execute_query)
        workflow.add_node("generate_answer", self._generate_answer)
        workflow.add_node("handle_blocked", self._handle_blocked)
        workflow.add_node("cache_result", self._cache_result)
        
        # Set entry point
        workflow.set_entry_point("check_cache")
        
        # Conditional after cache check
        workflow.add_conditional_edges(
            "check_cache",
            self._route_after_cache,
            {
                "cache_hit": "execute_query",
                "cache_miss": "detect_language"
            }
        )
        
        workflow.add_edge("detect_language", "fetch_schema")
        workflow.add_edge("fetch_schema", "analyze_intent")
        workflow.add_edge("analyze_intent", "generate_sql")
        workflow.add_edge("generate_sql", "validate_security")
        
        workflow.add_conditional_edges(
            "validate_security",
            self._route_after_security,
            {
                "blocked": "handle_blocked",
                "allowed": "execute_query"
            }
        )
        
        workflow.add_edge("execute_query", "generate_answer")
        workflow.add_edge("generate_answer", "cache_result")
        workflow.add_edge("cache_result", END)
        workflow.add_edge("handle_blocked", END)
        
        return workflow.compile()
    
    def _check_cache(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Check if a similar query exists in cache."""
        log_step("0️⃣ CACHE_CHECK", f"Checking cache for: '{state['user_question']}'")
        
        cached = query_cache.find_similar_query(state['user_question'])
        
        if cached:
            log_step("0️⃣ CACHE_CHECK ✅", f"Cache HIT! Similarity: {cached['similarity']:.2%}")
            return {
                "generated_sql": cached['sql'],
                "cache_hit": True,
                "detected_language": "english"  # Default, will be detected if needed
            }
        else:
            log_step("0️⃣ CACHE_CHECK ❌", "Cache miss - proceeding with full pipeline")
            return {"cache_hit": False}
    
    def _route_after_cache(self, state: Dict[str, Any]) -> str:
        """Route based on cache hit/miss."""
        return "cache_hit" if state.get("cache_hit") else "cache_miss"
    
    def _detect_language(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Detect if the question is in English or Hinglish."""
        log_step("1️⃣ LANGUAGE_DETECTOR", f"Detecting language for: '{state['user_question']}'")
        
        question = state["user_question"].lower()
        words_in_question = question.split()
        
        hinglish_count = sum(1 for word in words_in_question if word in self.hinglish_words)
        
        hinglish_patterns = [
            r'\bkitne\b', r'\bdikhao\b', r'\bbatao\b', r'\bsabhi\b',
            r'\bwale\b', r'\bwali\b', r'\bmein\b', r'\bko\b'
        ]
        pattern_matches = sum(1 for p in hinglish_patterns if re.search(p, question))
        
        if hinglish_count >= 2 or pattern_matches >= 2:
            detected = "hinglish"
        else:
            detected = "english"
        
        log_step("1️⃣ LANGUAGE_DETECTOR ✅", f"Detected language: {detected.upper()}")
        return {"detected_language": detected}
    
    def _fetch_schema(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Fetch comprehensive database schema context."""
        log_step("2️⃣ SCHEMA_FETCHER", "Fetching database schema, ENUMs, sample data, and relationships...")
        
        try:
            schema_context = self._get_detailed_schema()
            log_step("2️⃣ SCHEMA_FETCHER", "Schema fetched", schema_context[:500] + "...")
            
            enum_context = self._get_enum_context()
            log_step("2️⃣ SCHEMA_FETCHER", "ENUM values fetched", enum_context[:500] + "...")
            
            sample_data_context = self._get_sample_data_context()
            log_step("2️⃣ SCHEMA_FETCHER", "Sample data fetched", sample_data_context[:500] + "...")
            
            relationship_context = self._get_relationship_context()
            log_step("2️⃣ SCHEMA_FETCHER ✅", "All schema context fetched successfully!")
            
            return {
                "schema_context": schema_context,
                "enum_context": enum_context,
                "sample_data_context": sample_data_context,
                "relationship_context": relationship_context
            }
        except Exception as e:
            log_step("2️⃣ SCHEMA_FETCHER ❌", f"Error: {str(e)}")
            return {"error": f"Failed to fetch schema: {str(e)}"}
    
    def _get_detailed_schema(self) -> str:
        """Get detailed schema information."""
        query = """
        SELECT 
            table_name, 
            column_name, 
            data_type,
            is_nullable,
            column_default
        FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name IN ('checklist', 'delegation', 'users')
        ORDER BY table_name, ordinal_position;
        """
        
        try:
            rows = self.db_service.execute_select(query)
            
            schema_map = {}
            for row in rows:
                table = row['table_name']
                col_info = f"{row['column_name']} ({row['data_type']})"
                if row['is_nullable'] == 'NO':
                    col_info += " NOT NULL"
                schema_map.setdefault(table, []).append(col_info)
            
            schema_text = ""
            for table, cols in schema_map.items():
                schema_text += f"Table: public.{table}\nColumns:\n  - " + "\n  - ".join(cols) + "\n\n"
            
            return schema_text.strip()
        except Exception as e:
            return f"Schema fetch error: {str(e)}"
    
    def _get_enum_context(self) -> str:
        """Get ENUM types and their valid values."""
        enum_query = """
        SELECT 
            t.typname AS enum_name,
            e.enumlabel AS enum_value
        FROM pg_type t
        JOIN pg_enum e ON t.oid = e.enumtypid
        JOIN pg_catalog.pg_namespace n ON n.oid = t.typnamespace
        WHERE n.nspname = 'public'
        ORDER BY t.typname, e.enumsortorder;
        """
        
        mapping_query = """
        SELECT 
            c.table_name,
            c.column_name,
            c.udt_name as enum_type
        FROM information_schema.columns c
        WHERE c.table_schema = 'public'
          AND c.table_name IN ('checklist', 'delegation', 'users')
          AND c.data_type = 'USER-DEFINED'
        ORDER BY c.table_name, c.column_name;
        """
        
        try:
            enum_rows = self.db_service.execute_select(enum_query)
            enum_map = {}
            for row in enum_rows:
                enum_map.setdefault(row['enum_name'], []).append(row['enum_value'])
            
            enum_text = "=== All ENUM Types in Database ===\n"
            for enum_name, values in enum_map.items():
                enum_text += f"  {enum_name}: {', '.join(repr(v) for v in values)}\n"
            
            mapping_rows = self.db_service.execute_select(mapping_query)
            
            enum_text += "\n=== ⚠️ ACTUAL ENUM Column Mappings ===\n"
            enum_text += "CRITICAL: Use ONLY these exact values for each column:\n\n"
            
            for row in mapping_rows:
                enum_type = row['enum_type']
                values = enum_map.get(enum_type, [])
                enum_text += f"  {row['table_name']}.{row['column_name']} (ENUM type: {enum_type}):\n"
                enum_text += f"    Valid values: {', '.join(repr(v) for v in values)}\n\n"
            
            return enum_text.strip()
        except Exception as e:
            return f"ENUM fetch error: {str(e)}"
    
    def _get_sample_data_context(self) -> str:
        """Get sample values from key columns."""
        sample_queries = {
            "checklist.status": "SELECT DISTINCT status::text FROM public.checklist WHERE status IS NOT NULL LIMIT 10",
            "checklist.enable_reminder": "SELECT DISTINCT enable_reminder::text FROM public.checklist WHERE enable_reminder IS NOT NULL LIMIT 10",
            "checklist.department": "SELECT DISTINCT department FROM public.checklist WHERE department IS NOT NULL LIMIT 10",
            "checklist.frequency": "SELECT DISTINCT frequency FROM public.checklist WHERE frequency IS NOT NULL LIMIT 10",
            "checklist.name": "SELECT DISTINCT name FROM public.checklist WHERE name IS NOT NULL LIMIT 10",
            "checklist.planned_date": "SELECT DISTINCT planned_date FROM public.checklist WHERE planned_date IS NOT NULL LIMIT 5",
            "delegation.status": "SELECT DISTINCT status FROM public.delegation WHERE status IS NOT NULL LIMIT 10",
            "users.role": "SELECT DISTINCT role::text FROM public.users WHERE role IS NOT NULL LIMIT 10",
            "users.status": "SELECT DISTINCT status::text FROM public.users WHERE status IS NOT NULL LIMIT 10",
            "users.department": "SELECT DISTINCT department FROM public.users WHERE department IS NOT NULL LIMIT 10",
            "users.user_name": "SELECT DISTINCT user_name FROM public.users WHERE user_name IS NOT NULL LIMIT 10",
        }
        
        samples = {}
        for col_name, query in sample_queries.items():
            try:
                rows = self.db_service.execute_select(query)
                if rows:
                    first_col = list(rows[0].keys())[0]
                    values = [str(row[first_col]) for row in rows]
                    samples[col_name] = values
            except Exception:
                pass
        
        sample_text = "=== Actual Sample Values from Database ===\n"
        sample_text += "⚠️ Use these EXACT values in WHERE clauses:\n\n"
        for col, values in samples.items():
            sample_text += f"  {col}: {', '.join(repr(v) for v in values[:7])}\n"
        
        return sample_text.strip()
    
    def _get_relationship_context(self) -> str:
        """Get foreign key relationships between tables."""
        return """IMPLICIT RELATIONSHIPS (use for JOINs):
- users.user_name = checklist.name (user assigned to checklist task)
- users.user_name = delegation.name (user assigned to delegation task)
- users.department = checklist.department
- users.department = delegation.department"""
    
    def _analyze_intent(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze user intent."""
        log_step("3️⃣ INTENT_ANALYZER", f"Analyzing intent for: '{state['user_question']}'")
        
        if state.get("error"):
            log_step("3️⃣ INTENT_ANALYZER ⏭️", "Skipped due to previous error")
            return {}
        
        hinglish_context = ""
        if state.get("detected_language") == "hinglish":
            hinglish_context = """
NOTE: The user's question is in HINGLISH (Hindi + English mix).
Common Hinglish patterns:
- "dikhao" / "dikha do" = show
- "batao" = tell/show
- "kitne" / "kitna" = how many/much
- "sabhi" / "sab" = all
- "wale" = those who
- "complete nahi hua" = not completed
- "pending wale" = pending ones
"""
        
        prompt = f"""Analyze the user's question and determine:
1. Which tables are relevant (checklist, delegation, users)
2. Whether JOINs are needed
3. What type of aggregation/filtering is required

CRITICAL RULE: This is READ-ONLY. No modifications allowed.
{hinglish_context}

Available Tables:
{state['schema_context']}

{state['enum_context']}

{state['sample_data_context']}

User Question: {state['user_question']}

Respond in JSON format:
{{"tables": ["table1", "table2"], "needs_join": true/false, "query_type": "simple/aggregate/join", "notes": "brief analysis"}}
"""
        
        try:
            log_step("3️⃣ INTENT_ANALYZER", "Sending prompt to LLM...")
            resp = self.llm.invoke(prompt)
            intent = resp.content.strip()
            log_step("3️⃣ INTENT_ANALYZER ✅", "Intent analysis complete!", intent)
            return {"intent_analysis": intent}
        except Exception as e:
            log_step("3️⃣ INTENT_ANALYZER ❌", f"Error: {str(e)}")
            return {"intent_analysis": f'{{"error": "{str(e)}"}}'}
    
    def _generate_sql(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Generate SQL with comprehensive prompt."""
        log_step("4️⃣ SQL_GENERATOR", "Generating SQL query...")
        
        if state.get("error"):
            log_step("4️⃣ SQL_GENERATOR ⏭️", "Skipped due to previous error")
            return {}
        
        hinglish_sql_context = ""
        if state.get("detected_language") == "hinglish":
            hinglish_sql_context = """
=== HINGLISH QUERY TRANSLATION GUIDE ===
- "sabhi users dikhao" = SELECT * FROM users
- "kitne tasks hain" = SELECT COUNT(*) FROM checklist
- "pending wale tasks" = WHERE status = 'no'
- "complete ho gaye" = WHERE status = 'yes'
- "active users batao" = WHERE status = 'active'
- "top 5/10" = LIMIT 5/10
- "jinka task complete nahi hua" = WHERE status = 'no'
"""
        
        system_rules = f"""You are a PostgreSQL SQL generator for a READ-ONLY chatbot.
{hinglish_sql_context}

=== CRITICAL SAFETY RULES (NEVER BREAK) ===
1. ONLY generate SELECT queries
2. NEVER use: DELETE, UPDATE, TRUNCATE, DROP, INSERT, ALTER, CREATE, GRANT, REVOKE
3. If user asks to modify data, return: SELECT 'READ_ONLY_MODE: Cannot modify data' as message;

=== SCOPE RULES ===
- Use ONLY tables: public.checklist, public.delegation, public.users
- Use JOINs when needed between tables
- Always qualify columns with table names in JOINs

=== OUTPUT RULES ===
- Return ONLY ONE SQL query (single statement)
- No explanations, no markdown, no code blocks
- Use proper PostgreSQL syntax

=== ⚠️⚠️⚠️ SUPER CRITICAL: ENUM VALUES ⚠️⚠️⚠️ ===
For checklist.status:
  - ONLY valid values: 'yes', 'no'
  - 'yes' = task completed, 'no' = task not completed
  - DO NOT use 'done', 'completed', 'pending'

For users.status:
  - Valid values: 'active', 'inactive', 'on_leave', 'terminated'

For delegation.status:
  - This is TEXT, not ENUM - values like 'done', 'Done', 'extend'

=== ⚠️⚠️⚠️ SUPER CRITICAL: DATE HANDLING ⚠️⚠️⚠️ ===
⚠️ checklist.planned_date is TEXT in DD/MM/YYYY format (e.g., '28/11/2025')
⚠️ NEVER use ::timestamp directly on planned_date!
⚠️ Use TO_TIMESTAMP() with proper format:

CORRECT WAY to convert planned_date:
  TO_TIMESTAMP(checklist.planned_date, 'DD/MM/YYYY')

CORRECT comparison with NOW():
  TO_TIMESTAMP(checklist.planned_date, 'DD/MM/YYYY') < NOW()

WRONG (will cause error):
  checklist.planned_date::timestamp < NOW()  -- ERROR!
  checklist.planned_date < NOW()  -- ERROR!

For "not completed on time" queries:
  WHERE checklist.status = 'no' 
    AND TO_TIMESTAMP(checklist.planned_date, 'DD/MM/YYYY') < NOW()

Other date columns (these ARE proper timestamps):
- checklist.submission_date: TIMESTAMP
- checklist.task_start_date: TIMESTAMP  
- checklist.created_at: TIMESTAMP
- delegation.planned_date: TIMESTAMP (proper timestamp)
- delegation.submission_date: TIMESTAMP

=== JOIN LOGIC ===
- Link users to tasks: users.user_name = checklist.name
- Or by department: users.department = checklist.department

=== SEARCH / LIKE QUERIES ===
For name searches, use ILIKE for case-insensitive:
WHERE user_name ILIKE '%search_term%'
"""

        prompt = f"""{system_rules}

Database Schema:
{state['schema_context']}

{state['enum_context']}

{state['sample_data_context']}

{state.get('relationship_context', '')}

Intent Analysis:
{state.get('intent_analysis', 'Not available')}

User Question:
{state['user_question']}

⚠️⚠️⚠️ CRITICAL REMINDERS ⚠️⚠️⚠️
1. checklist.status uses 'yes'/'no' (NOT 'done'/'completed')
2. users.status uses 'active'/'inactive'/'on_leave'/'terminated'
3. checklist.planned_date is TEXT in DD/MM/YYYY format!
4. Use TO_TIMESTAMP(planned_date, 'DD/MM/YYYY') for date comparisons!
5. For "not completed on time": 
   WHERE status = 'no' AND TO_TIMESTAMP(planned_date, 'DD/MM/YYYY') < NOW()

Return ONLY the SQL statement:"""

        try:
            log_step("4️⃣ SQL_GENERATOR", "Sending prompt to LLM...")
            resp = self.llm.invoke(prompt)
            sql = resp.content.strip()
            
            # Clean the SQL
            sql = re.sub(r"```sql|```", "", sql).strip()
            sql = re.sub(r"--.*$", "", sql, flags=re.MULTILINE).strip()
            
            log_step("4️⃣ SQL_GENERATOR ✅", "SQL generated!", f"SQL:\n{sql}")
            return {"generated_sql": sql}
            
        except Exception as e:
            log_step("4️⃣ SQL_GENERATOR ❌", f"Error: {str(e)}")
            return {"error": f"Failed to generate SQL: {str(e)}"}
    
    def _validate_security(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """🔒 LAYER 3: HARDCODED SECURITY VALIDATION"""
        log_step("5️⃣ SECURITY_VALIDATOR", "Validating SQL for security...")
        
        if state.get("error"):
            log_step("5️⃣ SECURITY_VALIDATOR ⏭️", "Skipped due to previous error")
            return {"is_blocked": True}
        
        log_step("5️⃣ SECURITY_VALIDATOR", f"Checking SQL:\n{state['generated_sql']}")
        
        is_valid, error_message, sanitized_sql = validate_sql_security(state["generated_sql"])
        
        security_result = {
            "is_valid": is_valid,
            "error_message": error_message,
            "original_sql": state["generated_sql"],
            "sanitized_sql": sanitized_sql
        }
        
        if not is_valid:
            log_step("5️⃣ SECURITY_VALIDATOR ❌", f"BLOCKED! Reason: {error_message}")
            return {
                "security_result": security_result,
                "is_blocked": True,
                "error": error_message
            }
        else:
            log_step("5️⃣ SECURITY_VALIDATOR ✅", f"SQL passed security checks!\nSanitized SQL:\n{sanitized_sql}")
            return {
                "security_result": security_result,
                "generated_sql": sanitized_sql,
                "is_blocked": False
            }
    
    def _route_after_security(self, state: Dict[str, Any]) -> str:
        """Route based on security validation result."""
        if state.get("is_blocked"):
            return "blocked"
        return "allowed"
    
    def _execute_query(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the validated query."""
        log_step("6️⃣ DB_EXECUTOR", "Executing SQL query on database...")
        log_step("6️⃣ DB_EXECUTOR", f"SQL to execute:\n{state['generated_sql']}")
        
        try:
            result = self.db_service.execute_select(state["generated_sql"])
            row_count = len(result) if result else 0
            
            log_step("6️⃣ DB_EXECUTOR ✅", f"Query executed successfully! {row_count} rows returned")
            
            if result and row_count > 0:
                sample = result[:5]
                log_step("6️⃣ DB_EXECUTOR", f"Sample results (first {min(5, row_count)} rows):", sample)
            
            return {"query_result": result}
        except Exception as e:
            log_step("6️⃣ DB_EXECUTOR ❌", f"Query execution failed: {str(e)}")
            return {"error": f"Query execution failed: {str(e)}"}
    
    def _generate_answer(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Generate natural language answer from query results."""
        log_step("7️⃣ ANSWER_GENERATOR", "Generating natural language response...")
        
        if state.get("error"):
            log_step("7️⃣ ANSWER_GENERATOR", f"Returning error: {state['error']}")
            return {"final_answer": f"Error: {state['error']}"}
        
        if state.get("detected_language") == "hinglish":
            language_instruction = "Respond in Hinglish (Hindi-English mix). Use Hindi words naturally."
        else:
            language_instruction = "Respond in English"
        
        results = state.get("query_result", [])
        result_count = len(results) if results else 0
        
        # Show ALL results, not just 50
        display_results = results
        
        log_step("7️⃣ ANSWER_GENERATOR", f"Processing {result_count} results for answer generation...")
        
        answer_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful database assistant that provides well-formatted, easy-to-read responses.

{language_instruction}

FORMATTING RULES:
1. Start with a brief summary answering the user's question
2. If the data has multiple columns, present it in a markdown TABLE format
3. If showing a simple list, use numbered list
4. For aggregated counts, show them clearly with the count value
5. Keep the response concise but complete
6. Present ALL results - do NOT say "showing sample" or "showing X of Y"

Example table format:
| Name | Department | Count |
|------|------------|-------|
| John | Engineering | 5 |

Example list format:
1. **Rinku Gautam** - 2,592 incomplete tasks
2. **Atul Yadav** - 843 incomplete tasks

Be natural and conversational while keeping data organized.
Do NOT add disclaimers about showing partial data."""),
            ("human", """User Question: {question}

SQL Query: {sql}

Total Results: {result_count}
Query Results: {results}

Provide a well-formatted, natural language answer with ALL the data:""")
        ])
        
        chain = answer_prompt | self.llm | StrOutputParser()
        
        try:
            answer = chain.invoke({
                "language_instruction": language_instruction,
                "question": state["user_question"],
                "sql": state["generated_sql"],
                "result_count": result_count,
                "results": str(display_results)
            })
            
            log_step("7️⃣ ANSWER_GENERATOR ✅", "Answer generated!", answer[:500] + "..." if len(answer) > 500 else answer)
            return {"final_answer": answer}
        except Exception as e:
            log_step("7️⃣ ANSWER_GENERATOR ❌", f"Error: {str(e)}")
            return {"final_answer": f"Results: {display_results}"}
    
    def _cache_result(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Cache the successful query result."""
        if state.get("error") or state.get("is_blocked") or state.get("cache_hit"):
            return {}
        
        log_step("8️⃣ CACHE_STORE", "Caching successful query...")
        
        try:
            query_cache.cache_query(
                question=state["user_question"],
                sql=state["generated_sql"],
                intent_analysis=state.get("intent_analysis", ""),
                language=state.get("detected_language", "english")
            )
            log_step("8️⃣ CACHE_STORE ✅", "Query cached for future use")
        except Exception as e:
            log_step("8️⃣ CACHE_STORE ❌", f"Failed to cache: {e}")
        
        return {}
    
    def _handle_blocked(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Handle blocked queries with appropriate error message."""
        error_msg = state.get("error", "Query blocked")
        log_step("🚫 BLOCKED_HANDLER", f"Query was blocked: {error_msg}")
        
        if state.get("detected_language") == "hinglish":
            return {"final_answer": f"🚫 Maaf kijiye, yeh query allow nahi hai. {error_msg}"}
        else:
            return {"final_answer": f"🚫 Sorry, this query is not allowed. {error_msg}"}
    
    async def process_query(
        self,
        question: str,
        session_id: Optional[str] = None,
        request_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Process a user question through the complete flow.
        
        Args:
            question: User's natural language question
            session_id: Optional session ID for history tracking
            request_id: Optional request ID for cancellation support
            
        Returns:
            Dict containing answer, sql, and metadata
        """
        # Register request for cancellation tracking
        if request_id:
            self.register_request(request_id)
        
        try:
            # Log pipeline start
            log_pipeline_start(question)
            
            # Add user message to session if provided
            if session_id:
                session_service.add_message(
                    session_id=session_id,
                    role="user",
                    content=question
                )
            
            # Initialize state
            initial_state = {
                "user_question": question,
                "session_id": session_id,
                "detected_language": "english",
                "schema_context": "",
                "enum_context": "",
                "sample_data_context": "",
                "relationship_context": "",
                "intent_analysis": "",
                "generated_sql": "",
                "security_result": {},
                "query_result": None,
                "final_answer": "",
                "error": None,
                "is_blocked": False,
                "cache_hit": False,
                "cancelled": False
            }
            
            # Check for cancellation before starting
            if request_id and self.is_cancelled(request_id):
                return {
                    "answer": "Request was cancelled.",
                    "sql": None,
                    "cancelled": True
                }
            
            # Run the workflow
            final_state = self.workflow.invoke(initial_state)
            
            # Log pipeline summary
            log_pipeline_summary(final_state)
            
            # Add assistant message to session
            if session_id:
                session_service.add_message(
                    session_id=session_id,
                    role="assistant",
                    content=final_state.get("final_answer", ""),
                    sql=final_state.get("generated_sql") if not final_state.get("is_blocked") else None
                )
            
            # Prepare response
            response = {
                "answer": final_state.get("final_answer", ""),
                "sql": final_state.get("generated_sql") if not final_state.get("is_blocked") else None,
                "language": final_state.get("detected_language", "english"),
                "is_blocked": final_state.get("is_blocked", False),
                "error": final_state.get("error"),
                "cache_hit": final_state.get("cache_hit", False),
                "session_id": session_id
            }
            
            return response
            
        finally:
            # Unregister request
            if request_id:
                self.unregister_request(request_id)
    
    async def process_query_streaming(
        self,
        question: str,
        session_id: Optional[str] = None,
        request_id: Optional[str] = None
    ):
        """
        Process a user question with streaming response for the answer.
        
        Yields:
            JSON strings with type: 'status', 'chunk', 'sql', 'done', 'error'
        """
        import json as json_module
        
        if request_id:
            self.register_request(request_id)
        
        try:
            log_pipeline_start(question)
            
            # Add user message to session
            if session_id:
                session_service.add_message(
                    session_id=session_id,
                    role="user",
                    content=question
                )
                print(f"💬 Added user message to session {session_id[:8]}...")
            
            # Yield: Processing started
            yield json_module.dumps({"type": "status", "message": "Processing your query..."}) + "\n"
            print("📝 Step 1: Processing query...")
            
            # Default language detection (done early for all paths)
            question_lower = question.lower()
            words = question_lower.split()
            hinglish_count = sum(1 for w in words if w in self.hinglish_words)
            detected_language = "hinglish" if hinglish_count >= 2 else "english"
            print(f"🌐 Step 2: Detected language: {detected_language}")
            
            # Check cache first
            cached = query_cache.find_similar_query(question)
            if cached:
                yield json_module.dumps({"type": "status", "message": "Found similar query in cache!"}) + "\n"
                yield json_module.dumps({"type": "cache_hit", "value": True}) + "\n"
                generated_sql = cached['sql']
                print(f"⚡ Step 3: CACHE HIT! Using cached SQL")
            else:
                yield json_module.dumps({"type": "cache_hit", "value": False}) + "\n"
                print("🔍 Step 3: Cache miss - generating new SQL...")
                
                # Fetch schema
                yield json_module.dumps({"type": "status", "message": "Fetching database context..."}) + "\n"
                print("📊 Step 4: Fetching database schema...")
                schema_context = self._get_detailed_schema()
                enum_context = self._get_enum_context()
                sample_data = self._get_sample_data_context()
                relationship_context = self._get_relationship_context()
                
                # Generate SQL
                yield json_module.dumps({"type": "status", "message": "Generating SQL query..."}) + "\n"
                print("🤖 Step 5: Calling LLM to generate SQL...")
                
                # Build SQL prompt (simplified for streaming)
                sql_prompt = self._build_sql_prompt(
                    question, detected_language, schema_context, 
                    enum_context, sample_data, relationship_context
                )
                
                resp = self.llm.invoke(sql_prompt)
                generated_sql = resp.content.strip()
                generated_sql = re.sub(r"```sql|```", "", generated_sql).strip()
                generated_sql = re.sub(r"--.*$", "", generated_sql, flags=re.MULTILINE).strip()
                print(f"✅ Step 6: SQL Generated:\n{generated_sql[:200]}...")
                
                # Cache the query
                query_cache.cache_query(question, generated_sql, "", detected_language)
                print("💾 Cached new query")
            
            # Security validation
            yield json_module.dumps({"type": "status", "message": "Validating query security..."}) + "\n"
            print("🔒 Step 7: Validating SQL security...")
            is_valid, error_message, sanitized_sql = validate_sql_security(generated_sql)
            
            if not is_valid:
                print(f"❌ Security validation FAILED: {error_message}")
                yield json_module.dumps({"type": "error", "message": f"Query blocked: {error_message}"}) + "\n"
                return
            print("✅ Security validation passed")
            
            # Yield the SQL
            yield json_module.dumps({"type": "sql", "value": sanitized_sql}) + "\n"
            
            # Execute query
            yield json_module.dumps({"type": "status", "message": "Executing query..."}) + "\n"
            print("🗄️ Step 8: Executing SQL query...")
            
            try:
                results = self.db_service.execute_select(sanitized_sql)
                result_count = len(results) if results else 0
                print(f"✅ Query executed - {result_count} results")
            except Exception as e:
                print(f"❌ Query execution FAILED: {str(e)}")
                yield json_module.dumps({"type": "error", "message": f"Query failed: {str(e)}"}) + "\n"
                return
            
            yield json_module.dumps({"type": "status", "message": f"Found {result_count} results. Generating response..."}) + "\n"
            print(f"🤖 Step 9: Streaming answer from LLM...")
            
            # Stream the answer generation
            language_instruction = "Respond in Hinglish (Hindi-English mix)." if detected_language == "hinglish" else "Respond in English"
            
            answer_prompt = f"""You are a helpful database assistant. {language_instruction}

User Question: {question}
SQL Query: {sanitized_sql}
Total Results: {result_count}
Query Results: {str(results[:100]) if result_count > 100 else str(results)}

FORMATTING RULES:
1. Start with a brief summary
2. Use markdown TABLE format for multiple columns
3. Use numbered lists for simple lists
4. Be concise but complete
5. Do NOT say "showing sample" - present ALL data

Provide a well-formatted answer:"""

            # Use streaming LLM
            full_answer = ""
            for chunk in self.llm.stream(answer_prompt):
                if hasattr(chunk, 'content') and chunk.content:
                    full_answer += chunk.content
                    yield json_module.dumps({"type": "chunk", "content": chunk.content}) + "\n"
            
            # Save to session
            if session_id:
                session_service.add_message(
                    session_id=session_id,
                    role="assistant",
                    content=full_answer,
                    sql=sanitized_sql
                )
            
            # Done
            yield json_module.dumps({"type": "done", "session_id": session_id}) + "\n"
            
        except Exception as e:
            yield json_module.dumps({"type": "error", "message": str(e)}) + "\n"
        finally:
            if request_id:
                self.unregister_request(request_id)
    
    def _build_sql_prompt(self, question, language, schema, enums, samples, relationships):
        """Build the SQL generation prompt."""
        hinglish_guide = """
=== HINGLISH TRANSLATION ===
- "dikhao"/"batao" = show
- "kitne" = how many
- "sabhi"/"sab" = all
- "wale" = those who
- "pending wale" = WHERE status = 'no'
""" if language == "hinglish" else ""

        return f"""You are a PostgreSQL SQL generator. Generate READ-ONLY SELECT queries only.
{hinglish_guide}

CRITICAL RULES:
- ONLY SELECT queries allowed
- checklist.status: 'yes' (completed), 'no' (not completed)
- users.status: 'active', 'inactive', 'on_leave', 'terminated'

⚠️ CRITICAL DATE HANDLING:
The column checklist.planned_date stores dates as TEXT in MIXED formats and may have invalid data.

Create a helper function in your query using a CTE or just filter valid dates:

For date comparisons, first filter only valid date formats, then compare:
- Valid DD/MM/YYYY: planned_date ~ '^[0-9]{{2}}/[0-9]{{2}}/[0-9]{{4}}$'
- Valid ISO: planned_date ~ '^[0-9]{{4}}-[0-9]{{2}}-[0-9]{{2}}'

Example - Find active users with overdue incomplete tasks (HANDLES ALL DATE FORMATS SAFELY):
SELECT DISTINCT u.* FROM users u
JOIN checklist c ON u.id = c.user_id
WHERE u.status = 'active' 
AND c.status = 'no' 
AND (
    (c.planned_date ~ '^[0-9]{{2}}/[0-9]{{2}}/[0-9]{{4}}$' AND TO_TIMESTAMP(c.planned_date, 'DD/MM/YYYY') < NOW())
    OR 
    (c.planned_date ~ '^[0-9]{{4}}-[0-9]{{2}}-[0-9]{{2}}' AND c.planned_date::timestamp < NOW())
)

This safely handles:
- DD/MM/YYYY dates (28/11/2025)
- ISO dates (2025-12-22T09:00:00)  
- Ignores invalid data (numbers, nulls, etc.)

Database Schema:
{schema}

{enums}

{samples}

{relationships}

User Question: {question}

Return ONLY the SQL statement (no markdown, no explanation):"""


# Singleton instance
chat_service = ChatService()
