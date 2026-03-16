# AI Agent Mastery — 9-Week Curriculum Repository

A comprehensive, hands-on repository for mastering AI agent development using **LangGraph** and **Google ADK**, with observability via **Arize Phoenix**.

## Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/ai-agent-mastery.git
cd ai-agent-mastery

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up API keys
cp config/.env.example config/.env
# Edit config/.env with your API keys

# 5. Open Week 1 notebook
# Go to https://colab.research.google.com/ and upload week-01-fundamentals/notebooks/
```

## Repository Structure

```
ai-agent-mastery/
│
├── README.md                          # This file
├── requirements.txt                   # All Python dependencies
├── setup.py                           # Package configuration
├── .gitignore                         # Git ignore rules
├── .env.example                       # Template for API keys
│
├── config/                            # Configuration files
│   ├── .env.example                   # API keys template (NEVER commit .env)
│   ├── phoenix_config.py              # Arize Phoenix tracing setup
│   └── llm_config.py                  # LLM model configurations
│
├── shared/                            # Shared utilities across all weeks
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── api_helpers.py             # Common API call utilities
│   │   ├── cost_tracker.py            # Token usage & cost tracking
│   │   └── tracing.py                 # Phoenix tracing helpers
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── base_schemas.py            # Pydantic models shared across weeks
│   └── prompts/
│       ├── __init__.py
│       └── system_prompts.py          # Reusable system prompt templates
│
├── week-01-fundamentals/              # Week 1: Agent Fundamentals & Setup
│   ├── notebooks/
│   │   ├── 01_what_is_an_agent.ipynb
│   │   ├── 02_environment_setup.ipynb
│   │   ├── 03_first_llm_calls.ipynb
│   │   ├── 04_basic_tools.ipynb
│   │   └── 05_state_and_tracing.ipynb
│   ├── exercises/
│   │   ├── exercise_01_weather_fetcher.py
│   │   ├── exercise_02_smart_summarizer.py
│   │   └── exercise_03_name_memory_agent.py
│   └── solutions/
│       └── (completed after attempting exercises)
│
├── week-02-framework-basics/          # Week 2: LangGraph & ADK Basics
│   ├── notebooks/
│   │   ├── 01_langgraph_basics.ipynb
│   │   ├── 02_adk_basics.ipynb
│   │   ├── 03_framework_comparison.ipynb
│   │   └── 04_error_handling_cost.ipynb
│   ├── langgraph/
│   │   └── simple_graph_agent.py
│   ├── adk/
│   │   └── simple_llm_agent.py
│   ├── exercises/
│   └── solutions/
│
├── week-03-basic-patterns/            # Week 3: Basic Agentic Patterns
│   ├── notebooks/
│   │   ├── 01_tool_use_patterns.ipynb
│   │   ├── 02_react_pattern.ipynb
│   │   ├── 03_chain_of_thought.ipynb
│   │   └── 04_human_in_the_loop.ipynb
│   ├── exercises/
│   └── solutions/
│
├── week-04-advanced-patterns/         # Week 4: Advanced Patterns & Middlewares
│   ├── notebooks/
│   │   ├── 01_planning_decomposition.ipynb
│   │   ├── 02_multi_agent_systems.ipynb
│   │   ├── 03_ralph_wiggum_loop.ipynb
│   │   ├── 04_failure_recovery.ipynb
│   │   └── 05_middlewares.ipynb
│   ├── exercises/
│   └── solutions/
│
├── week-05-context-memory/            # Week 5: Context Engineering & Memory
│   ├── notebooks/
│   │   ├── 01_context_engineering.ipynb
│   │   ├── 02_basic_rag.ipynb
│   │   ├── 03_advanced_rag.ipynb
│   │   ├── 04_agentic_rag.ipynb
│   │   ├── 05_memory_types.ipynb
│   │   └── 06_context_graphs.ipynb
│   ├── exercises/
│   └── solutions/
│
├── week-06-framework-mastery/         # Week 6: Framework Mastery & Observability
│   ├── notebooks/
│   │   ├── 01_langgraph_deep_dive.ipynb
│   │   ├── 02_adk_deep_dive.ipynb
│   │   ├── 03_advanced_middlewares.ipynb
│   │   ├── 04_phoenix_evals.ipynb
│   │   └── 05_streaming_async.ipynb
│   ├── exercises/
│   └── solutions/
│
├── week-07-mcp-a2a-synthesis/         # Week 7: MCP, A2A Protocol & Synthesis
│   ├── notebooks/
│   │   ├── 01_mcp_fundamentals.ipynb
│   │   ├── 02_building_mcp_servers.ipynb
│   │   ├── 03_a2a_protocol.ipynb
│   │   ├── 04_a2a_agent_cards.ipynb
│   │   └── 05_capstone_integration.ipynb
│   ├── mcp-servers/
│   │   ├── weather_server.py
│   │   └── database_server.py
│   ├── exercises/
│   └── solutions/
│
├── week-08-safety-security-cost/      # Week 8: Safety, Security & Cost Management
│   ├── notebooks/
│   │   ├── 01_prompt_injection_defense.ipynb
│   │   ├── 02_safety_layers.ipynb
│   │   ├── 03_cost_management.ipynb
│   │   ├── 04_rate_limiting_caching.ipynb
│   │   └── 05_red_teaming.ipynb
│   ├── exercises/
│   └── solutions/
│
├── week-09-testing-deployment/        # Week 9: Testing, Deployment & Production
│   ├── notebooks/
│   │   ├── 01_unit_testing_agents.ipynb
│   │   ├── 02_integration_testing.ipynb
│   │   ├── 03_deployment_docker.ipynb
│   │   └── 04_monitoring_alerting.ipynb
│   ├── tests/
│   │   ├── unit/
│   │   ├── integration/
│   │   └── e2e/
│   ├── docker/
│   │   ├── Dockerfile
│   │   └── docker-compose.yml
│   └── solutions/
│
├── project-topic-research-agent/      # Ongoing Project (Weeks 1–9)
│   ├── README.md                      # Project documentation
│   ├── src/
│   │   ├── __init__.py
│   │   ├── main.py                    # Entry point
│   │   ├── agents/
│   │   │   ├── __init__.py
│   │   │   ├── langgraph_agent.py     # LangGraph implementation
│   │   │   └── adk_agent.py           # ADK implementation
│   │   ├── tools/
│   │   │   ├── __init__.py
│   │   │   ├── search.py              # Web search tool
│   │   │   ├── weather.py             # Weather API tool
│   │   │   └── calculator.py          # Calculator tool
│   │   ├── middlewares/
│   │   │   ├── __init__.py
│   │   │   ├── logging_mw.py          # Logging middleware
│   │   │   ├── safety_guard.py        # Input validation
│   │   │   └── cost_guard.py          # Token budget enforcement
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── research_schemas.py    # Pydantic output models
│   │   └── config/
│   │       ├── __init__.py
│   │       └── settings.py            # Project settings
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_tools.py
│   │   ├── test_agent.py
│   │   └── test_middlewares.py
│   ├── traces/                        # Phoenix trace exports
│   │   └── .gitkeep
│   └── docs/
│       └── architecture.md            # Agent architecture diagram
│
├── docs/                              # Course documentation
│   ├── curriculum_overview.md
│   ├── setup_guide.md
│   └── troubleshooting.md
│
└── .github/
    └── workflows/
        └── ci.yml                     # CI/CD pipeline
