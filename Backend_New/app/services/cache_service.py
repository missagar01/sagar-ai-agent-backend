"""
Cache Service - ChromaDB-based Query Caching
=============================================
Semantic similarity caching for SQL queries.
"""

import os
import hashlib
from typing import Optional, Dict, Any
from datetime import datetime

try:
    import chromadb
    CHROMADB_AVAILABLE = True
except ImportError:
    CHROMADB_AVAILABLE = False
    print("⚠️ ChromaDB not installed. Query caching disabled.")


class QueryCacheService:
    """Semantic query cache using ChromaDB"""
    
    def __init__(
        self,
        persist_directory: str = "./chroma_cache",
        collection_name: str = "query_cache",
        similarity_threshold: float = 0.92  # High threshold to prevent false matches (completed vs all)
    ):
        self.similarity_threshold = similarity_threshold
        self.enabled = CHROMADB_AVAILABLE
        self.cache_hits = 0
        self.cache_misses = 0
        
        if not self.enabled:
            return
        
        try:
            os.makedirs(persist_directory, exist_ok=True)
            self.client = chromadb.PersistentClient(path=persist_directory)
            self.collection = self.client.get_or_create_collection(
                name=collection_name,
                metadata={"description": "SQL query cache"}
            )
            print(f"✅ Cache initialized. Threshold: {similarity_threshold * 100}%, Entries: {self.collection.count()}")
        except Exception as e:
            print(f"❌ Cache init failed: {e}")
            self.enabled = False
    
    def _generate_id(self, question: str) -> str:
        """Generate unique ID from question"""
        return hashlib.md5(question.lower().strip().encode()).hexdigest()
    
    def find_similar_query(self, question: str, db_name: str = "checklist") -> Optional[Dict[str, Any]]:
        """Find cached query with semantic similarity"""
        if not self.enabled:
            return None
        
        try:
            results = self.collection.query(
                query_texts=[question.lower().strip()],
                n_results=1,
                include=["documents", "metadatas", "distances"],
                where={"database": db_name}
            )
            
            if not results or not results['documents'] or not results['documents'][0]:
                return None
            
            # Convert L2 distance to similarity
            distance = results['distances'][0][0]
            similarity = 1 / (1 + distance)
            
            if similarity >= self.similarity_threshold:
                metadata = results['metadatas'][0][0]
                cached_question = results['documents'][0][0]
                
                self.cache_hits += 1
                print(f"🎯 CACHE HIT! Similarity: {similarity:.2%}")
                print(f"   Cached: '{cached_question[:50]}...'")
                print(f"   Current: '{question[:50]}...'")
                
                return {
                    "cached_question": cached_question,
                    "sql": metadata.get("sql"),
                    "similarity": similarity,
                    "cached_at": metadata.get("cached_at"),
                    "hit_count": int(metadata.get("hit_count", 0)) + 1
                }
            else:
                self.cache_misses += 1
                print(f"📭 Cache miss. Similarity: {similarity:.2%}")
                return None
                
        except Exception as e:
            print(f"❌ Cache lookup error: {e}")
            return None
    
    def cache_query(self, question: str, sql: str, db_name: str = "checklist", language: str = "english") -> bool:
        """Cache question-SQL mapping"""
        if not self.enabled:
            return False
        
        try:
            # Generate ID specific to this database context
            doc_id = self._generate_id(f"{db_name}:{question}")
            existing = self.collection.get(ids=[doc_id])
            
            metadata = {
                "sql": sql,
                "language": language,
                "database": db_name,
                "cached_at": datetime.now().isoformat(),
                "hit_count": "0"
            }
            
            if existing and existing['ids']:
                self.collection.update(
                    ids=[doc_id],
                    documents=[question.lower().strip()],
                    metadatas=[metadata]
                )
                print(f"📝 Cache updated: '{question[:50]}...'")
            else:
                self.collection.add(
                    ids=[doc_id],
                    documents=[question.lower().strip()],
                    metadatas=[metadata]
                )
                print(f"💾 Cached: '{question[:50]}...'")
            
            return True
        except Exception as e:
            print(f"❌ Cache write error: {e}")
            return False
    
    def invalidate(self, question: str, db_name: str = "checklist") -> bool:
        """Remove cached query"""
        if not self.enabled:
            return False
        
        try:
            doc_id = self._generate_id(f"{db_name}:{question}")
            self.collection.delete(ids=[doc_id])
            print(f"🗑️ Cache invalidated: '{question[:50]}...'")
            return True
        except Exception as e:
            print(f"❌ Cache invalidation error: {e}")
            return False
    
    def get_stats(self) -> Dict[str, Any]:
        """Get cache statistics"""
        if not self.enabled:
            return {"total_queries": 0, "enabled": False}
        
        total_requests = self.cache_hits + self.cache_misses
        hit_rate = (self.cache_hits / total_requests * 100) if total_requests > 0 else 0.0
        
        return {
            "total_queries": self.collection.count(),
            "enabled": True,
            "threshold": self.similarity_threshold,
            "cache_hits": self.cache_hits,
            "cache_misses": self.cache_misses,
            "hit_rate": hit_rate
        }
    
    def clear(self) -> bool:
        """Clear all cache"""
        if not self.enabled:
            return False
        
        try:
            self.client.delete_collection(self.collection.name)
            self.collection = self.client.get_or_create_collection(
                name=self.collection.name,
                metadata={"description": "SQL query cache"}
            )
            print("🧹 Cache cleared")
            return True
        except Exception as e:
            print(f"❌ Cache clear error: {e}")
            return False


# Global instance
query_cache = QueryCacheService()
