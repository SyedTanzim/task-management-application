import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import HTTPException, Request, status, Depends
from sqlalchemy.orm import Session
from task_management_application.utils.db import get_db
from task_management_application.utils.settings import settings
from task_management_application.user.models import UserModel

def is_authenticated(request: Request, db:Session = Depends(get_db)):
    try:
        token = request.headers.get("authorization")

        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")

        token = token.split(" ")[-1]

        data = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        
        user_id = (data.get("_id"))

        user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

        return user
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
