"""
Arize Phoenix Tracing Configuration
====================================
Sets up Phoenix for agent observability across all weeks.
Import this at the top of any notebook or script to enable tracing.

Usage:
    from config.phoenix_config import setup_tracing
    setup_tracing()
"""

import os


def setup_tracing(port: int = None):
    """Initialize Arize Phoenix for agent tracing.

    Args:
        port: Phoenix dashboard port (default: from env or 6006)
    """
    try:
        import phoenix as px
        from openinference.instrumentation.langchain import LangChainInstrumentor
        from phoenix.otel import register

        phoenix_port = port or int(os.getenv("PHOENIX_PORT", "6006"))

        # Launch Phoenix dashboard
        px.launch_app(port=phoenix_port)
        print(f"Phoenix dashboard: http://localhost:{phoenix_port}")

        # Instrument LangChain/LangGraph
        tracer_provider = register()
        LangChainInstrumentor().instrument(tracer_provider=tracer_provider)

        print("Tracing active — all LangGraph/LangChain calls will be traced.")
        return tracer_provider

    except ImportError as e:
        print(f"Phoenix not installed. Run: pip install arize-phoenix")
        print(f"Missing: {e}")
        return None


def setup_tracing_colab():
    """Simplified setup for Google Colab notebooks."""
    print("Installing Phoenix dependencies...")
    os.system("pip install -q arize-phoenix openinference-instrumentation-langchain")
    return setup_tracing()
