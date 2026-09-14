from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from task_management_application.tasks import controller
from task_management_application.tasks.dtos import TaskSchema
from task_management_application.tasks.dtos import TaskResponseSchema
from task_management_application.utils.db import get_db
from task_management_application.user.models import UserModel
from task_management_application.utils.helpers import is_authenticated

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create", response_model = TaskResponseSchema, status_code = status.HTTP_201_CREATED)
def create_task(body:TaskSchema, db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.create_task(body, db)

@task_routes.get("/all_tasks", response_model = List[TaskResponseSchema], status_code = status.HTTP_200_OK)
def get_all_tasks(db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.get_all_task(db)

@task_routes.get("/all_tasks/{id}", response_model = TaskResponseSchema, status_code = status.HTTP_200_OK)
def get_a_task(id:int, db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.get_a_task(id, db)

@task_routes.put("/update_task/{id}", response_model = TaskResponseSchema, status_code = status.HTTP_200_OK)
def update_task(body:TaskSchema, id:int, db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.update_task(body, id, db)

@task_routes.delete("/delete_task/{id}", response_model = None, status_code = status.HTTP_204_NO_CONTENT)
def delete_task(id:int, db:Session = Depends(get_db), user:UserModel = Depends(is_authenticated)):
    return controller.delete_task(id, db)