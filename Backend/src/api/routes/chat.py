"""
Chat API Routes
================
LAYER 1: API Validation using Pydantic models.

Features:
- Chat endpoint with session support
- Streaming responses for real-time output
- Session management (create, list, delete, clear)
- Cache management (stats, clear, configure)
- Request cancellation support
- Verbose mode configuration
"""

from fastapi import APIRouter, HTTPException, status, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, Any
import re
import uuid

router = APIRouter(prefix="/chat", tags=["chat"])


# ============================================================================
# PYDANTIC MODELS
# ============================================================================

class ChatRequest(BaseModel):
    """Request model for chat endpoint."""
    question: str = Field(
        ...,
        min_length=3,
        max_length=1000,
        description="User's natural language question"
    )
    session_id: Optional[str] = Field(
        None,
        description="Session ID for conversation history"
    )
    
    @validator('question')
    def validate_question(cls, v):
        """Additional validation for the question field."""
        if not v or not v.strip():
            raise ValueError("Question cannot be empty")
        
        v = ' '.join(v.split())
        
        suspicious_patterns = [
            r'<script',
            r'javascript:',
            r'on\w+\s*=',
        ]
        
        for pattern in suspicious_patterns:
            if re.search(pattern, v, re.IGNORECASE):
                raise ValueError("Invalid input detected")
        
        return v


class ChatResponse(BaseModel):
    """Response model for chat endpoint."""
    answer: str = Field(..., description="Natural language answer")
    sql: Optional[str] = Field(None, description="Generated SQL query (if allowed)")
    language: str = Field("english", description="Detected language (english/hinglish)")
    is_blocked: bool = Field(False, description="Whether query was blocked by security")
    error: Optional[str] = Field(None, description="Error message if any")
    cache_hit: bool = Field(False, description="Whether response came from cache")
    session_id: Optional[str] = Field(None, description="Session ID")
    request_id: Optional[str] = Field(None, description="Request ID for cancellation")


class SessionCreateRequest(BaseModel):
    """Request model for creating a new session."""
    title: Optional[str] = Field(None, max_length=200, description="Optional session title")


class SessionResponse(BaseModel):
    """Response model for session details."""
    session_id: str
    title: str
    created_at: str
    updated_at: str
    message_count: int


class MessageResponse(BaseModel):
    """Response model for a chat message."""
    message_id: str
    session_id: str
    role: str  # 'user' or 'assistant'
    content: str
    sql: Optional[str] = None
    timestamp: str


class SessionMessagesResponse(BaseModel):
    """Response model for session messages."""
    session_id: str
    messages: List[MessageResponse]
    total: int


class CacheStatsResponse(BaseModel):
    """Response model for cache statistics."""
    enabled: bool
    total_entries: int = 0
    similarity_threshold: float = 0.9
    error: Optional[str] = None


class CacheConfigRequest(BaseModel):
    """Request model for cache configuration."""
    similarity_threshold: Optional[float] = Field(
        None, 
        ge=0.0, 
        le=1.0,
        description="Similarity threshold (0.0 to 1.0)"
    )


class VerboseConfigRequest(BaseModel):
    """Request model for verbose mode configuration."""
    enabled: bool = Field(..., description="Enable or disable verbose logging")


class VerboseConfigResponse(BaseModel):
    """Response model for verbose mode configuration."""
    verbose_mode: bool
    message: str


class CancelRequest(BaseModel):
    """Request model for cancelling a query."""
    request_id: str = Field(..., description="The request ID to cancel")


class CancelResponse(BaseModel):
    """Response model for cancel operation."""
    success: bool
    message: str


class TableConfigRequest(BaseModel):
    """Request model for table configuration."""
    action: str = Field(..., pattern="^(add|remove)$", description="Action to perform")
    table_name: str = Field(..., min_length=1, max_length=100, description="Table name")
    
    @validator('table_name')
    def validate_table_name(cls, v):
        if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)?$', v):
            raise ValueError("Invalid table name format")
        return v


class SchemaResponse(BaseModel):
    """Response model for schema endpoint."""
    tables: List[str]
    schema_info: dict


# ============================================================================
# CHAT ENDPOINTS
# ============================================================================

