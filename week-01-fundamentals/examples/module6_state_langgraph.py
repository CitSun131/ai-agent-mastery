"""
Module 6: State Management — LangGraph Stateful Research Agent
================================================================
Demonstrates how LangGraph manages state across graph nodes.
The agent:
  1. Collects facts about a topic
  2. Summarizes the collected facts

Each node reads from and writes to a shared state object.

Run: python week-01-fundamentals/examples/module6_state_langgraph.py
"""

import os
from dotenv import load_dotenv

load_dotenv("config/.env")
load_dotenv()

from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, List
from langgraph.graph import add_messages

# Initialize LLM based on provider
provider = os.getenv("LLM_PROVIDER", "groq").lower()
if provider == "groq":
    from langchain_groq import ChatGroq
    llm = ChatGroq(model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"))
else:
    from langchain_openai import ChatOpenAI
    llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"))


class ResearchState(TypedDict):
    messages: Annotated[list, add_messages]
    topic: str
    facts_collected: List[str]
    summary: str


def collect_facts(state):
    """Agent collects facts about the topic."""
    prompt = f"List 3 key facts about: {state['topic']}"
    response = llm.invoke(prompt)
    facts = response.content.split("\n")
    return {"facts_collected": facts}


def summarize(state):
    """Agent summarizes collected facts."""
    facts_text = "\n".join(state["facts_collected"])
    prompt = f"Summarize these facts into one paragraph:\n{facts_text}"
    response = llm.invoke(prompt)
    return {"summary": response.content}


# Build the graph
graph = StateGraph(ResearchState)
graph.add_node("collect", collect_facts)
graph.add_node("summarize", summarize)
graph.set_entry_point("collect")
graph.add_edge("collect", "summarize")
graph.add_edge("summarize", END)

app = graph.compile()


if __name__ == "__main__":
    print(f"Stateful Research Agent (provider: {provider})")
    print("=" * 50)

    topic = "AI agents"
    print(f"Topic: {topic}\n")

    result = app.invoke({
        "messages": [],
        "topic": topic,
        "facts_collected": [],
        "summary": "",
    })

    print("Facts collected:")
    for fact in result["facts_collected"]:
        if fact.strip():
            print(f"  {fact}")

    print(f"\nSummary: {result['summary']}")
