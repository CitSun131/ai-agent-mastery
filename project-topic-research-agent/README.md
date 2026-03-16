# Topic Research Agent — Ongoing Project

This agent evolves across all 9 weeks of the curriculum, growing from a simple LLM summarizer into a production-ready, multi-agent research system.

## Project Evolution

| Week | Feature Added | Branch |
|------|--------------|--------|
| 1 | Basic LLM summarizer + Phoenix tracing | `week-1-basic` |
| 2 | LangGraph + ADK implementations, error handling | `week-2-frameworks` |
| 3 | Web search tool, ReAct pattern, HITL approval | `week-3-patterns` |
| 4 | Multi-agent (supervisor/researcher), Ralph Wiggum Loop, middlewares | `week-4-advanced` |
| 5 | RAG pipeline, context graphs, persistent memory | `week-5-memory` |
| 6 | Production-grade observability, streaming, Phoenix evals | `week-6-mastery` |
| 7 | MCP tool server, A2A agent interoperability | `week-7-mcp-a2a` |
| 8 | 6-layer safety stack, cost budgets, red-team tested | `week-8-safety` |
| 9 | Unit/integration tests, Docker deployment, CI/CD | `week-9-production` |

## Running the Agent

```bash
# From the repo root
cd project-topic-research-agent

# LangGraph version
python src/main.py --framework langgraph --topic "Impact of AI on healthcare"

# ADK version
python src/main.py --framework adk --topic "Impact of AI on healthcare"
```

## Architecture

```
User Query → Input Validation → Tool Selection → Research Loop → Structured Output
                  ↑                                    ↓
             Safety Guard                     Phoenix Tracing
```
