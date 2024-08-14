from sqlalchemy.orm import Session
from app.models.attachment import Attachment
from fastapi import HTTPException, status

def get_attachment(db: Session, projectId: int, taskId: int) -> Attachment:
    attachment = db.query(Attachment).filter(Attachment.task_id == taskId).all()
    if not attachment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Attachment not found")
    return attachment
