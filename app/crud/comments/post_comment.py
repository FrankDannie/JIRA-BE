from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.schemas.comments.post_comment import CommentCreate

def create_comment(db: Session, comment_create: CommentCreate, task_id: int, author_id: int) -> Comment:
    db_comment = Comment(
        content=comment_create.content,
        task_id=task_id,
        author_id=author_id
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
