"""
LangGraph Implementation — Topic Research Agent
=================================================
Week 1: Basic summarizer with tracing
(Evolves each week — see git history for progression)
"""

from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from typing import TypedDict, Annotated, Optional, List
from langgraph.graph import add_messages
import os


class ResearchState(TypedDict):
    """Agent state — grows more complex each week."""
    messages: Annotated[list, add_messages]
    topic: str
    raw_research: str
    structured_output: Optional[dict]
    iteration: int


def create_research_agent():
    """Build and return the LangGraph research agent."""

    provider = os.getenv("LLM_PROVIDER", "groq").lower()
    if provider == "groq":
        llm = ChatGroq(
            model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
            temperature=0.7,
        )
    else:
        llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            temperature=0.7,
        )

    def research_node(state: ResearchState) -> dict:
        """Generate research about the topic."""
        prompt = f"""You are a research analyst. Provide a comprehensive summary of
the following topic. Include key facts, current trends, and important considerations.
Structure your response with: Title, Summary, Key Points, and Follow-up Questions.

Topic: {state['topic']}"""

        response = llm.invoke(prompt)
        return {
            "raw_research": response.content,
            "iteration": state.get("iteration", 0) + 1,
        }

    def format_node(state: ResearchState) -> dict:
        """Format raw research into structured output."""
        return {
            "structured_output": {
                "topic": state["topic"],
                "research": state["raw_research"],
                "iteration": state["iteration"],
            }
        }

    # Build the graph
    graph = StateGraph(ResearchState)
    graph.add_node("research", research_node)
    graph.add_node("format", format_node)
    graph.set_entry_point("research")
    graph.add_edge("research", "format")
    graph.add_edge("format", END)

    return graph.compile()


def run_research(topic: str) -> dict:
    """Run the research agent on a given topic.

    Args:
        topic: The research topic to investigate

    Returns:
        Structured research output
    """
    agent = create_research_agent()

    result = agent.invoke({
        "messages": [],
        "topic": topic,
        "raw_research": "",
        "structured_output": None,
        "iteration": 0,
    })

    return result.get("structured_output", {})
