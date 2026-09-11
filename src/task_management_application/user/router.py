from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from task_management_application.user.dtos import UserSchema, UserResponseSchema, loginSchema
from task_management_application.utils.db import get_db
from task_management_application.user import controller 

user_routes = APIRouter(prefix="/user")

@user_routes.post("/register",  response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED)
def register(body:UserSchema, db:Session=Depends(get_db)):
    return controller.register(body, db)

@user_routes.post("/login", status_code=status.HTTP_200_OK)
def login(body:loginSchema, db:Session=Depends(get_db)):
    return controller.login_user(body, db)
