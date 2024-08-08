from app.services.authentication.user_get import get_current_user
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.attachments.post_attachments import upload_attachment
from app.schemas.attachments.post_attachments import AttachmentOut

router = APIRouter()

@router.post("/projects/{projectId}/tasks/{taskId}/attachments/", response_model=AttachmentOut, tags=["attachments"], summary="Upload a file attachment")
async def upload_file_attachment(projectId: int, taskId: int, file: UploadFile = File(...), db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    try:
        return upload_attachment(db, file, taskId, current_user.id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
