---
name: backend-setup
description: Project setup and configuration using uv and pydantic-settings
---

# Project Setup & Configuration

## Package Management with uv

We use `uv` for a fast and reliable Python workflow.

### Initializing a Project

To start a new project in `server/`:

```bash
mkdir server
cd server
uv init
```

This creates a `pyproject.toml` and a basic project structure.

### Python Version

Enforce Python 3.12+ in `pyproject.toml`:

```toml
[project]
name = "server"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "fastapi",
    "uvicorn[standard]",
    "pydantic-settings",
    "python-dotenv",
]
```

To install dependencies:
```bash
uv sync
```

## Configuration Management

Use `pydantic-settings` to manage environment variables in a type-safe way.

### `.env` File

Create a `.env` file for local development (and add to `.gitignore`):

```env
APP_ENV=development
DATABASE_URL=postgresql+asyncpg://user:pass@localhost:5432/dbname
OPENAI_API_KEY=sk-...
```

### Config Module (`src/core/config.py`)

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_ENV: str = "development"
    DATABASE_URL: str
    OPENAI_API_KEY: str | None = None
    ALIYUN_API_KEY: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

settings = Settings()
```

### Usage

```python
from src.core.config import settings

print(settings.DATABASE_URL)
```
