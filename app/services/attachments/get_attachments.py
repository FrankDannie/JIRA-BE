from sqlalchemy.orm import Session
from app.crud.attachments.get_attachments import get_attachment
from app.schemas.attachments.get_attachments import AttachmentOut

def fetch_attachment(db: Session, attachment_id: int) -> AttachmentOut:
    attachment = get_attachment(db, attachment_id)
    return AttachmentOut.from_orm(attachment)
