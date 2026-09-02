from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    userName: str
    password: str
    email: str