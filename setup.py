from setuptools import setup, find_packages

setup(
    name="ai-agent-mastery",
    version="1.0.0",
    description="AI Agent Mastery — 9-Week Curriculum Repository",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "langgraph>=0.2.0",
        "langchain>=0.3.0",
        "langchain-openai>=0.2.0",
        "google-adk>=0.3.0",
        "arize-phoenix>=5.0.0",
        "pydantic>=2.9.0",
        "requests>=2.32.0",
        "tenacity>=9.0.0",
        "python-dotenv>=1.0.0",
    ],
)
