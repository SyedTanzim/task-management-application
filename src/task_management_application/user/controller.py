from fastapi import HTTPException
from pwdlib import PasswordHash
from sqlalchemy.orm import Session
from task_management_application.user.dtos import UserSchema
from task_management_application.user.models import UserModel

SECRET_KEY = "Ss0ZKnq8RiKT+02EkO9+mlG8CGUo5RFrnOEDHvhrj7E="
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)

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