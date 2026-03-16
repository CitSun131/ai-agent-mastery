"""
Project Settings
=================
Centralized configuration for the Topic Research Agent.
"""

import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Agent configuration loaded from environment variables."""

    # Provider Selection (groq, openai, google, anthropic)
    llm_provider: str = "groq"

    # LLM Configuration
    groq_api_key: str = ""
    groq_model: str = "llama-3.3-70b-versatile"
    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"
    google_api_key: str = ""
    google_model: str = "gemini-3-flash-preview"

    # Agent Behavior
    max_iterations: int = 10
    max_tokens_per_call: int = 2000
    temperature: float = 0.7

    # Cost Management
    weekly_budget_usd: float = 5.00
    session_token_limit: int = 50000

    # Phoenix
    phoenix_port: int = 6006
    tracing_enabled: bool = True

    class Config:
        env_file = "config/.env"
        env_file_encoding = "utf-8"


# Singleton instance
settings = Settings()
