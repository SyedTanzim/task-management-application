from sqlalchemy import Column, ForeignKey, Integer, Boolean, DateTime, String
from task_management_application.utils.db import base

class UserModel(base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    userName = Column(String, nullable = False)
    hash_password = Column(String, nullable = False)
    email = Column(String)