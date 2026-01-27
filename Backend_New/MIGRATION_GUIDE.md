# 🚀 Backend Migration Guide

## Overview
Migrating from simple FastAPI backend to complete dual-LLM system with LangGraph.

## What's New?
- ✅ **6-Node LangGraph** state machine
- ✅ **Dual-LLM Validation** (Generator + Validator)
- ✅ **5-Step Mandatory Analysis** for query generation
- ✅ **Schema-Evidence Validation** for query approval
- ✅ **Validation Loop** with max 3 attempts
- ✅ **Multi-Table Handling** (checklist + delegation)
- ✅ **5-Layer Security** validator (50K char limit, 40 keywords, 21 patterns)
- ✅ **SQLite Session Storage** for persistence
- ✅ **Streaming with SSE** compatible with Frontend

## Quick Migration Steps

### 1. ✅ COMPLETED - New Backend Created
All files created in `Backend_New/`:
- main.py (FastAPI entry point)
- app/core/config.py (settings)
- app/core/security.py (5-layer validator)
- app/services/sql_agent.py (LLM prompts)
- app/services/agent_nodes.py (LangGraph nodes)
- app/services/session_manager.py (session storage)
- app/api/routes/chat.py (streaming endpoint)
- app/api/routes/sessions.py (session CRUD)
- app/api/routes/health.py (health checks)
- requirements.txt (dependencies)
- .env.example (config template)
- All __init__.py files created

### 2. Copy Environment Configuration

```powershell
# From project root
cd Backend_New

# If old Backend has .env, copy it
Copy-Item ..\Backend\.env .env

# Otherwise, create from template
Copy-Item .env.example .env
# Then edit .env and add your credentials
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

Expected packages:
- fastapi==0.115.0
- uvicorn[standard]
- langchain==0.3.7
- langgraph==0.2.45
- langchain-openai
- psycopg2-binary
- pydantic-settings
- python-dotenv
- SQLAlchemy

### 4. Test Backend

```powershell
# Start server
python main.py

# In another terminal, test health
curl http://localhost:8000/health
# Should return: {"status":"healthy","version":"1.0.0"}
```

### 5. Test with Frontend

```powershell
# Open Frontend in browser
start ..\Frontend\index.html

# Or if you have a local server
cd ..\Frontend
python -m http.server 3000
# Then open http://localhost:3000
```

### 6. Verify Complete Workflow

Test these queries in Frontend:
1. **Simple Query**: "How many pending tasks?"
   - Should see: Schema analysis → LLM 1 generation → LLM 2 validation → Execution

2. **Multi-Table Query**: "Performance report for Hem Kumar Jagat"
   - Should see: Multi-table detection → Separate execution → Result aggregation

3. **Validation Loop**: "Show tasks with created_at today"
   - Should see: LLM 2 rejection → Feedback → LLM 1 regeneration → Retry

4. **Security Block**: "DROP TABLE users;"
   - Should see: Security validation error immediately

### 7. Remove Old Backend (After Testing)

```powershell
# Backup first (optional)
Rename-Item ..\Backend Backend_OLD

# Or delete after confirming everything works
Remove-Item ..\Backend -Recurse -Force

# Rename new backend
cd ..
Rename-Item Backend_New Backend
```

## API Changes

### Old Backend
- Simple `/chat` endpoint
- No validation loop
- No LangGraph
- Basic error handling

### New Backend
- **POST** `/chat/stream` - Streaming with SSE (same format as before)
- **GET** `/chat/sessions` - Session list
- **POST** `/chat/sessions` - Create session
- **GET** `/chat/sessions/{id}/messages` - Get messages
- **DELETE** `/chat/sessions/{id}` - Delete session
- **POST** `/chat/sessions/{id}/clear` - Clear session
- **GET** `/chat/cache/stats` - Cache stats (compatibility)
- **POST** `/chat/cache/clear` - Clear cache (compatibility)
- **GET** `/health` - Health check

**Note**: All Frontend endpoints remain compatible!

## Architecture Comparison

### Old Backend
```
User Input → Simple LLM Call → Execute Query → Return Results
```

### New Backend (from sagar.ipynb)
```
User Input 
  ↓
list_tables (get available tables)
  ↓
call_get_schema (fetch schema + samples)
  ↓
store_schema (save to state)
  ↓
generate_query (LLM 1 with 5-step analysis)
  ↓
validate_query (LLM 2 with schema-evidence)
  ↓
  ├─ APPROVED → run_query (security check + execute)
  └─ REJECTED → regenerate (back to generate_query, max 3 times)
```

## Testing Checklist

- [ ] Backend starts on port 8000
- [ ] `/health` returns success
- [ ] Frontend connects successfully
- [ ] Simple query works (e.g., "How many tasks?")
- [ ] Multi-table query works (e.g., "Performance report...")
- [ ] Validation loop triggers (e.g., wrong field names)
- [ ] Security blocks malicious queries (e.g., "DROP TABLE...")
- [ ] Sessions persist correctly
- [ ] Streaming shows progress indicators
- [ ] Query display shows generated SQL
- [ ] Results format correctly

## Troubleshooting

### Import Errors
```powershell
# Check all __init__.py files exist
Get-ChildItem -Recurse -Filter "__init__.py" | Select-Object FullName
```

### Database Connection
```powershell
# Test PostgreSQL connection
psql -h localhost -U postgres -d your_database -c "SELECT 1"
```

### OpenAI API
```powershell
# Verify API key
Select-String -Path .env -Pattern "OPENAI_API_KEY"
```

### Port 8000 in Use
```powershell
# Find and kill process
Get-NetTCPConnection -LocalPort 8000 | Select-Object OwningProcess
Stop-Process -Id <PID>
```

### Module Not Found
```powershell
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## Rollback Plan

If issues arise:
```powershell
# Stop new backend (Ctrl+C)

# Restore old backend
cd ..
Rename-Item Backend_OLD Backend

# Start old backend
cd Backend\src
uvicorn main:app --reload
```

## Session Data

Sessions stored in SQLite: `Backend_New/chat_sessions.db`

Schema:
```sql
-- sessions table
CREATE TABLE sessions (
    session_id TEXT PRIMARY KEY,
    title TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- messages table
CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    session_id TEXT,
    role TEXT,  -- 'user' or 'assistant'
    content TEXT,
    timestamp TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id)
);
```

## Performance Notes

- LangGraph adds ~2-3s latency (schema analysis + dual-LLM)
- Validation loop adds ~1-2s per retry (max 3 attempts)
- Streaming ensures responsive UI despite latency
- Session queries cached in memory

## Next Steps

1. ✅ Backend structure complete
2. ⏳ Copy .env configuration
3. ⏳ Install dependencies
4. ⏳ Start backend
5. ⏳ Test with Frontend
6. ⏳ Verify all features
7. ⏳ Remove old Backend
8. ⏳ Rename Backend_New → Backend

## Support

Check logs for detailed execution traces:
- Console output shows LangGraph node execution
- SSE events show progress in real-time
- Error messages include full stack traces

For issues, check:
1. [README.md](README.md) - Complete documentation
2. `.env` - Configuration
3. `requirements.txt` - Dependencies
4. Console logs - Error messages
