# Task Management Application
 
A task management backend built with **FastAPI** and **Python 3.13**, managed with **uv**.
 
**Status:** Early scaffold. The project structure is in place, but the core logic (models, routes, database) has not been implemented yet. See [Current Stage](#current-stage) below.
 
## Tech Stack
 
- **Language:** Python 3.13
- **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (`fastapi[standard]`)
- **Database:** PostgreSQL, via [SQLAlchemy](https://www.sqlalchemy.org/) ORM and the [psycopg](https://www.psycopg.org/) driver
- **Configuration:** [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) (loads settings from `.env`)
- **Package manager:** [uv](https://docs.astral.sh/uv/)
- **Build backend:** `uv_build`
## Project Structure
 
```
task-management-application/
├── pyproject.toml                      # Project metadata & dependencies
├── uv.lock                             # Locked dependency versions
├── .python-version                     # Pinned Python version (3.13)
├── .env                                # Environment variables (db_connection)
└── src/
    └── task_management_application/
        ├── __init__.py
        ├── main.py                     # FastAPI app entry point
        ├── tasks/                      # Task domain
        │   ├── __init__.py
        │   ├── models.py               # Task ORM model
        │   ├── dtos.py                 # Request/response schemas
        │   ├── controller.py           # Business logic
        │   └── router.py               # API routes
        ├── user/                       # User domain
        │   ├── __init__.py
        │   ├── models.py               # User data models
        │   ├── dtos.py                 # Request/response schemas
        │   ├── controller.py           # Business logic
        │   └── router.py               # API routes
        └── utils/                      # Shared utilities
            ├── __init__.py
            ├── db.py                   # Database engine, session, base
            ├── settings.py             # Environment-based settings
            ├── constant.py             # Shared constants
            └── helpers.py              # Helper functions
```
 
## Current Stage
 
Completed:
 
- Project restructured into a proper `src/task_management_application` package.
- PostgreSQL database connection configured via SQLAlchemy: engine, session factory, and declarative base set up in `utils/db.py`, with connection settings loaded from `.env` through `utils/settings.py`.
- `main.py` creates all database tables on startup and registers the tasks router.
- Tasks module implemented end to end: `TaskModel` (ORM model), `TaskSchema` (pydantic schema), a `create_task` controller function, and a `POST /tasks/create` endpoint to create a task.
Outstanding:
 
- User module (`models.py`, `dtos.py`, `controller.py`, `router.py`) is still scaffolded but empty; no user endpoints or router are registered on the app yet.
- `utils/constant.py` and `utils/helpers.py` are still empty.
- Only task creation is implemented; there are no endpoints yet to list, retrieve, update, or delete tasks.
- No authentication yet.
- No tests yet.
## Current API Endpoints
 
| Method | Path            | Description       |
|--------|-----------------|--------------------|
| POST   | `/tasks/create` | Create a new task |
 
## Getting Started
 
**Prerequisites:** Python 3.13+, [uv](https://docs.astral.sh/uv/getting-started/installation/), and a running PostgreSQL instance.
 
```bash
# Clone the repository
git clone git@github.com:SyedTanzim/task-management-application.git
cd task-management-application
 
# Install dependencies
uv sync
```
 
Create a `.env` file in the project root with a PostgreSQL connection string:
 
```
db_connection=postgresql+psycopg://<user>:<password>@<host>:<port>/<database>
```
 
```bash
# Run the development server
uv run fastapi dev src/task_management_application/main.py
```
 
Once running, the app will be available at `http://127.0.0.1:8000`, with interactive API docs at `http://127.0.0.1:8000/docs`. On startup, the app creates any missing database tables automatically.
 
## Roadmap
 
- Define `User` and `Task` models
- Implement DTOs/schemas for request and response validation
- Implement controller logic for tasks and users
- Define routers and register them on the FastAPI app in `main.py`
- Set up database connection in `utils/db.py`
- Add authentication
- Add tests
## Roadmap
 
- Add endpoints to list, retrieve, update, and delete tasks
- Implement the user module (model, schema, controller, router) and register it on the app
- Add authentication
- Populate `utils/constant.py` and `utils/helpers.py` as shared logic emerges
- Add tests
## Author
 
**Tanzim** — syedtanzimwajih@gmail.com