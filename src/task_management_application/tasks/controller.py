from task_management_application.tasks.dtos import TaskSchema
from sqlalchemy.orm import session
from task_management_application.tasks.models import TaskModel
from fastapi import HTTPException
from task_management_application.user.models import UserModel

def create_task(body:TaskSchema, db:session, user:UserModel):
    data = body.model_dump()

    new_task = TaskModel(
        title = data["title"],
        description = data["description"],
        is_completed = data["is_completed"],
        user_id = user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

def get_all_task(db:session, user:UserModel):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    return tasks

def get_a_task(id:int, db:session, user:UserModel):
    task = db.get(TaskModel, id)

    if not task:
        raise HTTPException(404, detail="Task not found")

    if task.user_id != user.id:
        raise HTTPException(401, detail="You do not have permission to access this task")
    
    return task

def update_task(body: TaskSchema, id: int, db: session, user:UserModel):
    task = db.get(TaskModel, id)

    if not task:
        raise HTTPException(404, detail="Task not found")

    if task.user_id != user.id:
        raise HTTPException(401, detail="You do not have permission to update this task")

    body_data = body.model_dump()

    for field, value in body_data.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return task

def delete_task(id: int, db: session, user:UserModel):
    task = db.get(TaskModel, id)

    if not task:
        raise HTTPException(404, detail="Task not found")

    if task.user_id != user.id:
        raise HTTPException(401, detail="You do not have permission to delete this task")

    db.delete(task)
    db.commit()

    return None