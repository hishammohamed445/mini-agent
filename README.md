# Mini Agent

A lightweight learning project for building toward a small AI-agent / RAG service with FastAPI.

The repository currently provides the initial API and environment setup. It is intentionally minimal and will be expanded incrementally with retrieval, model integration, tool use, memory, and evaluation components.

## Current scope

- FastAPI application
- `/welcome` health-style endpoint
- Uvicorn development server
- Environment configuration template
- Foundation for future AI-agent and RAG experiments

## Tech stack

- Python
- FastAPI
- Uvicorn
- python-multipart

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requierments.txt
uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/welcome
```

Interactive API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Roadmap

Planned next steps:

1. Add LLM provider integration.
2. Introduce document ingestion and chunking.
3. Add vector retrieval for a minimal RAG workflow.
4. Introduce tool calling and a basic agent loop.
5. Add structured configuration and secrets handling.
6. Add tests and evaluation for retrieval and agent behavior.

## Status

Early-stage learning project. The current repository is the application foundation rather than a complete agent system.

## Author

[Hisham Mohamed](https://github.com/hishammohamed445) — AI Engineer focused on Computer Vision, Machine Learning systems, RAG, and Agentic AI.
