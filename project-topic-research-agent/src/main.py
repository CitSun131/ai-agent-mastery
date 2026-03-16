"""
Topic Research Agent — Main Entry Point
=========================================
Run the research agent from the command line.

Usage:
    python src/main.py --framework langgraph --topic "AI in healthcare"
    python src/main.py --framework adk --topic "Climate change solutions"
    python src/main.py --framework langgraph --topic "AI agents" --no-trace
"""

import argparse
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from dotenv import load_dotenv
# Load .env from project root (ai-agent-mastery/config/.env) regardless of cwd
project_root = os.path.join(os.path.dirname(__file__), "..", "..")
load_dotenv(os.path.join(project_root, "config", ".env"))
load_dotenv()


def main():
    parser = argparse.ArgumentParser(description="Topic Research Agent")
    parser.add_argument("--framework", choices=["langgraph", "adk"], default="langgraph",
                        help="Agent framework to use")
    parser.add_argument("--topic", type=str, required=True,
                        help="Research topic to investigate")
    parser.add_argument("--no-trace", action="store_true",
                        help="Disable Phoenix tracing")
    parser.add_argument("--verbose", action="store_true",
                        help="Enable verbose output")

    args = parser.parse_args()
    tracing_active = False

    # Setup tracing (enabled by default, disable with --no-trace)
    if not args.no_trace:
        try:
            from config.phoenix_config import setup_tracing
            setup_tracing()
            tracing_active = True
        except ImportError:
            print("Phoenix not available. Running without tracing.")
        except Exception as e:
            print(f"Phoenix setup failed: {e}. Running without tracing.")

    print(f"\nTopic Research Agent")
    print(f"{'='*50}")
    print(f"Framework: {args.framework}")
    print(f"Topic:     {args.topic}")
    print(f"Tracing:   {'enabled' if tracing_active else 'disabled'}")
    print(f"{'='*50}\n")

    # Run the appropriate agent
    result = None
    try:
        if args.framework == "langgraph":
            from agents.langgraph_agent import run_research
            result = run_research(args.topic)
        elif args.framework == "adk":
            from agents.adk_agent import run_research
            import asyncio
            result = asyncio.run(run_research(args.topic))

        # Display results
        if result:
            print(f"\n{'='*50}")
            print("RESEARCH COMPLETE")
            print(f"{'='*50}")
            if isinstance(result, dict):
                import json
                print(json.dumps(result, indent=2, default=str))
            else:
                print(result)

    except Exception as e:
        print(f"\n[Error] {type(e).__name__}: {e}")

    # Keep alive for Phoenix trace inspection (even on error, so you can see partial traces)
    if tracing_active:
        print(f"\n{'='*50}")
        print("Phoenix dashboard is running at http://localhost:6006")
        print("Open the URL above to inspect LLM call traces.")
        print("Type 'exit' to quit.\n")

        while True:
            try:
                user_input = input("> ").strip().lower()
                if user_input in ("exit", "quit"):
                    print("Shutting down...")
                    break
            except (KeyboardInterrupt, EOFError):
                print("\nShutting down...")
                break

    # Force clean exit to avoid Phoenix temp file cleanup errors on Windows
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)


if __name__ == "__main__":
    main()
