from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    userName: str
    password: str
    email: str


class UserResponseSchema(BaseModel):
    id: int
    email: str
    name: str
    userName: str

class loginSchema(BaseModel):
    userName: str
    password: str