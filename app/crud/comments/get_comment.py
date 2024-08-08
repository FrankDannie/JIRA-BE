from sqlalchemy.orm import Session
from app.models.comment import Comment

def get_comments_by_task(db: Session, task_id: int):
    return db.query(Comment).filter(Comment.task_id == task_id).all()
