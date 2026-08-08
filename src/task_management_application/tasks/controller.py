from task_management_application.tasks.dtos import TaskSchema
from sqlalchemy.orm import session
from task_management_application.tasks.models import TaskModel

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