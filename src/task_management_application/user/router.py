from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from task_management_application.user.dtos import UserSchema
from task_management_application.utils.db import get_db
from task_management_application.user import controller 


user_routes = APIRouter(prefix="/user")

@user_routes.post("/register", status_code=status.HTTP_201_CREATED)
def register(body:UserSchema, db:Session=Depends(get_db)):
    return controller.register(body, db)
