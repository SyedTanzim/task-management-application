from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from task_management_application.utils.settings import settings

base = declarative_base()
engine = create_engine(url=settings.db_connection)

localSession = sessionmaker(bind=engine)

def get_db():
    session = localSession()
    try:
        yield session
    finally:
        session.close()