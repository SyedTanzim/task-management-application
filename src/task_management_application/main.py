from fastapi import FastAPI
from task_management_application.utils.db import base, engine
from task_management_application.tasks.models import TaskModel
from task_management_application.tasks.router import task_routes
from task_management_application.user.router import user_routes

base.metadata.create_all(engine)

app = FastAPI(title="Task Management Application")
app.include_router(task_routes)
app.include_router(user_routes)