from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.models.task import Task

def get_task_by_id(db: Session, project_id: int, task_id: int) -> Task:
    task = db.query(Task).filter(Task.id == task_id, Task.project_id == project_id).first()
    if not task:
        raise NoResultFound("Task not found")
    return task
