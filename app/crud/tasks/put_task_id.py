from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.tasks.put_task_id import TaskUpdate
from sqlalchemy.exc import NoResultFound

def update_task(db: Session, project_id: int, task_id: int, task_update: TaskUpdate) -> Task:
    db_task = db.query(Task).filter(Task.id == task_id, Task.project_id == project_id).first()
    if not db_task:
        raise NoResultFound("Task not found")

    for field, value in task_update.dict(exclude_unset=True).items():
        setattr(db_task, field, value)

    db.commit()
    db.refresh(db_task)
    return db_task
