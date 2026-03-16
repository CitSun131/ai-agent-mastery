"""
Exercise 3: Name Memory Agent
================================
Difficulty: Intermediate | Time: 2.5 hours

Task:
Build a LangGraph agent that:
1. Greets the user and asks for their name
2. Remembers the name across conversation turns
3. Tracks how many messages have been exchanged
4. Uses the name naturally in all responses

Instructions:
1. Define a ChatState TypedDict with: messages, user_name, message_count
2. Create a chat_node that uses the LLM with state context
3. Build a LangGraph StateGraph with conditional edges
4. Add a simple loop: continue chatting until user says "bye"
5. Bonus: Add Phoenix tracing and observe the conversation flow

Run: python exercise_03_name_memory_agent.py
"""

from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, Optional
from langgraph.graph import add_messages


class ChatState(TypedDict):
    """Define your agent state here."""
    # TODO: Add fields for messages, user_name, message_count
    pass


def create_memory_agent():
    """Build the name-memory agent.

    Returns:
        Compiled LangGraph agent
    """
    # TODO: Implement the agent
    # 1. Initialize ChatOpenAI
    # 2. Create chat_node function that uses state
    # 3. Create should_continue function for loop control
    # 4. Build StateGraph with nodes and edges
    # 5. Return compiled graph
    pass


if __name__ == "__main__":
    print("Name Memory Agent")
    print("=" * 40)
    print("Type 'quit' to exit\n")

    # agent = create_memory_agent()
    # state = {"messages": [], "user_name": None, "message_count": 0}
    #
    # while True:
    #     user_input = input("You: ")
    #     if user_input.lower() in ["quit", "exit"]:
    #         break
    #     # ... invoke agent and print response
