---
name: backend
description: Preferred stack for backend services using uv, FastAPI, Python 3.12+, and AI tools
metadata:
  author: User
  version: "2026.01.28"
---

# Modern Backend Stack Preferences

This skill covers the preferred tooling, configurations, and best practices for creating backend services in the `server` directory.

## Quick Summary

| Category | Preference |
|----------|------------|
| Package Manager | uv |
| Language | Python 3.12+ |
| Web Framework | FastAPI |
| ASGI Server | Uvicorn |
| Validation | Pydantic v2 |
| Configuration | Pydantic Settings |
| Database | SQLAlchemy (Async) |
| Migrations | Alembic |
| LLM Integration | LiteLLM |
| Document Parsing | Docling |

---

## Core Stack

### Project Management (uv)

Use **uv** for all Python project management (scaffolding, dependency management, virtual environments).

| Command | Description |
|---------|-------------|
| `uv init` | Initialize a new project |
| `uv add <pkg>` | Add dependency |
| `uv add --dev <pkg>` | Add development dependency |
| `uv run <cmd>` | Run command in virtual environment |
| `uv venv` | Create virtual environment |

### Project Location

The backend project should be initialized in the `server/` directory.

### Framework (FastAPI)

Use **FastAPI** for building APIs.

-   Use `APIRouter` for modularizing routes.
-   Use `pydantic-settings` for configuration management.

### Database (SQLAlchemy + Alembic)

Use **SQLAlchemy 2.0+** with **AsyncIO** support.
Use **Alembic** for database migrations.

### AI & LLM (LiteLLM + Docling)

-   **LiteLLM**: For standardized access to various LLM providers.
-   **Docling**: For parsing and processing documents.

---

## References

### Setup & Configuration

| Topic | Description | Reference |
|-------|-------------|-----------|
| Project Setup | Using uv, strict python versioning, and environment variables | [setup](references/setup.md) |
| API Development | FastAPI structure, error handling, and validation | [api](references/api.md) |

### Data & Architecture

| Topic | Description | Reference |
|-------|-------------|-----------|
| Database Access | Async SQLAlchemy strategies and Alembic migrations | [database](references/database.md) |
| AI Integration | using LiteLLM and Docling for AI features | [ai](references/ai.md) |
