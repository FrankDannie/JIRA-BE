from app.services.authentication.user_get import get_current_user
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.comments.post_comment import add_comment_to_task
from app.schemas.comments.post_comment import CommentCreate, CommentOut
from typing import Optional
from app.models.user import User

router = APIRouter()

@router.post("/projects/{projectId}/tasks/{taskId}/comments/", response_model=CommentOut, tags=["comments"], summary="Create a new comment")
async def create_comment(projectId: int, taskId: int, comment_create: CommentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    created_comment = add_comment_to_task(db, taskId, comment_create, current_user.username)
    if not created_comment:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return created_comment
