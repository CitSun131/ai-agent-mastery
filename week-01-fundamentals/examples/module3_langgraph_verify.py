"""
Module 3: LangGraph Setup Verification
========================================
Verifies that LangGraph is correctly installed and working.
Run this first to confirm your environment is ready.

Run: python week-01-fundamentals/examples/module3_langgraph_verify.py
"""

from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
from langgraph.graph import add_messages


# Define a minimal state
class TestState(TypedDict):
    messages: Annotated[list, add_messages]


# Create a minimal graph
graph = StateGraph(TestState)


def hello_node(state):
    return {"messages": ["LangGraph is working!"]}


graph.add_node("hello", hello_node)
graph.set_entry_point("hello")
graph.add_edge("hello", END)

app = graph.compile()
result = app.invoke({"messages": []})
print(result)
print("\n[OK] LangGraph setup verified!")
