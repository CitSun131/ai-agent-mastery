"""
Tracing Utilities
==================
Helper functions for Phoenix tracing across all weeks.
"""

import time
from functools import wraps


def trace_agent_run(func):
    """Decorator to trace agent execution time and log results.

    Usage:
        @trace_agent_run
        def my_agent_function(query):
            ...
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"[TRACE] Starting: {func.__name__}")

        try:
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            print(f"[TRACE] Completed: {func.__name__} ({elapsed:.2f}s)")
            return result
        except Exception as e:
            elapsed = time.time() - start
            print(f"[TRACE] FAILED: {func.__name__} ({elapsed:.2f}s) - {e}")
            raise

    return wrapper


def print_trace_summary(result: dict, label: str = "Agent Run"):
    """Print a formatted summary of an agent run result.

    Args:
        result: The agent's output dictionary
        label: A label for this trace
    """
    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"{'='*50}")

    if isinstance(result, dict):
        for key, value in result.items():
            if key == "messages":
                print(f"  messages: {len(value)} total")
                if value:
                    last = value[-1]
                    content = getattr(last, "content", str(last))
                    preview = content[:200] + "..." if len(content) > 200 else content
                    print(f"  last_message: {preview}")
            else:
                val_str = str(value)
                preview = val_str[:200] + "..." if len(val_str) > 200 else val_str
                print(f"  {key}: {preview}")
    else:
        print(f"  Result: {result}")

    print(f"{'='*50}\n")
