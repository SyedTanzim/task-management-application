# Task Management Application

A task management backend built with **FastAPI** and **Python 3.13**, managed with **uv**.

**Status:** Early scaffold. The project structure is in place, but the core logic (models, routes, database) has not been implemented yet. See [Current Stage](#current-stage) below.

## Tech Stack

- **Language:** Python 3.13
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (`fastapi[standard]`)
- **Package manager:** [uv](https://docs.astral.sh/uv/)
- **Build backend:** `uv_build`

## Project Structure

```
task-management-application/
├── main.py                  # FastAPI app entry point
├── pyproject.toml           # Project metadata & dependencies
├── uv.lock                  # Locked dependency versions
├── .python-version          # Pinned Python version (3.13)
├── .env                     # Environment variables (currently empty)
└── src/
    ├── tasks/               # Task domain
    │   ├── __init__.py
    │   ├── models.py        # Task data models
    │   ├── dtos.py           # Request/response schemas
    │   ├── controller.py    # Business logic
    │   └── router.py        # API routes
    ├── user/                # User domain
    │   ├── __init__.py
    │   ├── models.py        # User data models
    │   ├── dtos.py           # Request/response schemas
    │   ├── controller.py    # Business logic
    │   └── router.py        # API routes
    └── utils/                # Shared utilities
        ├── __init__.py
        ├── db.py             # Database connection/setup
        ├── constant.py       # Shared constants
        └── helpers.py        # Helper functions
```

## Current Stage

Completed:

- Project initialized with `uv`, Python 3.13 pinned, `fastapi[standard]` installed as the sole dependency.
- Layered module structure scaffolded for two domains, `tasks` and `user`, each following a `models -> dtos -> controller -> router` pattern.
- Shared `utils` module scaffolded for database setup, constants, and helpers.

Outstanding:

- `main.py` only instantiates the FastAPI app; no routers are registered yet.
- All files under `src/` (`models.py`, `dtos.py`, `controller.py`, `router.py`, `db.py`, `constant.py`, `helpers.py`) are currently empty placeholders.
- No database connection, authentication, or business logic implemented yet.
- No tests yet.

The module skeleton is in place; the remaining work is implementing each layer.

## Getting Started

**Prerequisites:** Python 3.13+ and [uv](https://docs.astral.sh/uv/getting-started/installation/) installed.

```bash
# Clone the repository
git clone git@github.com:SyedTanzim/task-management-application.git
cd task-management-application

# Install dependencies
uv sync

# Run the development server
uv run fastapi dev main.py
```

Once running, the app will be available at `http://127.0.0.1:8000`, with interactive API docs at `http://127.0.0.1:8000/docs` (currently no endpoints are registered beyond the defaults).

## Author

**Tanzim** — syedtanzimwajih@gmail.com