@router.post("/", response_model=ChatResponse, summary="Process a chat query")
async def chat_endpoint(request: ChatRequest):
    """
    Process a user's natural language question (non-streaming).
    
    Features:
    - Semantic caching (90% similarity threshold)
    - Session support for conversation history
    - Cancellation support via request_id
    """
    from src.services.chat_service import chat_service
    
    # Generate request ID for cancellation support
    request_id = str(uuid.uuid4())
    
    try:
        result = await chat_service.process_query(
            question=request.question,
            session_id=request.session_id,
            request_id=request_id
        )
        
        response = ChatResponse(
            answer=result.get("answer", ""),
            sql=result.get("sql"),
            language=result.get("language", "english"),
            is_blocked=result.get("is_blocked", False),
            error=result.get("error"),
            cache_hit=result.get("cache_hit", False),
            session_id=result.get("session_id"),
            request_id=request_id
        )
        return response
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing query: {str(e)}"
        )


@router.post("/stream", summary="Process a chat query with streaming response")
async def chat_stream_endpoint(request: ChatRequest):
    """
    Process a user's natural language question with STREAMING response.
    
    Returns Server-Sent Events (SSE) stream with:
    - status: Processing status updates
    - cache_hit: Whether response came from cache
    - sql: Generated SQL query
    - chunk: Answer text chunks (streamed word-by-word)
    - done: Completion signal
    - error: Error messages
    
    This endpoint provides real-time feedback as the query is processed,
    making the response feel instant and reducing perceived latency.
    """
    from src.services.chat_service import chat_service
    
    request_id = str(uuid.uuid4())
    
    async def generate():
        async for chunk in chat_service.process_query_streaming(
            question=request.question,
            session_id=request.session_id,
            request_id=request_id
        ):
            yield f"data: {chunk}\n\n"
    
    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )


@router.post("/cancel", response_model=CancelResponse, summary="Cancel a running query")
async def cancel_query(request: CancelRequest):
    """
    Cancel a running query by its request ID.
    
    Use the request_id returned from the chat endpoint to cancel a long-running query.
    """
    from src.services.chat_service import ChatService
    
    success = ChatService.cancel_request(request.request_id)
    
    return CancelResponse(
        success=success,
        message="Query cancellation requested" if success else "Request not found or already completed"
    )


# ============================================================================
# SESSION ENDPOINTS
# ============================================================================

@router.post("/sessions", response_model=SessionResponse, summary="Create a new session")
async def create_session(request: SessionCreateRequest = None):
    """
    Create a new chat session.
    
    Sessions allow grouping related conversations and maintaining chat history.
    """
    from src.services.session_service import session_service
    
    session = session_service.create_session(
        title=request.title if request else None
    )
    
    return SessionResponse(**session)


@router.get("/sessions", response_model=List[SessionResponse], summary="List all sessions")
async def list_sessions(limit: int = 50):
    """
    List all chat sessions, ordered by most recent first.
    """
    from src.services.session_service import session_service
    
    sessions = session_service.list_sessions(limit=limit)
    return [SessionResponse(**s) for s in sessions]


@router.get("/sessions/{session_id}", response_model=SessionResponse, summary="Get session details")
async def get_session(session_id: str):
    """
    Get details of a specific session.
    """
    from src.services.session_service import session_service
    
    session = session_service.get_session(session_id)
    
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Session {session_id} not found"
        )
    
    return SessionResponse(**session)


@router.get("/sessions/{session_id}/messages", response_model=SessionMessagesResponse, summary="Get session messages")
async def get_session_messages(session_id: str, limit: int = 100):
    """
    Get all messages in a session.
    """
    from src.services.session_service import session_service
    
    session = session_service.get_session(session_id)
    if not session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Session {session_id} not found"
        )
    
    messages = session_service.get_session_messages(session_id, limit=limit)
    
    return SessionMessagesResponse(
        session_id=session_id,
        messages=[MessageResponse(**m) for m in messages],
        total=len(messages)
    )


@router.delete("/sessions/{session_id}", summary="Delete a session")
async def delete_session(session_id: str):
    """
    Delete a session and all its messages.
    """
    from src.services.session_service import session_service
    
    success = session_service.delete_session(session_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Session {session_id} not found"
        )
    
    return {"message": f"Session {session_id} deleted successfully"}


