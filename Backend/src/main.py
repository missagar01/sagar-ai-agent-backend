"""
FastAPI Application Entry Point
================================
DB Assistant Backend with Hardcoded Security

Security Architecture:
┌─────────────────────────────────────────────────────────────┐
│                    USER REQUEST                              │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  LAYER 1: API Validation (Pydantic)                         │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  LAYER 2: LLM generates SQL                                 │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  🔒 LAYER 3: HARDCODED SECURITY VALIDATION                  │
│  ├── Length check (max 2000 chars)                          │
│  ├── Whitelist check (SELECT only)                          │
│  ├── Blocked keyword detection (40+ keywords)               │
│  ├── Blocked pattern detection (regex)                      │
│  └── Multiple statement detection                           │
└─────────────────────┬───────────────────────────────────────┘
                      │
            ┌─────────┴─────────┐
            │                   │
        BLOCKED              ALLOWED
            │                   │
            ▼                   ▼
    ❌ Return Error      ✅ Execute Query
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="DB Assistant API",
    description="Read-only database chatbot with hardcoded security",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware - Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:5500",  # Live Server
        "http://127.0.0.1:5500",
        "http://localhost:3000",
        "null",  # For file:// protocol
        "*"  # Allow all for development
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PUT", "PATCH", "OPTIONS"],
    allow_headers=["*"],
)


# Import and include routers
from src.api.routes import chat, health

app.include_router(chat.router)
app.include_router(health.router)


# Serve Frontend static files
frontend_path = Path(__file__).parent.parent.parent / "Frontend"
if frontend_path.exists():
    app.mount("/static", StaticFiles(directory=str(frontend_path)), name="static")
    
    @app.get("/app", tags=["frontend"])
    async def serve_frontend():
        """Serve the frontend application."""
        return FileResponse(str(frontend_path / "index.html"))


@app.get("/", tags=["root"])
async def root():
    """Root endpoint with API information."""
    return {
        "name": "DB Assistant API",
        "version": "1.0.0",
        "description": "Read-only database chatbot with hardcoded security",
        "frontend": "/app",
        "docs": "/docs",
        "health": "/health",
        "endpoints": {
            "POST /chat": "Process natural language queries",
            "GET /chat/tables": "List allowed tables",
            "GET /chat/schema": "Get database schema",
            "POST /chat/config/tables": "Configure allowed tables",
            "GET /health": "Health check",
            "GET /app": "Frontend application"
        }
    }


@app.on_event("startup")
async def startup_event():
    """Initialize services on startup."""
    print("🚀 Starting DB Assistant API...")
    print("📊 Security: HARDCODED (40+ blocked keywords)")
    print("🔒 Mode: READ-ONLY (SELECT queries only)")
    
    # Test database connection
    from src.services.db_service import db_service
    if db_service.test_connection():
        print("✅ Database connection: OK")
    else:
        print("❌ Database connection: FAILED")
    
    # Check OpenAI API key
    if os.getenv("OPENAI_API_KEY"):
        print("✅ OpenAI API key: Configured")
    else:
        print("❌ OpenAI API key: NOT CONFIGURED")
    
    # Check frontend
    if frontend_path.exists():
        print(f"✅ Frontend available at: /app")
    else:
        print(f"⚠️ Frontend not found at: {frontend_path}")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown."""
    print("👋 Shutting down DB Assistant API...")