from sqlalchemy.orm import Session
from app.crud.tasks.get_tasks import get_tasks_by_project
from app.schemas.tasks.get_tasks import TaskOut
from typing import List

def fetch_tasks_for_project(db: Session, project_id: int) -> List[TaskOut]:
    tasks = get_tasks_by_project(db, project_id)
    return [TaskOut.from_orm(task) for task in tasks]