@router.post("/sessions/{session_id}/clear", summary="Clear session messages")
async def clear_session_messages(session_id: str):
    """
    Clear all messages from a session but keep the session.
    """
    from src.services.session_service import session_service
    
    success = session_service.clear_session_messages(session_id)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Session {session_id} not found"
        )
    
    return {"message": f"Messages cleared from session {session_id}"}


@router.get("/sessions/stats", summary="Get session statistics")
async def get_session_stats():
    """
    Get statistics about sessions and messages.
    """
    from src.services.session_service import session_service
    
    return session_service.get_stats()


# ============================================================================
# CACHE ENDPOINTS
# ============================================================================

@router.get("/cache/stats", response_model=CacheStatsResponse, summary="Get cache statistics")
async def get_cache_stats():
    """
    Get statistics about the query cache.
    """
    from src.services.cache_service import query_cache
    
    stats = query_cache.get_cache_stats()
    return CacheStatsResponse(**stats)


@router.post("/cache/clear", summary="Clear the query cache")
async def clear_cache():
    """
    Clear all cached queries.
    """
    from src.services.cache_service import query_cache
    
    success = query_cache.clear_cache()
    
    if success:
        return {"message": "Cache cleared successfully"}
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to clear cache"
        )


@router.post("/cache/config", summary="Configure cache settings")
async def configure_cache(request: CacheConfigRequest):
    """
    Configure cache settings like similarity threshold.
    """
    from src.services.cache_service import query_cache
    
    if request.similarity_threshold is not None:
        try:
            query_cache.set_similarity_threshold(request.similarity_threshold)
            return {
                "message": f"Similarity threshold updated to {request.similarity_threshold:.2%}",
                "similarity_threshold": request.similarity_threshold
            }
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    
    return {"message": "No configuration changes made"}


# ============================================================================
# VERBOSE MODE CONFIGURATION
# ============================================================================

@router.post("/config/verbose", response_model=VerboseConfigResponse, summary="Toggle verbose logging")
async def configure_verbose(request: VerboseConfigRequest):
    """
    Enable or disable verbose logging mode.
    """
    from src.services.chat_service import ChatService
    
    ChatService.set_verbose(request.enabled)
    
    return VerboseConfigResponse(
        verbose_mode=request.enabled,
        message=f"Verbose logging {'enabled' if request.enabled else 'disabled'}"
    )


@router.get("/config/verbose", response_model=VerboseConfigResponse, summary="Get verbose mode status")
async def get_verbose_status():
    """
    Get the current status of verbose logging mode.
    """
    from src.services.chat_service import ChatService
    
    is_verbose = ChatService.is_verbose()
    
    return VerboseConfigResponse(
        verbose_mode=is_verbose,
        message=f"Verbose logging is {'enabled' if is_verbose else 'disabled'}"
    )


# ============================================================================
# SCHEMA/TABLE ENDPOINTS
# ============================================================================

@router.get("/tables", response_model=List[str], summary="Get allowed tables")
async def get_tables():
    """Get list of allowed tables for querying."""
    from src.services.schema_service import schema_service
    
    return list(schema_service.allowed_tables)


@router.get("/schema", response_model=SchemaResponse, summary="Get database schema")
async def get_schema():
    """Get the current database schema information."""
    from src.services.schema_service import schema_service
    
    return SchemaResponse(
        tables=list(schema_service.allowed_tables),
        schema_info=schema_service.get_schema_dict()
    )


@router.post("/config/tables", summary="Configure allowed tables")
async def configure_tables(request: TableConfigRequest):
    """
    Add or remove tables from the allowed list.
    """
    from src.services.schema_service import schema_service
    
    if request.action == "add":
        success = schema_service.add_allowed_table(request.table_name)
        if success:
            return {"message": f"Table '{request.table_name}' added successfully"}
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Table '{request.table_name}' does not exist in database"
            )
    else:
        success = schema_service.remove_allowed_table(request.table_name)
        if success:
            return {"message": f"Table '{request.table_name}' removed successfully"}
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Table '{request.table_name}' was not in allowed list"
            )
