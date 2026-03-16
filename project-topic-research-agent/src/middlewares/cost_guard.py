"""
Cost Guard Middleware
=====================
Enforce token budgets and prevent runaway API costs.
Week 8: Expanded with model routing and caching.
"""


class CostGuard:
    """Middleware that enforces a per-session token budget."""

    def __init__(self, max_tokens: int = 50000, max_cost_usd: float = 1.00):
        self.max_tokens = max_tokens
        self.max_cost_usd = max_cost_usd
        self.tokens_used = 0
        self.cost_used = 0.0

    def check_budget(self, estimated_tokens: int = 1000) -> bool:
        """Check if there is budget remaining for another API call.

        Args:
            estimated_tokens: Estimated tokens for the next call

        Returns:
            True if within budget, False if budget exceeded
        """
        if self.tokens_used + estimated_tokens > self.max_tokens:
            print(f"TOKEN BUDGET EXCEEDED: {self.tokens_used}/{self.max_tokens} tokens used")
            return False
        return True

    def log_usage(self, tokens: int, cost: float = 0.0):
        """Record token usage after an API call."""
        self.tokens_used += tokens
        self.cost_used += cost

    @property
    def remaining_tokens(self) -> int:
        return max(0, self.max_tokens - self.tokens_used)

    @property
    def remaining_budget(self) -> float:
        return max(0, self.max_cost_usd - self.cost_used)
