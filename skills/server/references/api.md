---
name: backend-api
description: API development guidelines with FastAPI
---

# API Development

## Project Structure

Organize the FastAPI application using a domain-driven or module-based structure.

```
src/
├── api/
│   ├── v1/
│   │   ├── endpoints/
│   │   │   ├── auth.py
│   │   │   ├── users.py
│   │   │   └── items.py
│   │   └── api.py  # Router aggregation
├── core/
│   ├── config.py
│   └── security.py
├── models/         # SQLAlchemy models
├── schemas/        # Pydantic schemas (DTOs)
├── services/       # Business logic
└── main.py
```

## Setup `main.py`

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.core.config import settings
from src.api.v1.api import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Database connection, etc.
    yield
    # Shutdown: Cleanup

app = FastAPI(
    title="Server API",
    lifespan=lifespan,
    docs_url="/docs" if settings.APP_ENV != "production" else None,
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
```

## Router Aggregation (`src/api/v1/api.py`)

```python
from fastapi import APIRouter
from src.api.v1.endpoints import users, items

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
```

## Validation (Pydantic)

Use Pydantic v2 schemas for request and response validation. Place them in `src/schemas/`.

```python
from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    email: str
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)
```

## Running the Server

Use `uvicorn` for development and production.

Development command:
```bash
uv run uvicorn src.main:app --reload
```
