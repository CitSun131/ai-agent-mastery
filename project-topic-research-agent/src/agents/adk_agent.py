"""
ADK Implementation — Topic Research Agent
===========================================
Week 1: Basic summarizer with tracing
(Evolves each week — see git history for progression)
"""

from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
import os


def create_research_agent():
    """Build and return the ADK research agent."""

    agent = LlmAgent(
        name="topic_researcher",
        model=os.getenv("GOOGLE_MODEL", "gemini-3-flash-preview"),
        instruction="""You are an expert research analyst. When given a topic:

1. Provide a comprehensive summary with key facts and current trends
2. List 3-5 key points, each with its importance
3. Suggest 2-3 follow-up questions for deeper research
4. Note any areas of uncertainty or debate

Structure your response clearly with headers for each section.
Be factual and balanced in your analysis.""",
    )

    return agent


async def run_research(topic: str) -> str:
    """Run the ADK research agent on a given topic.

    Args:
        topic: The research topic to investigate

    Returns:
        Research output as text
    """
    agent = create_research_agent()
    session_service = InMemorySessionService()

    runner = Runner(
        agent=agent,
        app_name="topic_research",
        session_service=session_service,
    )

    session = await session_service.create_session(
        app_name="topic_research",
        user_id="researcher",
    )

    result_text = ""
    async for event in runner.run_async(
        user_id="researcher",
        session_id=session.id,
        new_message=types.Content(
            role="user",
            parts=[types.Part(text=f"Research this topic thoroughly: {topic}")],
        ),
    ):
        if event.is_final_response():
            result_text = event.content.parts[0].text

    return result_text
