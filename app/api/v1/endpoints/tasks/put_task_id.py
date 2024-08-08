from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.tasks.put_task_id import modify_task_in_project
from app.schemas.tasks.put_task_id import TaskUpdate, TaskOut
from sqlalchemy.exc import NoResultFound

router = APIRouter()

@router.put("/projects/{projectId}/tasks/{taskId}/", response_model=TaskOut, tags=["tasks"], summary="Update a task")
async def update_task(projectId: int, taskId: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    try:
        updated_task = modify_task_in_project(db, projectId, taskId, task_update)
        return updated_task
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Task not found")
