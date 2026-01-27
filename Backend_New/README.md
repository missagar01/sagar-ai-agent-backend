# DB Assistant - FastAPI Backend with Dual-LLM Validation

Complete FastAPI backend implementing the sophisticated dual-LLM SQL agent from `sagar.ipynb` with LangGraph state machine.

## 🎯 Architecture Overview

### Dual-LLM Validation System
- **LLM 1 (Generator)**: Creates SQL queries using 5-step mandatory analysis
- **LLM 2 (Validator)**: Validates queries using schema-evidence checking
- **Validation Loop**: Max 3 attempts with feedback-driven regeneration

### LangGraph State Machine (6 Nodes)
```
START → list_tables → call_get_schema → store_schema → 
generate_query → [validate_query → regenerate OR run_query] → END
```

### 5-Layer Security Validation
1. **Length Check**: Max 50,000 characters
2. **Whitelist**: Only SELECT/WITH statements allowed
3. **Keyword Blocking**: 40 dangerous keywords (DROP, DELETE, UPDATE, etc.)
4. **Pattern Blocking**: 21 regex patterns for SQL injection
5. **Multi-Statement**: Blocks multiple statements (semicolon detection)

## 📁 Project Structure

```
Backend_New/
├── main.py                          # FastAPI entry point
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment template
├── app/
│   ├── core/
│   │   ├── config.py               # Pydantic settings
│   │   └── security.py             # 5-layer security validator
│   ├── services/
│   │   ├── sql_agent.py            # LLM prompts & DB initialization
│   │   ├── agent_nodes.py          # LangGraph nodes & graph builder
│   │   └── session_manager.py      # SQLite session storage
│   └── api/
│       └── routes/
│           ├── chat.py             # Streaming endpoint with SSE
│           ├── sessions.py         # Session CRUD operations
│           └── health.py           # Health checks
```

## 🚀 Quick Start

### 1. Copy Environment Configuration
```powershell
# Copy .env from old Backend
Copy-Item ..\Backend\.env .env
```

### 2. Install Dependencies
```powershell
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Edit `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
DB_HOST=localhost
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME=your_database
DB_PORT=5432
```

### 4. Run Backend
```powershell
# Option 1: Direct Python
python main.py

# Option 2: Uvicorn with hot reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Verify Health
```powershell
# PowerShell
Invoke-WebRequest -Uri http://localhost:8000/health

# Or open in browser
start http://localhost:8000/health
```

## 📡 API Endpoints

### Chat Endpoints
- **POST** `/chat/stream` - Stream chat responses with SSE
- **GET** `/chat/cache/stats` - Get cache statistics
- **POST** `/chat/cache/clear` - Clear cache

### Session Management
- **GET** `/chat/sessions` - List all sessions
- **POST** `/chat/sessions` - Create new session
- **GET** `/chat/sessions/{id}/messages` - Get session messages
- **DELETE** `/chat/sessions/{id}` - Delete session
- **POST** `/chat/sessions/{id}/clear` - Clear session messages

### Health Checks
- **GET** `/health` - Application health status
- **GET** `/ping` - Simple ping endpoint

## 🤖 LLM Prompts

### LLM 1: Query Generator (5-Step Analysis)
1. **NULL Pattern Detection** - Analyze NULL representation patterns
2. **Timestamp Field Comparison** - Compare date field names
3. **Multi-Table Discovery** - Identify relationships and joins
4. **Field Name Semantic Analysis** - Map user intent to schema
5. **Self-Validation Checklist** - Verify query correctness

### LLM 2: Query Validator (Schema-Evidence)
- Schema-based validation with evidence citation
- JSON output format with validation status and feedback
- Detects field mismatches, wrong table references, invalid operations

## 🔒 Security Features

### Hardcoded Security Validator
- **40 Blocked Keywords**: DROP, DELETE, UPDATE, INSERT, ALTER, TRUNCATE, etc.
- **21 Blocked Patterns**: SQL injection, file operations, admin commands
- **Query Sanitization**: Automatic LIMIT addition, semicolon removal
- **Table Whitelist**: Only users, checklist, delegation tables allowed

### Multi-Table Query Handling
- Automatic detection of checklist + delegation queries
- Separate execution with result aggregation
- Error handling for cross-table operations

## 🔄 Workflow Example

### User Query: "Performance report for Hem Kumar Jagat"

