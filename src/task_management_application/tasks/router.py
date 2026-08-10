from fastapi import APIRouter, Depends
from task_management_application.tasks import controller
from task_management_application.tasks.dtos import TaskSchema
from task_management_application.utils.db import get_db

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create")
def create_task(body:TaskSchema, db = Depends(get_db)):
    return controller.create_task(body, db)

@task_routes.get("/all_tasks")
def get_all_tasks(db = Depends(get_db)):
    return controller.get_task(db)

@task_routes.get("/all_tasks/{id}")
def get_a_task(id:int, db = Depends(get_db)):
    return controller.get_a_task(id, db)

@task_routes.delete("/delete_task/{id}")
def delete_task(id:int, db = Depends(get_db)):
    return controller.delete_task(id, db)

@task_routes.put("/update_task/{id}")
def update_task(body:TaskSchema, id:int, db = Depends(get_db)):
    return controller.update_task(body, id, db)