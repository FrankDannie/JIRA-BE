from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.comments.get_comment import retrieve_comments_for_task
from app.schemas.comments.get_comment import CommentOut

router = APIRouter()

@router.get("/projects/{projectId}/tasks/{taskId}/comments/", response_model=list[CommentOut], tags=["comments"], summary="Get all comments for a task")
async def get_comments_for_task(projectId: int, taskId: int, db: Session = Depends(get_db)):
    comments = retrieve_comments_for_task(db, taskId)
    if comments is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return comments
