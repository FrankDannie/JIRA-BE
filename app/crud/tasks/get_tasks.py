from sqlalchemy.orm import Session
from app.models.task import Task
from typing import List

def get_tasks_by_project(db: Session, project_id: int) -> List[Task]:
    return db.query(Task).filter(Task.project_id == project_id).all()
