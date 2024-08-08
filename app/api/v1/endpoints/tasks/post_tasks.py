from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.tasks.post_tasks import add_task_to_project
from app.schemas.tasks.post_tasks import TaskCreate, TaskOut
from typing import Optional

router = APIRouter()

@router.post("/projects/{projectId}/tasks/", response_model=TaskOut, tags=["tasks"], summary="Create a new task")
async def create_task(projectId: int, task_create: TaskCreate, db: Session = Depends(get_db), user_id: Optional[int] = None):
    created_task = add_task_to_project(db, projectId, task_create, user_id)
    if not created_task:
        raise HTTPException(status_code=404, detail="Project not found")
    return created_task
