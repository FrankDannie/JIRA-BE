import os
from sqlalchemy.orm import Session
from app.crud.attachments.delete_attachments import delete_attachment
from app.models.attachment import Attachment

def remove_file(file_path: str) -> None:
    if os.path.exists(file_path):
        os.remove(file_path)

def delete_attachment_service(db: Session, attachment_id: int) -> bool:
    attachment = db.query(Attachment).filter(Attachment.id == attachment_id).first()
    if attachment:
        remove_file(attachment.file_path)
        return delete_attachment(db, attachment_id)
    return False
