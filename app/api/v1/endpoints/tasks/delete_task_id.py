from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.tasks.delete_task_id import remove_task_from_project

router = APIRouter()

@router.delete("/projects/{projectId}/tasks/{taskId}/", status_code=204, tags=["tasks"], summary="Delete a task")
async def delete_task(projectId: int, taskId: int, db: Session = Depends(get_db)):
    if not remove_task_from_project(db, taskId):
        raise HTTPException(status_code=404, detail="Task not found")