```
1. 📊 Loading tables... (list_tables)
   → Returns: ['users', 'checklist', 'delegation']

2. 🔍 Fetching schema... (call_get_schema)
   → Retrieves schema + 3 sample rows per table

3. 💾 Storing schema... (store_schema)
   → Saves to LangGraph state

4. 🤖 LLM 1: Generating query... (generate_query)
   → 5-Step Analysis:
     STEP 1: NULL pattern = '' (empty string)
     STEP 2: Timestamp field = created_ts
     STEP 3: Multi-table = checklist + delegation JOIN
     STEP 4: "performance report" = task count, status breakdown
     STEP 5: Query verification checklist passed
   → Output: SQL query

5. 🔍 LLM 2: Validating query... (validate_query)
   → Schema-evidence validation
   → Check: Field names correct? ✅
   → Check: Table references valid? ✅
   → Check: Join conditions sound? ✅
   → Output: {"validation_status": "APPROVED"}

6. 🔒 Security check... (run_query_node)
   → 5-layer validation: ✅ PASSED

7. ⚡ Executing query... (run_query_node)
   → Multi-table detection: True
   → Execute checklist query
   → Execute delegation query
   → Aggregate results

8. 📊 Streaming results... (SSE to Frontend)
   → Word-by-word streaming via Server-Sent Events
```

## 🧪 Testing

### Test Basic Functionality
```powershell
# Test health endpoint
curl http://localhost:8000/health

# Test session creation
curl -X POST http://localhost:8000/chat/sessions `
  -H "Content-Type: application/json" `
  -d '{"title":"Test Session"}'

# Test chat (requires session_id from above)
curl -X POST http://localhost:8000/chat/stream `
  -H "Content-Type: application/json" `
  -d '{"message":"How many pending tasks?","session_id":"<session_id>"}'
```

### Test Validation Loop
Try queries that should fail validation:
- "Show tasks created_at today" → Should reject (wrong field name)
- "List tasks with status pending" → Should reject (status field doesn't exist)

### Test Security
Try malicious queries:
- "DROP TABLE users;" → Should block
- "UPDATE checklist SET..." → Should block
- Query >50K characters → Should block

## 🛠️ Configuration

### Database Configuration
Edit `app/core/config.py`:
```python
ALLOWED_TABLES: list[str] = ["users", "checklist", "delegation"]
MAX_QUERY_LENGTH: int = 50000
MAX_VALIDATION_ATTEMPTS: int = 3
```

### LLM Configuration
Edit `app/services/sql_agent.py`:
```python
model = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    streaming=True
)
```

## 📊 Session Storage

SQLite database (`chat_sessions.db`) with two tables:
- **sessions**: session_id, title, created_at, updated_at
- **messages**: id, session_id, role, content, timestamp

## 🔗 Frontend Integration

Frontend expects:
- **Streaming Format**: Server-Sent Events (SSE)
- **Event Types**: 'status', 'query', 'content', 'done', 'error'
- **Base URL**: http://localhost:8000

Progress indicators:
- 🔄 Analyzing schema...
- 🤖 LLM 1: Generating query...
- 🔍 LLM 2: Validating query...
- ✅ Query approved!
- ⚡ Executing query...

## 🐛 Troubleshooting

### Import Errors
```powershell
# Ensure all __init__.py files exist
Get-ChildItem -Recurse -Filter "__init__.py"
```

### Database Connection Errors
```powershell
# Test PostgreSQL connection
psql -h localhost -U postgres -d your_database -c "SELECT 1"
```

### OpenAI API Errors
```powershell
# Verify API key in .env
Select-String -Path .env -Pattern "OPENAI_API_KEY"
```

### Port Already in Use
```powershell
# Kill process on port 8000
Get-NetTCPConnection -LocalPort 8000 | Select-Object OwningProcess
Stop-Process -Id <PID>
```

## 📝 Notes

### Differences from sagar.ipynb
- ✅ Added: Session persistence (SQLite)
- ✅ Added: RESTful API endpoints
- ✅ Added: Frontend serving
- ✅ Added: Health checks
- ✅ Maintained: Complete LangGraph workflow
- ✅ Maintained: Dual-LLM validation
- ✅ Maintained: 5-step analysis framework
- ✅ Maintained: Security validation (all 5 layers)

### Why Rebuild?
Old backend lacked:
- ❌ No LangGraph state machine
- ❌ No dual-LLM validation
- ❌ No 5-step mandatory analysis
- ❌ No validation loops with feedback
- ❌ No sophisticated schema pattern discovery

New backend implements:
- ✅ Complete 6-node LangGraph workflow
- ✅ Adversarial dual-LLM system
- ✅ 5-step mandatory analysis for LLM 1
- ✅ Schema-evidence validation for LLM 2
- ✅ Validation loop (max 3 attempts)
- ✅ Multi-table query handling
- ✅ Hardcoded security (5 layers)
- ✅ Streaming compatible with Frontend SSE

## 📚 Dependencies

Key packages:
- **FastAPI 0.115.0** - Web framework
- **LangGraph 0.2.45** - State machine orchestration
- **LangChain 0.3.7** - LLM abstractions
- **psycopg2-binary** - PostgreSQL adapter
- **Pydantic v2** - Settings & validation
- **uvicorn** - ASGI server

## 🎓 Learning Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Server-Sent Events (SSE)](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## 📄 License

Part of DB_Assistant project - Dual-LLM SQL Agent with LangGraph
