"""
Session Management Routes
==========================
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid

from app.services.session_manager import session_manager

router = APIRouter()

class CreateSessionRequest(BaseModel):
    title: Optional[str] = "New Chat"

@router.get("")
async def list_sessions():
    """List all chat sessions"""
    sessions = session_manager.get_sessions()
    return sessions

@router.post("")
async def create_session(request: CreateSessionRequest = CreateSessionRequest()):
    """Create a new chat session"""
    session_id = str(uuid.uuid4())
    session = session_manager.create_session(session_id, request.title)
    return session

@router.get("/{session_id}/messages")
async def get_session_messages(session_id: str):
    """Get all messages for a session"""
    messages = session_manager.get_session_messages(session_id)
    return {"session_id": session_id, "messages": messages}

@router.delete("/{session_id}")
async def delete_session(session_id: str):
    """Delete a session"""
    try:
        session_manager.delete_session(session_id)
        return {"status": "success", "message": f"Session {session_id} deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{session_id}/clear")
async def clear_session(session_id: str):
    """Clear all messages from a session"""
    try:
        session_manager.clear_session(session_id)
        return {"status": "success", "message": f"Session {session_id} cleared"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
