"""
Phoenix Tracing Configuration
===============================
Sets up Arize Phoenix for LLM call tracing.
Dashboard available at http://localhost:6006 after setup.
"""

import sys
import warnings

# Suppress SQLAlchemy reflection warnings from Phoenix
warnings.filterwarnings("ignore", message=".*Skipped unsupported reflection.*")

# Fix Windows console encoding for Phoenix emoji output
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def setup_tracing():
    """Launch Phoenix and instrument LangChain for tracing."""
    import phoenix as px
    from openinference.instrumentation.langchain import LangChainInstrumentor
    from phoenix.otel import register

    px.launch_app()
    tracer_provider = register()
    LangChainInstrumentor().instrument(tracer_provider=tracer_provider)

    print("[OK] Phoenix tracing is active!")
    print("Dashboard: http://localhost:6006\n")
