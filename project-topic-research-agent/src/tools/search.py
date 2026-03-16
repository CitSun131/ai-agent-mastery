"""
Web Search Tool
================
Provides web search capability for the research agent.
Add your preferred search API key to config/.env.

Week 3+: Used by the agent for real-time information retrieval.
"""

import requests
from langchain_core.tools import tool


@tool
def search_web(query: str, max_results: int = 5) -> str:
    """Search the web for information about a topic.

    Args:
        query: The search query string
        max_results: Maximum results to return (default: 5)

    Returns:
        Search results as formatted text
    """
    # TODO (Week 3): Replace with real search API (Tavily, SerpAPI, or Brave)
    # For now, returns a placeholder
    return f"[Search placeholder] Results for: '{query}' (implement real search in Week 3)"
