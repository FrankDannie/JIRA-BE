from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.models.comment import Comment
from app.schemas.comments.put_comments import CommentUpdate

def update_comment(db: Session, comment_id: int, comment_update: CommentUpdate) -> Comment:
    try:
        comment = db.query(Comment).filter(Comment.id == comment_id).one()
        comment.content = comment_update.content
        db.commit()
        db.refresh(comment)
        return comment
    except NoResultFound:
        db.rollback()
        return None
