"""
Module 4: LLM API Integration — First API Calls
==================================================
Demonstrates calling multiple LLM providers:
  - Groq (default, fast inference with Llama models)
  - OpenAI (GPT-4o-mini)
  - Gemini (via LangChain)

Set LLM_PROVIDER in your .env to choose the default provider.

Run: python week-01-fundamentals/examples/module4_llm_api_calls.py
"""

import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv("config/.env")
load_dotenv()


# ──────────────────────────────────────────────
# 1. Groq API Call (default — fast & affordable)
# ──────────────────────────────────────────────
def demo_groq():
    from langchain_groq import ChatGroq

    print("=" * 50)
    print("1. GROQ API (Llama 3.3 70B)")
    print("=" * 50)

    llm = ChatGroq(
        model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
        temperature=0.7,
        max_tokens=500,
    )

    messages = [
        SystemMessage(content="You are a helpful AI tutor."),
        HumanMessage(content="Explain what an AI agent is in 3 sentences."),
    ]

    response = llm.invoke(messages)
    print(response.content)
    print(f"\nTokens used: {response.response_metadata.get('token_usage', 'N/A')}")
    print()


# ──────────────────────────────────────────────
# 2. OpenAI API Call
# ──────────────────────────────────────────────
def demo_openai():
    from langchain_openai import ChatOpenAI

    print("=" * 50)
    print("2. OPENAI API (GPT-4o-mini)")
    print("=" * 50)

    llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0.7,
        max_tokens=500,
    )

    messages = [
        SystemMessage(content="You are a helpful AI tutor."),
        HumanMessage(content="Explain what an AI agent is in 3 sentences."),
    ]

    response = llm.invoke(messages)
    print(response.content)
    print(f"\nTokens used: {response.response_metadata.get('token_usage', 'N/A')}")
    print()


# ──────────────────────────────────────────────
# 3. Gemini API Call
# ──────────────────────────────────────────────
def demo_gemini():
    from langchain_google_genai import ChatGoogleGenerativeAI

    print("=" * 50)
    print("3. GEMINI API (Gemini 2.0 Flash)")
    print("=" * 50)

    gemini = ChatGoogleGenerativeAI(
        model=os.getenv("GOOGLE_MODEL", "gemini-3-flash-preview"),
        temperature=0.7,
    )

    response = gemini.invoke(
        [HumanMessage(content="What makes an AI agent different from a chatbot?")]
    )
    print(response.content)
    print()


# ──────────────────────────────────────────────
# Run the demo for the selected provider
# ──────────────────────────────────────────────
if __name__ == "__main__":
    provider = os.getenv("LLM_PROVIDER", "groq").lower()

    print(f"Default provider: {provider}")
    print(f"(Set LLM_PROVIDER in .env to switch)\n")

    if provider == "groq":
        demo_groq()
    elif provider == "openai":
        demo_openai()
    elif provider == "google":
        demo_gemini()
    else:
        demo_groq()

    # Uncomment below to run ALL providers at once:
    # demo_groq()
    # demo_openai()
    # demo_gemini()
