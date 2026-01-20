"""
Session Service - ChromaDB-based Chat History & Session Management
===================================================================
Manages chat conversations with persistent storage.

Features:
- Session creation and management
- Chat history storage
- Conversation retrieval
- Session-based context for follow-up questions
"""

import os
import uuid
from typing import Optional, Dict, Any, List
from datetime import datetime
import json

try:
    import chromadb
    CHROMADB_AVAILABLE = True
except ImportError:
    CHROMADB_AVAILABLE = False
    print("⚠️ ChromaDB not installed. Session management will use in-memory storage.")


class SessionService:
    """
    Service for managing chat sessions and history.
    
    Each session has:
    - session_id: Unique identifier
    - title: Auto-generated or user-defined title
    - messages: List of conversation messages
    - created_at: Timestamp
    - updated_at: Timestamp
    """
    
    def __init__(
        self,
        persist_directory: str = "./chroma_sessions"
    ):
        """
        Initialize the session service.
        
        Args:
            persist_directory: Directory to persist session data
        """
        self.enabled = CHROMADB_AVAILABLE
        self.sessions_in_memory: Dict[str, Dict[str, Any]] = {}
        
        if not self.enabled:
            print("⚠️ Session service using in-memory storage")
            return
        
        try:
            # Initialize ChromaDB with the new persistent client API
            os.makedirs(persist_directory, exist_ok=True)
            self.client = chromadb.PersistentClient(path=persist_directory)
            
            # Collection for session metadata
            self.sessions_collection = self.client.get_or_create_collection(
                name="chat_sessions",
                metadata={"description": "Chat session metadata"}
            )
            
            # Collection for chat messages
            self.messages_collection = self.client.get_or_create_collection(
                name="chat_messages",
                metadata={"description": "Chat messages with session context"}
            )
            
            print(f"✅ Session service initialized")
            print(f"   Active sessions: {self.sessions_collection.count()}")
            print(f"   Total messages: {self.messages_collection.count()}")
            
        except Exception as e:
            print(f"❌ Failed to initialize session service: {e}")
            print("   Falling back to in-memory storage")
            self.enabled = False
    
    def create_session(self, title: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new chat session.
        
        Args:
            title: Optional title for the session
            
        Returns:
            Dict with session details
        """
        session_id = str(uuid.uuid4())
        now = datetime.now().isoformat()
        
        session = {
            "session_id": session_id,
            "title": title or f"Chat {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            "created_at": now,
            "updated_at": now,
            "message_count": 0
        }
        
        if self.enabled:
            try:
                self.sessions_collection.add(
                    ids=[session_id],
                    documents=[session["title"]],
                    metadatas=[{
                        "title": session["title"],
                        "created_at": now,
                        "updated_at": now,
                        "message_count": "0"
                    }]
                )
                print(f"✅ Created session: {session_id}")
            except Exception as e:
                print(f"❌ Failed to persist session: {e}")
                self.sessions_in_memory[session_id] = session
        else:
            self.sessions_in_memory[session_id] = {
                **session,
                "messages": []
            }
        
        return session
    
    def get_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """
        Get session details by ID.
        
        Args:
            session_id: The session ID
            
        Returns:
            Session dict or None if not found
        """
        if self.enabled:
            try:
                result = self.sessions_collection.get(
                    ids=[session_id],
                    include=["metadatas", "documents"]
                )
                
                if result and result['ids']:
                    metadata = result['metadatas'][0]
                    return {
                        "session_id": session_id,
                        "title": result['documents'][0],
                        "created_at": metadata.get("created_at"),
                        "updated_at": metadata.get("updated_at"),
                        "message_count": int(metadata.get("message_count", 0))
                    }
                return None
            except Exception as e:
                print(f"❌ Error getting session: {e}")
                return None
        else:
            return self.sessions_in_memory.get(session_id)
    
    def list_sessions(self, limit: int = 50) -> List[Dict[str, Any]]:
        """
        List all sessions, ordered by most recent first.
        
        Args:
            limit: Maximum number of sessions to return
            
        Returns:
            List of session dicts
        """
        if self.enabled:
            try:
                # Get all sessions
                result = self.sessions_collection.get(
                    include=["metadatas", "documents"]
                )
                
                if not result or not result['ids']:
                    return []
                
                sessions = []
                for i, session_id in enumerate(result['ids']):
                    metadata = result['metadatas'][i]
                    sessions.append({
                        "session_id": session_id,
                        "title": result['documents'][i],
                        "created_at": metadata.get("created_at"),
                        "updated_at": metadata.get("updated_at"),
                        "message_count": int(metadata.get("message_count", 0))
                    })
                
                # Sort by updated_at descending
                sessions.sort(key=lambda x: x.get("updated_at", ""), reverse=True)
                return sessions[:limit]
                
            except Exception as e:
                print(f"❌ Error listing sessions: {e}")
                return []
        else:
            sessions = list(self.sessions_in_memory.values())
            sessions.sort(key=lambda x: x.get("updated_at", ""), reverse=True)
            return sessions[:limit]
    
    def add_message(
        self,
        session_id: str,
        role: str,  # 'user' or 'assistant'
        content: str,
        sql: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Add a message to a session.
        
        Args:
            session_id: The session ID
            role: 'user' or 'assistant'
            content: Message content
            sql: Optional SQL query (for assistant messages)
            metadata: Optional additional metadata
            
        Returns:
            The created message dict
        """
        message_id = str(uuid.uuid4())
        now = datetime.now().isoformat()
        
        message = {
            "message_id": message_id,
            "session_id": session_id,
            "role": role,
            "content": content,
            "sql": sql,
            "timestamp": now,
            "metadata": metadata or {}
        }
        
        if self.enabled:
            try:
                # Add message to messages collection
                self.messages_collection.add(
                    ids=[message_id],
                    documents=[content],
                    metadatas=[{
                        "session_id": session_id,
                        "role": role,
                        "sql": sql or "",
                        "timestamp": now,
                        "metadata_json": json.dumps(metadata or {})
                    }]
                )
                
                # Update session's updated_at and message_count
                session = self.get_session(session_id)
                if session:
                    new_count = session.get("message_count", 0) + 1
                    # Update title if first user message and title is default
                    new_title = session["title"]
                    if role == "user" and new_count == 1:
                        # Use first 50 chars of first user message as title
                        new_title = content[:50] + ("..." if len(content) > 50 else "")
                    
                    self.sessions_collection.update(
                        ids=[session_id],
                        documents=[new_title],
                        metadatas=[{
                            "title": new_title,
                            "created_at": session["created_at"],
                            "updated_at": now,
                            "message_count": str(new_count)
                        }]
                    )
                
                print(f"💬 Added {role} message to session {session_id[:8]}...")
                
            except Exception as e:
                print(f"❌ Failed to persist message: {e}")
        else:
            if session_id in self.sessions_in_memory:
                self.sessions_in_memory[session_id]["messages"].append(message)
                self.sessions_in_memory[session_id]["updated_at"] = now
                self.sessions_in_memory[session_id]["message_count"] += 1
                
                # Update title on first user message
                if role == "user" and len(self.sessions_in_memory[session_id]["messages"]) == 1:
                    self.sessions_in_memory[session_id]["title"] = content[:50] + ("..." if len(content) > 50 else "")
        
        return message
    
    def get_session_messages(
        self,
        session_id: str,
        limit: int = 100
    ) -> List[Dict[str, Any]]:
        """
        Get all messages for a session.
        
        Args:
            session_id: The session ID
            limit: Maximum number of messages to return
            
        Returns:
            List of message dicts, ordered by timestamp
        """
        if self.enabled:
            try:
                # Query messages by session_id
                result = self.messages_collection.get(
                    where={"session_id": session_id},
                    include=["metadatas", "documents"]
                )
                
                if not result or not result['ids']:
                    return []
                
                messages = []
                for i, message_id in enumerate(result['ids']):
                    metadata = result['metadatas'][i]
                    messages.append({
                        "message_id": message_id,
                        "session_id": session_id,
                        "role": metadata.get("role"),
                        "content": result['documents'][i],
                        "sql": metadata.get("sql") or None,
                        "timestamp": metadata.get("timestamp"),
                        "metadata": json.loads(metadata.get("metadata_json", "{}"))
                    })
                
                # Sort by timestamp
                messages.sort(key=lambda x: x.get("timestamp", ""))
                return messages[:limit]
                
            except Exception as e:
                print(f"❌ Error getting messages: {e}")
                return []
        else:
            session = self.sessions_in_memory.get(session_id)
            if session:
                return session.get("messages", [])[:limit]
            return []
    
    def get_recent_context(
        self,
        session_id: str,
        num_messages: int = 6
    ) -> str:
        """
        Get recent conversation context for follow-up questions.
        
        Args:
            session_id: The session ID
            num_messages: Number of recent messages to include
            
        Returns:
            Formatted context string
        """
        messages = self.get_session_messages(session_id, limit=num_messages)
        
        if not messages:
            return ""
        
        context_parts = []
        for msg in messages[-num_messages:]:
            role = "User" if msg["role"] == "user" else "Assistant"
            content = msg["content"][:200] + "..." if len(msg["content"]) > 200 else msg["content"]
            context_parts.append(f"{role}: {content}")
        
        return "\n".join(context_parts)
    
    def delete_session(self, session_id: str) -> bool:
        """
        Delete a session and all its messages.
        
        Args:
            session_id: The session ID to delete
            
        Returns:
            True if deleted successfully
        """
        if self.enabled:
            try:
                # Delete all messages for this session
                messages = self.get_session_messages(session_id, limit=10000)
                if messages:
                    message_ids = [m["message_id"] for m in messages]
                    self.messages_collection.delete(ids=message_ids)
                
                # Delete the session
                self.sessions_collection.delete(ids=[session_id])
                print(f"🗑️ Deleted session: {session_id}")
                return True
                
            except Exception as e:
                print(f"❌ Error deleting session: {e}")
                return False
        else:
            if session_id in self.sessions_in_memory:
                del self.sessions_in_memory[session_id]
                return True
            return False
    
    def clear_session_messages(self, session_id: str) -> bool:
        """
        Clear all messages from a session (keep the session).
        
        Args:
            session_id: The session ID
            
        Returns:
            True if cleared successfully
        """
        if self.enabled:
            try:
                # Delete all messages for this session
                messages = self.get_session_messages(session_id, limit=10000)
                if messages:
                    message_ids = [m["message_id"] for m in messages]
                    self.messages_collection.delete(ids=message_ids)
                
                # Reset message count
                session = self.get_session(session_id)
                if session:
                    self.sessions_collection.update(
                        ids=[session_id],
                        metadatas=[{
                            "title": session["title"],
                            "created_at": session["created_at"],
                            "updated_at": datetime.now().isoformat(),
                            "message_count": "0"
                        }]
                    )
                
                print(f"🧹 Cleared messages for session: {session_id}")
                return True
                
            except Exception as e:
                print(f"❌ Error clearing session messages: {e}")
                return False
        else:
            if session_id in self.sessions_in_memory:
                self.sessions_in_memory[session_id]["messages"] = []
                self.sessions_in_memory[session_id]["message_count"] = 0
                return True
            return False
    
    def get_stats(self) -> Dict[str, Any]:
        """Get session service statistics."""
        if self.enabled:
            try:
                return {
                    "enabled": True,
                    "storage": "chromadb",
                    "total_sessions": self.sessions_collection.count(),
                    "total_messages": self.messages_collection.count()
                }
            except Exception as e:
                return {"enabled": True, "error": str(e)}
        else:
            return {
                "enabled": True,
                "storage": "in_memory",
                "total_sessions": len(self.sessions_in_memory),
                "total_messages": sum(
                    len(s.get("messages", [])) 
                    for s in self.sessions_in_memory.values()
                )
            }


# Singleton instance
session_service = SessionService()
