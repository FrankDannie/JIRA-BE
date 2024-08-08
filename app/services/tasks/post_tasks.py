from sqlalchemy.orm import Session
from app.crud.tasks.post_tasks import create_task
from app.schemas.tasks.post_tasks import TaskCreate, TaskOut
from typing import Optional

def add_task_to_project(db: Session, project_id: int, task_create: TaskCreate, user_id: Optional[int] = None) -> TaskOut:
    created_task = create_task(db, task_create, project_id, user_id)
    return TaskOut.from_orm(created_task)
