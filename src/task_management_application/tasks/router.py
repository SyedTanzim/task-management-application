from fastapi import APIRouter, Depends
from task_management_application.tasks import controller
from task_management_application.tasks.dtos import TaskSchema
from task_management_application.utils.db import get_db

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create")
def create_task(body:TaskSchema, db = Depends(get_db)):
    return controller.create_task(body, db)