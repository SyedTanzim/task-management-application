from task_management_application.tasks.dtos import TaskSchema
from sqlalchemy.orm import session
from task_management_application.tasks.models import TaskModel
from fastapi import HTTPException

def create_task(body:TaskSchema, db:session):
    data = body.model_dump()

    new_task = TaskModel(
        title = data["title"],
        description = data["description"],
        is_completed = data["is_completed"]
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {"status": "Task is created", "data":new_task}

def get_task(db:session):
    tasks = db.query(TaskModel).all()
    return {"status":"All Tasks", "data":tasks}

def get_a_task(id:int, db:session):
    task = db.get(TaskModel, id)

    if not task:
        raise HTTPException(404, detail="Task Not Found")
    
    return {"status": "Task Found", "data": task}

def delete_task(id: int, db: session):
    task = db.get(TaskModel, id)

    if not task:
        raise HTTPException(404, detail="Task Not Found")

    db.delete(task)
    db.commit()

    return {"status": "Task Deleted"}

def update_task(body: TaskSchema, id: int, db: session):
    task = db.get(TaskModel, id)

    if not task:
        raise HTTPException(404, detail="Task Not Found")

    body_data = body.model_dump()

    for field, value in body_data.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return {
        "status": "Task Updated Successfully",
        "data": task
    }