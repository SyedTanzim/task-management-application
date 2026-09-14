import jwt
from pwdlib import PasswordHash
from fastapi import HTTPException, status, Request
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from task_management_application.utils.settings import settings
from task_management_application.user.dtos import UserSchema, loginSchema
from task_management_application.user.models import UserModel
from task_management_application.utils.helpers import is_authenticated

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def register(body:UserSchema, db:Session):
    existing_user = db.query(UserModel).filter(UserModel.userName == body.userName).first()
    if existing_user:
        raise HTTPException (400, detail = "Username already exists.")

    existing_email = db.query(UserModel).filter(UserModel.email == body.email).first()
    if existing_email:
        raise HTTPException (400, detail = "Email already exists.")

    hashed_password = get_password_hash(body.password)

    new_user = UserModel(
        name = body.name,
        userName = body.userName,
        hash_password = hashed_password,
        email = body.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login_user(body:loginSchema, db:Session):
    user = db.query(UserModel).filter(UserModel.userName == body.userName).first()

    if not user:
        raise HTTPException (status_code=status.HTTP_401_UNAUTHORIZED, detail = "Invalid username or password")

    if not verify_password(body.password, user.hash_password):
        raise HTTPException (status_code=status.HTTP_401_UNAUTHORIZED, detail = "Invalid username or password")

    expire_time = datetime.now() + timedelta(minutes = settings.expire_time)

    token = jwt.encode({"_id":user.id, "exp": expire_time.timestamp()}, settings.secret_key, algorithm=settings.algorithm)

    return {"token":token}