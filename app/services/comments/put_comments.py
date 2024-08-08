from sqlalchemy.orm import Session
from app.crud.comments.put_comments import update_comment
from app.schemas.comments.put_comments import CommentUpdate, CommentOut

def edit_comment(db: Session, comment_id: int, comment_update: CommentUpdate) -> CommentOut:
    updated_comment = update_comment(db, comment_id, comment_update)
    if updated_comment:
        return CommentOut.from_orm(updated_comment)
    return None
