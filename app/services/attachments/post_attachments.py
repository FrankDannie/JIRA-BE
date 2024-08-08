import os
from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.crud.attachments.post_attachments import create_attachment
from app.schemas.attachments.post_attachments import AttachmentOut

UPLOAD_DIR = "uploads/"  # Directory to store uploaded files

def save_file(file: UploadFile) -> str:
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return file_path

def upload_attachment(db: Session, file: UploadFile, task_id: int, user_id: int) -> AttachmentOut:
    file_path = save_file(file)
    attachment = create_attachment(db, file_path, task_id, user_id)
    return AttachmentOut.from_orm(attachment)
