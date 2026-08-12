from fastapi import APIRouter, Depends, status
from task_management_application.tasks import controller
from task_management_application.tasks.dtos import TaskSchema
from task_management_application.tasks.dtos import TaskResponseSchema
from task_management_application.utils.db import get_db
from sqlalchemy.orm import Session
from typing import List

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create", response_model = TaskResponseSchema, status_code = status.HTTP_201_CREATED)
def create_task(body:TaskSchema, db:Session = Depends(get_db)):
    return controller.create_task(body, db)

@task_routes.get("/all_tasks", response_model = List[TaskResponseSchema], status_code = status.HTTP_200_OK)
def get_all_tasks(db:Session = Depends(get_db)):
    return controller.get_all_task(db)

@task_routes.get("/all_tasks/{id}", response_model = TaskResponseSchema, status_code = status.HTTP_200_OK)
def get_a_task(id:int, db:Session = Depends(get_db)):
    return controller.get_a_task(id, db)

@task_routes.put("/update_task/{id}", response_model = TaskResponseSchema, status_code = status.HTTP_200_OK)
def update_task(body:TaskSchema, id:int, db:Session = Depends(get_db)):
    return controller.update_task(body, id, db)

@task_routes.delete("/delete_task/{id}", response_model = None, status_code = status.HTTP_204_NO_CONTENT)
def delete_task(id:int, db:Session = Depends(get_db)):
    return controller.delete_task(id, db)