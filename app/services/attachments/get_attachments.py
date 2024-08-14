from sqlalchemy.orm import Session
from app.crud.attachments.get_attachments import get_attachment
from app.schemas.attachments.get_attachments import AttachmentOut

def fetch_attachment(db: Session, projectId: int, taskId: int) -> AttachmentOut:
    attachment = get_attachment(db, projectId, taskId)
    return AttachmentOut.from_orm(attachment)
