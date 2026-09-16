from sqlalchemy import Column, ForeignKey, Integer, Boolean, String
from task_management_application.utils.db import base

class TaskModel(base):
    __tablename__ = "user_task"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean, default=False)

    user_id = Column(Integer, ForeignKey("user_table.id", ondelete="CASCADE"), nullable=False)