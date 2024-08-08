from app.services.authentication.user_get import get_current_user
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.attachments.delete_attachments import delete_attachment_service

router = APIRouter()

@router.delete("/projects/{projectId}/tasks/{taskId}/attachments/{attachmentId}/", status_code=204, tags=["attachments"], summary="Delete a file attachment")
async def delete_file_attachment(projectId: int, taskId: int, attachmentId: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    if not delete_attachment_service(db, attachmentId):
        raise HTTPException(status_code=404, detail="Attachment not found or could not be deleted")