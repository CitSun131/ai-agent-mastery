"""
Safety Guard Middleware
=======================
Input validation and prompt injection defense.
Week 8: Expanded into full 6-layer safety stack.
"""

import re
from typing import Tuple

DANGEROUS_PATTERNS = [
    r"ignore\s+(all\s+)?previous\s+instructions",
    r"ignore\s+(all\s+)?instructions",
    r"forget\s+everything",
    r"you\s+are\s+now",
    r"system\s+prompt",
    r"reveal\s+your\s+(instructions|prompt|system)",
    r"disregard\s+(all|any|your)",
    r"override\s+(safety|security|rules)",
]

COMPILED_PATTERNS = [re.compile(p, re.IGNORECASE) for p in DANGEROUS_PATTERNS]


def validate_input(user_input: str) -> Tuple[bool, str]:
    """Check user input for prompt injection patterns.

    Args:
        user_input: The raw user input string

    Returns:
        Tuple of (is_safe, reason). If is_safe is False, reason explains why.
    """
    if not user_input or not user_input.strip():
        return False, "Empty input"

    if len(user_input) > 10000:
        return False, "Input exceeds maximum length (10,000 characters)"

    for pattern in COMPILED_PATTERNS:
        if pattern.search(user_input):
            return False, f"Potential prompt injection detected"

    return True, "Input passed validation"


def sanitize_input(user_input: str) -> str:
    """Clean and sanitize user input for safe processing.

    Args:
        user_input: The raw user input

    Returns:
        Sanitized input string
    """
    # Remove control characters
    cleaned = "".join(c for c in user_input if c.isprintable() or c in "\n\t")
    # Trim excessive whitespace
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    cleaned = cleaned.strip()
    return cleaned
