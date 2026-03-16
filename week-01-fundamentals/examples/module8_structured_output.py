"""
Module 8: Structured Output — Getting Reliable Data from LLMs
===============================================================
Demonstrates two methods for structured output:
  1. JSON Mode — forces the LLM to return valid JSON
  2. Pydantic Models — type-safe, validated structured output (recommended)

Run: python week-01-fundamentals/examples/module8_structured_output.py
"""

import os
import json
from dotenv import load_dotenv

load_dotenv("config/.env")
load_dotenv()

from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel, Field
from typing import List


# ──────────────────────────────────────────────
# Method 1: JSON Mode
# ──────────────────────────────────────────────
def demo_json_mode():
    print("=" * 50)
    print("Method 1: JSON Mode")
    print("=" * 50)

    provider = os.getenv("LLM_PROVIDER", "groq").lower()
    if provider == "groq":
        from langchain_groq import ChatGroq
        llm = ChatGroq(
            model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
            model_kwargs={"response_format": {"type": "json_object"}},
        )
    else:
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            model_kwargs={"response_format": {"type": "json_object"}},
        )

    response = llm.invoke([
        SystemMessage(content="Always respond in JSON format."),
        HumanMessage(
            content="Give me 3 facts about AI agents. "
                    "Return as JSON with a 'facts' array."
        ),
    ])

    data = json.loads(response.content)
    print("Parsed JSON response:")
    for fact in data["facts"]:
        print(f"  - {fact}")
    print()


# ──────────────────────────────────────────────
# Method 2: Pydantic Models (Recommended)
# ──────────────────────────────────────────────
class ResearchFinding(BaseModel):
    """A single research finding."""
    title: str = Field(description="Short title of the finding")
    summary: str = Field(description="2-3 sentence summary")
    confidence: float = Field(description="Confidence score 0-1")


class ResearchReport(BaseModel):
    """Structured research report."""
    topic: str
    findings: List[ResearchFinding]
    conclusion: str


def demo_pydantic_output():
    print("=" * 50)
    print("Method 2: Pydantic Structured Output")
    print("=" * 50)

    provider = os.getenv("LLM_PROVIDER", "groq").lower()
    if provider == "groq":
        from langchain_groq import ChatGroq
        llm = ChatGroq(model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"))
    else:
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"))

    structured_llm = llm.with_structured_output(ResearchReport)

    result = structured_llm.invoke(
        "Research the benefits of AI agents in healthcare"
    )

    # result is a typed ResearchReport object!
    print(f"Topic: {result.topic}")
    for f in result.findings:
        print(f"  - {f.title} (confidence: {f.confidence})")
        print(f"    {f.summary}")
    print(f"Conclusion: {result.conclusion}")
    print()


if __name__ == "__main__":
    provider = os.getenv("LLM_PROVIDER", "groq").lower()
    print(f"Provider: {provider}\n")

    demo_json_mode()
    demo_pydantic_output()
