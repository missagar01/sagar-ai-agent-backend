"""
Cache Service - ChromaDB-based Query Caching
=============================================
Provides semantic similarity caching for SQL queries.
Avoids redundant LLM calls for similar questions.

Features:
- Semantic similarity matching (90% threshold by default)
- Stores question -> SQL mappings
- Automatic cache invalidation options
"""

import os
import hashlib
from typing import Optional, Dict, Any, List, Tuple
from datetime import datetime
import json

try:
    import chromadb
    CHROMADB_AVAILABLE = True
except ImportError:
    CHROMADB_AVAILABLE = False
    print("⚠️ ChromaDB not installed. Query caching disabled.")


class QueryCacheService:
    """
    Service for caching SQL queries based on semantic similarity.
    
    Uses ChromaDB for vector storage and similarity search.
    """
    
    def __init__(
        self,
        persist_directory: str = "./chroma_cache",
        collection_name: str = "query_cache",
        similarity_threshold: float = 0.90  # 90% similarity
    ):
        """
        Initialize the cache service.
        
        Args:
            persist_directory: Directory to persist ChromaDB data
            collection_name: Name of the collection for query cache
            similarity_threshold: Minimum similarity score (0.0 to 1.0) for cache hit
        """
        self.similarity_threshold = similarity_threshold
        self.enabled = CHROMADB_AVAILABLE
        
        if not self.enabled:
            print("⚠️ Cache service disabled - ChromaDB not available")
            return
        
        try:
            # Initialize ChromaDB with the new persistent client API
            os.makedirs(persist_directory, exist_ok=True)
            self.client = chromadb.PersistentClient(path=persist_directory)
            
            # Get or create the cache collection
            # Using default embedding function (sentence-transformers)
            self.collection = self.client.get_or_create_collection(
                name=collection_name,
                metadata={"description": "SQL query cache for semantic similarity"}
            )
            
            print(f"✅ Cache service initialized. Collection: {collection_name}")
            print(f"   Similarity threshold: {similarity_threshold * 100}%")
            print(f"   Current cache size: {self.collection.count()} entries")
            
        except Exception as e:
            print(f"❌ Failed to initialize cache service: {e}")
            self.enabled = False
    
    def _generate_id(self, question: str) -> str:
        """Generate a unique ID for a question."""
        return hashlib.md5(question.lower().strip().encode()).hexdigest()
    
    def find_similar_query(self, question: str) -> Optional[Dict[str, Any]]:
        """
        Find a cached query with similar semantics.
        
        Args:
            question: The user's question
            
        Returns:
            Dict with cached SQL and metadata if found, None otherwise
        """
        if not self.enabled:
            return None
        
        try:
            # Search for similar queries
            results = self.collection.query(
                query_texts=[question.lower().strip()],
                n_results=1,  # Get the best match
                include=["documents", "metadatas", "distances"]
            )
            
            if not results or not results['documents'] or not results['documents'][0]:
                return None
            
            # ChromaDB returns L2 distance, convert to similarity
            # Lower distance = higher similarity
            # Similarity = 1 / (1 + distance) for L2
            distance = results['distances'][0][0]
            similarity = 1 / (1 + distance)
            
            if similarity >= self.similarity_threshold:
                metadata = results['metadatas'][0][0]
                cached_question = results['documents'][0][0]
                
                print(f"🎯 CACHE HIT! Similarity: {similarity:.2%}")
                print(f"   Original: '{cached_question[:50]}...'")
                print(f"   Current:  '{question[:50]}...'")
                
                return {
                    "cached_question": cached_question,
                    "sql": metadata.get("sql"),
                    "similarity": similarity,
                    "cached_at": metadata.get("cached_at"),
                    "hit_count": int(metadata.get("hit_count", 0)) + 1
                }
            else:
                print(f"📭 Cache miss. Best similarity: {similarity:.2%} (threshold: {self.similarity_threshold:.2%})")
                return None
                
        except Exception as e:
            print(f"❌ Cache lookup error: {e}")
            return None
    
    def cache_query(
        self,
        question: str,
        sql: str,
        intent_analysis: str = "",
        language: str = "english"
    ) -> bool:
        """
        Cache a question-SQL mapping.
        
        Args:
            question: The user's question
            sql: The generated SQL query
            intent_analysis: Optional intent analysis JSON
            language: Detected language
            
        Returns:
            True if cached successfully, False otherwise
        """
        if not self.enabled:
            return False
        
        try:
            doc_id = self._generate_id(question)
            
            # Check if this exact question already exists
            existing = self.collection.get(ids=[doc_id])
            
            metadata = {
                "sql": sql,
                "intent_analysis": intent_analysis,
                "language": language,
                "cached_at": datetime.now().isoformat(),
                "hit_count": "0"
            }
            
            if existing and existing['ids']:
                # Update existing entry
                self.collection.update(
                    ids=[doc_id],
                    documents=[question.lower().strip()],
                    metadatas=[metadata]
                )
                print(f"📝 Cache updated for question: '{question[:50]}...'")
            else:
                # Add new entry
                self.collection.add(
                    ids=[doc_id],
                    documents=[question.lower().strip()],
                    metadatas=[metadata]
                )
                print(f"💾 Cached new query: '{question[:50]}...'")
            
            return True
            
        except Exception as e:
            print(f"❌ Cache write error: {e}")
            return False
    
    def update_hit_count(self, question: str) -> None:
        """Update the hit count for a cached query."""
        if not self.enabled:
            return
        
        try:
            doc_id = self._generate_id(question)
            existing = self.collection.get(ids=[doc_id], include=["metadatas"])
            
            if existing and existing['ids']:
                metadata = existing['metadatas'][0]
                metadata['hit_count'] = str(int(metadata.get('hit_count', 0)) + 1)
                self.collection.update(ids=[doc_id], metadatas=[metadata])
        except Exception:
            pass
    
    def clear_cache(self) -> bool:
        """Clear all cached queries."""
        if not self.enabled:
            return False
        
        try:
            # Delete and recreate the collection
            self.client.delete_collection(self.collection.name)
            self.collection = self.client.get_or_create_collection(
                name="query_cache",
                metadata={"description": "SQL query cache for semantic similarity"}
            )
            print("🗑️ Cache cleared successfully")
            return True
        except Exception as e:
            print(f"❌ Failed to clear cache: {e}")
            return False
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """Get cache statistics."""
        if not self.enabled:
            return {"enabled": False}
        
        try:
            count = self.collection.count()
            return {
                "enabled": True,
                "total_entries": count,
                "similarity_threshold": self.similarity_threshold
            }
        except Exception as e:
            return {"enabled": True, "error": str(e)}
    
    def set_similarity_threshold(self, threshold: float) -> None:
        """
        Update the similarity threshold.
        
        Args:
            threshold: New threshold (0.0 to 1.0)
        """
        if 0.0 <= threshold <= 1.0:
            self.similarity_threshold = threshold
            print(f"📊 Similarity threshold updated to: {threshold:.2%}")
        else:
            raise ValueError("Threshold must be between 0.0 and 1.0")


# Singleton instance
query_cache = QueryCacheService()
