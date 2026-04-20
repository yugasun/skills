---
name: backend-database
description: Database access using Async SQLAlchemy and Alembic
---

# Database & Migrations

## Dependencies

```bash
uv add "sqlalchemy[asyncio]" alembic asyncpg
```

## Async Engine Setup

Create `src/db/session.py`:

```python
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.core.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.APP_ENV == "development",
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)

# Dependency for FastAPI routes
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
```

## Declarative Models

Create `src/db/base.py` for the shared `Base` class, and import all models there to ensure Alembic detects them.

```python
# src/db/base_class.py
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```

Example Model (`src/models/user.py`):

```python
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from src.db.base_class import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
```

## Migrations (Alembic)

Initialize Alembic:

```bash
uv run alembic init -t async migrations
```

Update `migrations/env.py` to:
1.  Import your models' Base metadata (`target_metadata = Base.metadata`).
2.  Use `settings.DATABASE_URL`.

### Common Commands

| Action | Command |
|--------|---------|
| Create Migration | `uv run alembic revision --autogenerate -m "message"` |
| Run Migrations | `uv run alembic upgrade head` |
| Revert Migration | `uv run alembic downgrade -1` |
