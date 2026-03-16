"""
Cost Tracker
=============
Track token usage and estimated costs across LLM API calls.
Helps enforce weekly budgets and provides usage reports.

Usage:
    tracker = CostTracker(weekly_budget=5.00)
    tracker.log_call("gpt-4o-mini", input_tokens=150, output_tokens=300)
    tracker.report()
"""

import os
from datetime import datetime


# Pricing per 1M tokens (as of March 2026)
MODEL_PRICING = {
    "llama-3.3-70b-versatile": {"input": 0.59, "output": 0.79},
    "llama-3.1-8b-instant": {"input": 0.05, "output": 0.08},
    "mixtral-8x7b-32768": {"input": 0.24, "output": 0.24},
    "gemma2-9b-it": {"input": 0.20, "output": 0.20},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "gpt-4-turbo": {"input": 10.00, "output": 30.00},
    "gemini-3-flash-preview": {"input": 0.0, "output": 0.0},  # Free tier
    "gemini-1.5-pro": {"input": 1.25, "output": 5.00},
    "claude-3-5-sonnet": {"input": 3.00, "output": 15.00},
    "claude-3-5-haiku": {"input": 0.25, "output": 1.25},
}


class CostTracker:
    """Track and manage LLM API costs."""

    def __init__(self, weekly_budget: float = None):
        self.weekly_budget = weekly_budget or float(os.getenv("WEEKLY_BUDGET_USD", "5.00"))
        self.alert_threshold = float(os.getenv("ALERT_THRESHOLD_PCT", "80")) / 100
        self.calls = []
        self.total_cost = 0.0
        self.total_input_tokens = 0
        self.total_output_tokens = 0

    def log_call(self, model: str, input_tokens: int, output_tokens: int):
        """Log an LLM API call and its cost.

        Args:
            model: Model name (e.g., "gpt-4o-mini")
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
        """
        pricing = MODEL_PRICING.get(model, {"input": 1.0, "output": 3.0})
        cost = (input_tokens * pricing["input"] + output_tokens * pricing["output"]) / 1_000_000

        self.calls.append({
            "timestamp": datetime.now().isoformat(),
            "model": model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost_usd": cost,
        })

        self.total_cost += cost
        self.total_input_tokens += input_tokens
        self.total_output_tokens += output_tokens

        # Budget alert
        if self.total_cost >= self.weekly_budget * self.alert_threshold:
            pct = (self.total_cost / self.weekly_budget) * 100
            print(f"BUDGET ALERT: {pct:.0f}% of weekly budget used (${self.total_cost:.4f} / ${self.weekly_budget:.2f})")

        return cost

    def report(self):
        """Print a cost summary report."""
        print("\n" + "=" * 50)
        print("COST TRACKER REPORT")
        print("=" * 50)
        print(f"Total API calls:    {len(self.calls)}")
        print(f"Total input tokens: {self.total_input_tokens:,}")
        print(f"Total output tokens:{self.total_output_tokens:,}")
        print(f"Total cost:         ${self.total_cost:.4f}")
        print(f"Weekly budget:      ${self.weekly_budget:.2f}")
        print(f"Budget remaining:   ${self.weekly_budget - self.total_cost:.4f}")
        print("=" * 50)

        if self.calls:
            # Per-model breakdown
            models = {}
            for call in self.calls:
                m = call["model"]
                if m not in models:
                    models[m] = {"calls": 0, "cost": 0}
                models[m]["calls"] += 1
                models[m]["cost"] += call["cost_usd"]

            print("\nPer-Model Breakdown:")
            for model, stats in sorted(models.items()):
                print(f"  {model}: {stats['calls']} calls, ${stats['cost']:.4f}")

    def reset(self):
        """Reset the tracker for a new week."""
        self.calls = []
        self.total_cost = 0.0
        self.total_input_tokens = 0
        self.total_output_tokens = 0
