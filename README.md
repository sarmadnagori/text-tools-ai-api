# Text Tools AI API

A REST API offering three AI-powered text operations, built with FastAPI and Ollama.

## Features

- **Summarize** — condense any text
- **Translate** — translate text to Urdu
- **Explain** — explain text in simple terms

Each endpoint shares a single `ask_model` helper — the Ollama call is written once, and the endpoints differ only in the prompt they build.

## Tech Stack

- **FastAPI** — web framework
- **Ollama** — local LLM runtime (llama3.2)
- **Pydantic** — request validation

## Setup

1. Install [Ollama](https://ollama.com) and pull the model:
ollama pull llama3.2
2. Install dependencies:
python3 -m uvicorn main:app --reload
3. Run the server:
python3 -m uvicorn main:app --reload

## API

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/summarize` | Returns a summary of the text |
| POST | `/translate` | Returns the text translated to Urdu |
| POST | `/explain` | Returns a simple explanation of the text |

All three take the same body:
```json
{
  "text": "your text here"
}
```

Interactive docs available at `/docs` when the server is running.