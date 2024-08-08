from sqlalchemy.orm import Session
from app.crud.comments.post_comment import create_comment
from app.schemas.comments.post_comment import CommentCreate, CommentOut
from typing import Optional

def add_comment_to_task(db: Session, task_id: int, comment_create: CommentCreate, author_id: int) -> CommentOut:
    created_comment = create_comment(db, comment_create, task_id, author_id)
    return CommentOut.from_orm(created_comment)
