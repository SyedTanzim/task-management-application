from task_management_application.user.dtos import UserSchema
from sqlalchemy.orm import Session

def register(body:UserSchema, db:Session):
    return {"msg":"User registered"}