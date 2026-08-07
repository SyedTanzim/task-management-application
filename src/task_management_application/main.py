from fastapi import FastAPI
from task_management_application.utils.db import base, engine

base.metadata.create_all(engine)

app = FastAPI(title="Task Management Application")