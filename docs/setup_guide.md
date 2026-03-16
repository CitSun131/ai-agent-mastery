# Environment Setup Guide

## Option 1: Google Colab (Recommended for Beginners)

1. Go to [colab.research.google.com](https://colab.research.google.com/)
2. Create a new notebook
3. Run: `!pip install langgraph langchain langchain-openai google-adk arize-phoenix`
4. Add API keys via Colab Secrets (key icon in left sidebar)

## Option 2: Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt

# Set up API keys
cp config/.env.example config/.env
# Edit config/.env with your keys
```

## Option 3: Docker (Week 9)

```bash
cd week-09-testing-deployment/docker
docker-compose up --build
```

## Getting API Keys

| Provider | URL | Notes |
|----------|-----|-------|
| OpenAI | https://platform.openai.com/api-keys | $5 free credit on signup |
| Google | https://aistudio.google.com/apikey | Gemini Flash free tier |
| Anthropic | https://console.anthropic.com/ | Free tier available |
