"""
Application Configuration
=========================
Central configuration for the FastAPI application
"""

from pydantic_settings import BaseSettings
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "DB Assistant API"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # LLM Settings (Using OpenAI GPT)
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    LLM_MODEL: str = os.getenv("MODEL_NAME", "gpt-4o-mini")  # OpenAI GPT-4o-mini
    LLM_TEMPERATURE: float = 0.0
    
    # Database Settings
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_USER: str = os.getenv("DB_USER", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_NAME: str = os.getenv("DB_NAME", "")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    
    # ────────────────────────────────────────────────────────
    # MULTI-DATABASE URLS
    # ────────────────────────────────────────────────────────
    
    # 1. Checklist System
    DB_CHECKLIST_URL: str = os.getenv(
        "DB_CHECKLIST_URL", 
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )

    # 2. Lead-To-Order System (New)
    DB_LEAD_TO_ORDER_URL: str = os.getenv("DB_LEAD_TO_ORDER_URL", "")
    
    @property
    def DATABASE_URL(self) -> str:
        """Default Connection (Legacy Support)"""
        return self.DB_CHECKLIST_URL
    
    # Security Settings
    MAX_QUERY_LENGTH: int = 50000
    MAX_RESULT_ROWS: int = 200
    ALLOWED_TABLES: List[str] = ["users", "checklist", "delegation"]
    
    # Validation Settings
    MAX_VALIDATION_ATTEMPTS: int = 3
    CONFIDENCE_THRESHOLD: int = 70  # Auto-execute queries with confidence >= 70%
    
    # Metadata Settings
    METADATA_FILE: str = "metadata.json"
    
    # Session Settings
    SESSION_DB_PATH: str = "chat_sessions.db"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
