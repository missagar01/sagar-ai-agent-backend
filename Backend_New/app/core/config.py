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
    
    # OpenAI Settings
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = "gpt-4o"
    OPENAI_TEMPERATURE: float = 0.0
    
    # Database Settings
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_USER: str = os.getenv("DB_USER", "")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_NAME: str = os.getenv("DB_NAME", "")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    # Security Settings
    MAX_QUERY_LENGTH: int = 50000
    MAX_RESULT_ROWS: int = 200
    ALLOWED_TABLES: List[str] = ["users", "checklist", "delegation"]
    
    # Validation Settings
    MAX_VALIDATION_ATTEMPTS: int = 3
    
    # Session Settings
    SESSION_DB_PATH: str = "chat_sessions.db"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
