from sqlalchemy.orm import Session
from app.crud.tasks.get_task_id import get_task_by_id
from app.schemas.tasks.get_task_id import TaskOut

def get_task_details(db: Session, project_id: int, task_id: int) -> TaskOut:
    task = get_task_by_id(db, project_id, task_id)
    return TaskOut.from_orm(task)
