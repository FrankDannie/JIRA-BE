from sqlalchemy.orm import Session
from app.crud.tasks.put_task_id import update_task
from app.schemas.tasks.put_task_id import TaskUpdate, TaskOut
from typing import Optional

def modify_task_in_project(db: Session, project_id: int, task_id: int, task_update: TaskUpdate) -> TaskOut:
    updated_task = update_task(db, project_id, task_id, task_update)
    return TaskOut.from_orm(updated_task)
