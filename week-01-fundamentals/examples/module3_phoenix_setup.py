"""
Module 3: Arize Phoenix Observability Setup
=============================================
Launches Phoenix dashboard and instruments LangChain/LangGraph
so all LLM calls are automatically traced.

After running, open http://localhost:6006 in your browser to see traces.

Run: python week-01-fundamentals/examples/module3_phoenix_setup.py
"""

import os
import sys

# Fix Windows console encoding for Phoenix emoji output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import phoenix as px
from openinference.instrumentation.langchain import LangChainInstrumentor
from phoenix.otel import register

# Launch Phoenix (creates a local dashboard)
px.launch_app()

# Instrument LangChain/LangGraph
tracer_provider = register()
LangChainInstrumentor().instrument(tracer_provider=tracer_provider)

print("[OK] Phoenix tracing is active!")
print("Open the Phoenix dashboard at http://localhost:6006 to see traces.")
print("Press Ctrl+C to stop the dashboard.")

# Keep the process alive so the dashboard stays up
try:
    import time
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nPhoenix dashboard stopped.")
    os._exit(0)
