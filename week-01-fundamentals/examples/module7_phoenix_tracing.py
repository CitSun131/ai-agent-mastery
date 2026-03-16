"""
Module 7: Observability — Traced Weather Agent with Phoenix
=============================================================
Runs the weather tool agent from Module 5 WITH Phoenix tracing active.
Open http://localhost:6006 after running to see:
  - Each LLM call as a span (input prompt, output, latency, tokens)
  - Tool calls as child spans (which tool, what it returned)
  - The full agent loop as a trace

Run: python week-01-fundamentals/examples/module7_phoenix_tracing.py
"""

import os
import sys
import warnings
from dotenv import load_dotenv

load_dotenv("config/.env")
load_dotenv()

# Suppress SQLAlchemy reflection warnings from Phoenix
warnings.filterwarnings("ignore", message=".*Skipped unsupported reflection.*")

# Fix Windows console encoding for Phoenix emoji output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ── Step 1: Launch Phoenix and instrument LangChain ──

import phoenix as px
from openinference.instrumentation.langchain import LangChainInstrumentor
from phoenix.otel import register

px.launch_app()
tracer_provider = register()
LangChainInstrumentor().instrument(tracer_provider=tracer_provider)

print("[OK] Phoenix tracing is active!")
print("Dashboard: http://localhost:6006\n")

# ── Step 2: Build the weather agent (same as Module 5) ──

import requests
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from typing import TypedDict, Annotated
from langgraph.graph import add_messages


@tool
def get_weather(city: str) -> str:
    """Get the current weather for a city using a free API."""
    response = requests.get(f"https://wttr.in/{city}?format=%t+%C", timeout=10)
    if response.status_code == 200:
        return f"Weather in {city}: {response.text.strip()}"
    return f"Could not fetch weather for {city}"


@tool
def get_time(timezone: str) -> str:
    """Get the current time for a timezone. Use IANA format like America/New_York, Asia/Tokyo, Europe/London."""
    from datetime import datetime
    import pytz

    try:
        tz = pytz.timezone(timezone)
        now = datetime.now(tz)
        return f"Current time in {timezone}: {now.strftime('%H:%M:%S')}"
    except Exception:
        return f"Invalid timezone: {timezone}"


tools = [get_weather, get_time]

provider = os.getenv("LLM_PROVIDER", "groq").lower()
if provider == "groq":
    from langchain_groq import ChatGroq
    llm = ChatGroq(model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"))
else:
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"))

llm_with_tools = llm.bind_tools(tools)


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


def agent_node(state):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


def should_continue(state):
    last_msg = state["messages"][-1]
    if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
        return "tools"
    return "end"


graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.add_node("tools", ToolNode(tools))
graph.set_entry_point("agent")
graph.add_conditional_edges("agent", should_continue, {"tools": "tools", "end": END})
graph.add_edge("tools", "agent")

app = graph.compile()

# ── Step 3: Run the agent — traces appear in Phoenix ──

if __name__ == "__main__":
    print(f"Traced Weather Agent (provider: {provider})")
    print("=" * 50)

    queries = [
        "What's the weather in Paris?",
        "What's the current time in Asia/Tokyo?",
        "What's the weather in Tokyo?",
    ]

    for query in queries:
        print(f"\nQuery: {query}")
        try:
            result = app.invoke({"messages": [HumanMessage(content=query)]})
            print(f"Agent: {result['messages'][-1].content}")
        except Exception as e:
            print(f"Agent: [Error] {type(e).__name__}: {e}")

    print("\n" + "=" * 50)
    print("Now open http://localhost:6006 to inspect the traces!")
    print("You'll see:")
    print("  - LLM call spans (input prompt, output, token count)")
    print("  - Tool call spans (get_weather, get_time)")
    print("  - Full trace for each query")
    print("\nPhoenix dashboard is running. Type 'exit' to quit.\n")

    while True:
        user_input = input("> ").strip().lower()
        if user_input in ("exit", "quit"):
            print("Shutting down...")
            break

    # Force clean exit to avoid Phoenix temp file cleanup errors on Windows
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
