"""
Logging Middleware
==================
Structured logging for agent execution.
"""

import logging
import time
from functools import wraps

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%H:%M:%S",
)

logger = logging.getLogger("agent")


def log_node_execution(node_name: str):
    """Decorator to log LangGraph node execution.

    Usage:
        @log_node_execution("research")
        def research_node(state):
            ...
    """
    def decorator(func):
        @wraps(func)
        def wrapper(state, *args, **kwargs):
            logger.info(f"[{node_name}] Starting | iteration={state.get('iteration', '?')}")
            start = time.time()

            try:
                result = func(state, *args, **kwargs)
                elapsed = time.time() - start
                logger.info(f"[{node_name}] Completed ({elapsed:.2f}s)")
                return result
            except Exception as e:
                elapsed = time.time() - start
                logger.error(f"[{node_name}] FAILED ({elapsed:.2f}s) | {type(e).__name__}: {e}")
                raise

        return wrapper
    return decorator
