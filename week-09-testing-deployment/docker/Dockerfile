FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY project-topic-research-agent/ ./project-topic-research-agent/
COPY shared/ ./shared/
COPY config/ ./config/

# Environment variables (override at runtime)
ENV PYTHONPATH=/app
ENV OPENAI_MODEL=gpt-4o-mini
ENV GOOGLE_MODEL=gemini-3-flash-preview
ENV PHOENIX_PORT=6006

EXPOSE 8000 6006

# Default: run the agent API server (Week 9)
CMD ["uvicorn", "project-topic-research-agent.src.api:app", "--host", "0.0.0.0", "--port", "8000"]
