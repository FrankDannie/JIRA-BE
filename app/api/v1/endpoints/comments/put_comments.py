from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.comments.put_comments import edit_comment
from app.schemas.comments.put_comments import CommentUpdate, CommentOut

router = APIRouter()

@router.put("/projects/{projectId}/tasks/{taskId}/comments/{commentId}/", response_model=CommentOut, tags=["comments"], summary="Update a new comment")
async def update_comment(projectId: int, taskId: int, commentId: int, comment_update: CommentUpdate, db: Session = Depends(get_db)):
    updated_comment = edit_comment(db, commentId, comment_update)
    if not updated_comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return updated_comment
