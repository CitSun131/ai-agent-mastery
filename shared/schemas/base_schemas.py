"""
Base Pydantic Schemas
======================
Shared data models used across the curriculum.
These schemas ensure structured, validated output from LLM calls.
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime


class KeyPoint(BaseModel):
    """A single key finding or insight."""
    point: str = Field(description="A concise key point")
    importance: str = Field(description="Why this point matters")
    confidence: float = Field(default=0.8, description="Confidence score 0-1", ge=0, le=1)


class ResearchSummary(BaseModel):
    """Structured output for a research query."""
    topic: str = Field(description="The research topic")
    title: str = Field(description="A concise report title")
    summary: str = Field(description="3-5 sentence executive summary")
    key_points: List[KeyPoint] = Field(description="3-5 key findings")
    further_questions: List[str] = Field(description="Follow-up research questions")
    sources_consulted: Optional[List[str]] = Field(default=None, description="Sources used")


class AgentResponse(BaseModel):
    """Standard response format for all agents."""
    status: Literal["success", "error", "partial"] = Field(description="Execution status")
    message: str = Field(description="Human-readable response")
    data: Optional[dict] = Field(default=None, description="Structured data payload")
    tokens_used: Optional[int] = Field(default=None, description="Total tokens consumed")
    cost_usd: Optional[float] = Field(default=None, description="Estimated cost in USD")
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())


class ToolCallRecord(BaseModel):
    """Record of a single tool call by the agent."""
    tool_name: str
    arguments: dict
    result: str
    duration_ms: float
    success: bool


class AgentTrace(BaseModel):
    """Complete trace of an agent execution."""
    agent_name: str
    query: str
    iterations: int
    tool_calls: List[ToolCallRecord] = Field(default_factory=list)
    final_response: str
    total_tokens: int
    total_cost_usd: float
    total_duration_s: float
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
