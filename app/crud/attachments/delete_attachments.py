from sqlalchemy.orm import Session
from app.models.attachment import Attachment

def delete_attachment(db: Session, attachment_id: int) -> bool:
    attachment = db.query(Attachment).filter(Attachment.id == attachment_id).first()
    if attachment:
        db.delete(attachment)
        db.commit()
        return True
    return False
