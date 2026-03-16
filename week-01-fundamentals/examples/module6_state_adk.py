"""
Module 6: State Management — ADK Session Memory
=================================================
Demonstrates how ADK maintains state across conversation turns
within a session. The agent remembers the user's name and uses
it in subsequent interactions — all handled automatically by ADK.

Requires: GOOGLE_API_KEY in your environment.

Run: python week-01-fundamentals/examples/module6_state_adk.py
"""

import asyncio
import os
from dotenv import load_dotenv

load_dotenv("config/.env")
load_dotenv()

from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# ADK agents automatically maintain conversation history within a session.
# No manual state wiring needed — unlike LangGraph where you define TypedDict.
memory_agent = LlmAgent(
    name="memory_agent",
    model=os.getenv("GOOGLE_MODEL", "gemini-3-flash-preview"),
    instruction="""You are a helpful agent that remembers everything
    the user tells you. If the user shares their name, remember it.
    Always greet them by name in future turns.""",
)

session_service = InMemorySessionService()
runner = Runner(
    agent=memory_agent,
    app_name="memory_app",
    session_service=session_service,
)


async def chat_with_memory():
    # Create one session — ADK persists memory across turns within it
    session = await session_service.create_session(
        app_name="memory_app", user_id="user1"
    )

    # Turn 1: Tell the agent your name
    print("User: Hi! My name is Alex.")
    async for event in runner.run_async(
        user_id="user1",
        session_id=session.id,
        new_message=types.Content(role="user", parts=[types.Part(text="Hi! My name is Alex.")]),
    ):
        if event.is_final_response():
            print(f"Agent: {event.content.parts[0].text}")

    print()

    # Turn 2: Ask if it remembers (same session = same memory)
    print("User: What is my name?")
    async for event in runner.run_async(
        user_id="user1",
        session_id=session.id,
        new_message=types.Content(role="user", parts=[types.Part(text="What is my name?")]),
    ):
        if event.is_final_response():
            print(f"Agent: {event.content.parts[0].text}")
    # The agent should remember 'Alex'!


if __name__ == "__main__":
    print("ADK Session Memory Demo")
    print("=" * 50)
    asyncio.run(chat_with_memory())