```

## Curriculum Overview

| Week | Focus | Key Deliverable |
|------|-------|----------------|
| 1 | Agent Fundamentals & Setup | Working environments + first traced agent |
| 2 | Framework Basics (LangGraph & ADK) | Framework-based agents with error handling |
| 3 | Basic Agentic Patterns | Tool-use, ReAct, chain-of-thought agents |
| 4 | Advanced Patterns & Middlewares | Multi-agent, Ralph Wiggum Loop, failure recovery |
| 5 | Context Engineering & Memory | RAG pipeline + context graphs + memory persistence |
| 6 | Framework Mastery & Observability | Production-grade agents with Phoenix evals |
| 7 | MCP, A2A Protocol & Synthesis | MCP server integration + A2A interoperability |
| 8 | Safety, Security & Cost | 6-layer safety stack + cost budgeting |
| 9 | Testing, Deployment & Production | Docker deployment + CI/CD + monitoring |

## Ongoing Project: Topic Research Agent

The **Topic Research Agent** evolves across all 9 weeks:

- **Week 1**: Basic LLM-powered summarizer with tracing
- **Week 2**: Reimplemented in LangGraph + ADK frameworks
- **Week 3**: Added tools (web search), ReAct pattern, HITL
- **Week 4**: Multi-agent architecture, Ralph Wiggum Loop, middlewares
- **Week 5**: RAG integration, context graphs, persistent memory
- **Week 6**: Production-hardened with advanced observability
- **Week 7**: MCP tool server + A2A agent interoperability
- **Week 8**: Safety layers, cost budgets, red-team tested
- **Week 9**: Fully tested, Dockerized, deployed with monitoring

## Environment Setup

### Required API Keys

| Provider | Purpose | Free Tier? |
|----------|---------|------------|
| OpenAI | GPT-4o-mini for LangGraph | $5 credit on signup |
| Google | Gemini Flash for ADK | Generous free tier |
| Anthropic | Claude (optional) | Free tier available |

### Setup Steps

1. Copy `config/.env.example` to `config/.env`
2. Add your API keys to `config/.env`
3. **Never commit `.env` files** — they are in `.gitignore`

## Contributing

1. Create a feature branch: `git checkout -b week-X-progress`
2. Make your changes and commit: `git commit -m "Complete Week X exercises"`
3. Push and create a PR: `git push origin week-X-progress`

## License

This project is for educational purposes as part of the AI Agent Mastery curriculum.
