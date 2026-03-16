# Troubleshooting Guide

## Common Issues

### "OPENAI_API_KEY not set"
- Ensure `config/.env` exists and has your key
- In Colab: Add key via Secrets Manager (key icon)
- Check: `echo $OPENAI_API_KEY` (should not be empty)

### "Rate limit exceeded"
- You've made too many API calls too quickly
- Solution: Add retry with exponential backoff (see `shared/utils/api_helpers.py`)
- Or wait 60 seconds and try again

### "Module not found: langgraph"
```bash
pip install langgraph langchain langchain-openai
```

### Phoenix dashboard not loading
- Check if port 6006 is in use: `lsof -i :6006`
- Try a different port: `setup_tracing(port=6007)`

### "Invalid API key"
- Double-check your key hasn't expired
- Ensure no extra spaces or newlines in `.env`
- OpenAI keys start with `sk-`

### Colab disconnects
- Colab has idle timeout (~90 min). Re-run cells from top.
- Save work frequently: File > Save

### ADK agent not responding
- Verify Google API key: `echo $GOOGLE_API_KEY`
- Ensure `gemini-3-flash-preview` is available in your region
- Try: `pip install --upgrade google-adk`
