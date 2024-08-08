from typing import Optional
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.tasks.post_tasks import TaskCreate

def create_task(db: Session, task_create: TaskCreate, project_id: int, user_id: Optional[int] = None) -> Task:
    db_task = Task(
        title=task_create.title,
        description=task_create.description,
        status=task_create.status,
        priority=task_create.priority,
        deadline=task_create.deadline,
        project_id=project_id,
        assigned_to=user_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
