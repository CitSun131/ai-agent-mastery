"""
Calculator Tool
================
Safe mathematical expression evaluator for the agent.
"""

from langchain_core.tools import tool
import ast
import operator

# Safe operators for evaluation
SAFE_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.Mod: operator.mod,
}


def _safe_eval(node):
    """Safely evaluate a math expression AST node."""
    if isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        op = SAFE_OPERATORS.get(type(node.op))
        if op is None:
            raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
        return op(left, right)
    elif isinstance(node, ast.UnaryOp):
        operand = _safe_eval(node.operand)
        op = SAFE_OPERATORS.get(type(node.op))
        if op is None:
            raise ValueError(f"Unsupported operator: {type(node.op).__name__}")
        return op(operand)
    else:
        raise ValueError(f"Unsupported expression type: {type(node).__name__}")


@tool
def calculate(expression: str) -> str:
    """Safely evaluate a mathematical expression.

    Args:
        expression: A math expression (e.g., "2 + 3 * 4", "100 / 7")

    Returns:
        The result as a formatted string
    """
    try:
        tree = ast.parse(expression, mode="eval")
        result = _safe_eval(tree.body)
        return f"{expression} = {result}"
    except Exception as e:
        return f"Error evaluating '{expression}': {e}"
