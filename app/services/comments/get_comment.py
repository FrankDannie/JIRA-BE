from sqlalchemy.orm import Session
from app.crud.comments.get_comment import get_comments_by_task
from app.schemas.comments.get_comment import CommentOut  # Make sure you have this schema defined

def retrieve_comments_for_task(db: Session, task_id: int):
    comments = get_comments_by_task(db, task_id)
    return [CommentOut.from_orm(comment) for comment in comments]
