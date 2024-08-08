from sqlalchemy.orm import Session
from app.models.attachment import Attachment

def create_attachment(db: Session, file_path: str, task_id: int, user_id: int) -> Attachment:
    attachment = Attachment(
        file_path=file_path,
        task_id=task_id,
        uploaded_by=user_id,
    )
    db.add(attachment)
    db.commit()
    db.refresh(attachment)
    return attachment
