"""
Research Agent Schemas
=======================
Pydantic models for structured agent input/output.
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Literal


class KeyPoint(BaseModel):
    point: str = Field(description="A key finding or insight")
    importance: str = Field(description="Why this matters")
    confidence: float = Field(default=0.8, ge=0, le=1, description="Confidence 0-1")


class ResearchReport(BaseModel):
    """Structured research output — used with .with_structured_output()"""
    topic: str = Field(description="The research topic")
    title: str = Field(description="Report title")
    summary: str = Field(description="3-5 sentence executive summary")
    key_points: List[KeyPoint] = Field(description="3-5 key findings")
    further_questions: List[str] = Field(description="Follow-up questions")
    sources: Optional[List[str]] = Field(default=None, description="Sources consulted")


class SafetyCheckResult(BaseModel):
    """Output from the safety guard check."""
    is_safe: bool
    risk_level: Literal["none", "low", "medium", "high"]
    reason: str = ""
