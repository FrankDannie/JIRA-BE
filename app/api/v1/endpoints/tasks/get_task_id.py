from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.tasks.get_task_id import get_task_details
from app.schemas.tasks.get_task_id import TaskOut
from sqlalchemy.exc import NoResultFound

router = APIRouter()

@router.get("/projects/{projectId}/tasks/{taskId}/", response_model=TaskOut, tags=["tasks"], summary="Get task details")
async def get_task(projectId: int, taskId: int, db: Session = Depends(get_db)):
    try:
        task = get_task_details(db, projectId, taskId)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
