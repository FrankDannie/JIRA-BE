from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.tasks.get_tasks import fetch_tasks_for_project
from app.schemas.tasks.get_tasks import TaskOut

router = APIRouter()

@router.get("/projects/{projectId}/tasks/", response_model=List[TaskOut], tags=["tasks"], summary="Get all tasks for a project")
async def get_tasks(projectId: int, db: Session = Depends(get_db)):
    tasks = fetch_tasks_for_project(db, projectId)
    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this project")
    return tasks
