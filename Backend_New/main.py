"""
FastAPI Application with LangGraph SQL Agent
==============================================
Complete implementation of sagar.ipynb logic with:
- Dual-LLM validation (Generator + Validator)
- Human-in-the-loop via streaming
- Hardcoded security validation
- Session management
- Streaming responses
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn

from app.api.routes import chat, health, sessions
from app.core.config import settings

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    description="SQL Database Assistant with Dual-LLM Validation",
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "http://localhost:3000",
        "null",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(sessions.router, prefix="/chat/sessions", tags=["sessions"])
app.include_router(health.router, tags=["health"])

# Serve Frontend
frontend_path = Path(__file__).parent.parent / "Frontend"
if frontend_path.exists():
    app.mount("/static", StaticFiles(directory=str(frontend_path)), name="static")
    
    @app.get("/app")
    async def serve_frontend():
        return FileResponse(str(frontend_path / "index.html"))

@app.get("/")
async def root():
    return {
        "name": settings.APP_NAME,
        "version": "2.0.0",
        "status": "active",
        "features": [
            "Dual-LLM Validation",
            "Human-in-the-Loop",
            "Streaming Responses",
            "Session Management",
            "Hardcoded Security"
        ]
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
