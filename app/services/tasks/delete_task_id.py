from sqlalchemy.orm import Session
from app.crud.tasks.delete_task_id import delete_task

def remove_task_from_project(db: Session, task_id: int) -> bool:
    return delete_task(db, task_id)
