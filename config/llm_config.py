"""
LLM Model Configuration
========================
Centralized configuration for all LLM providers used in the course.
Import this to get pre-configured model instances.

Usage:
    from config.llm_config import get_groq_llm, get_openai_llm, get_gemini_llm
    llm = get_groq_llm()  # Ready to use!
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv("config/.env")
load_dotenv()  # Also check root .env


def get_groq_llm(model: str = None, temperature: float = 0.7, max_tokens: int = 1000):
    """Get a configured Groq LLM instance for LangGraph.

    Args:
        model: Model name (default: from env or llama-3.3-70b-versatile)
        temperature: Creativity level 0-1 (default: 0.7)
        max_tokens: Max response length (default: 1000)
    """
    from langchain_groq import ChatGroq

    return ChatGroq(
        model=model or os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
        temperature=temperature,
        max_tokens=max_tokens,
    )


def get_openai_llm(model: str = None, temperature: float = 0.7, max_tokens: int = 1000):
    """Get a configured OpenAI LLM instance for LangGraph.

    Args:
        model: Model name (default: from env or gpt-4o-mini)
        temperature: Creativity level 0-1 (default: 0.7)
        max_tokens: Max response length (default: 1000)
    """
    from langchain_openai import ChatOpenAI

    return ChatOpenAI(
        model=model or os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=temperature,
        max_tokens=max_tokens,
    )


def get_gemini_llm(model: str = None, temperature: float = 0.7):
    """Get a configured Gemini LLM instance for ADK/LangChain.

    Args:
        model: Model name (default: from env or gemini-2.0-flash)
        temperature: Creativity level 0-1 (default: 0.7)
    """
    from langchain_google_genai import ChatGoogleGenerativeAI

    return ChatGoogleGenerativeAI(
        model=model or os.getenv("GOOGLE_MODEL", "gemini-2.0-flash"),
        temperature=temperature,
    )


def get_anthropic_llm(model: str = None, temperature: float = 0.7, max_tokens: int = 1000):
    """Get a configured Anthropic LLM instance.

    Args:
        model: Model name (default: from env or claude-3-5-sonnet)
        temperature: Creativity level 0-1 (default: 0.7)
        max_tokens: Max response length (default: 1000)
    """
    from langchain_anthropic import ChatAnthropic

    return ChatAnthropic(
        model=model or os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022"),
        temperature=temperature,
        max_tokens=max_tokens,
    )


# Quick access dictionary
MODELS = {
    "groq": get_groq_llm,
    "openai": get_openai_llm,
    "gemini": get_gemini_llm,
    "anthropic": get_anthropic_llm,
}
