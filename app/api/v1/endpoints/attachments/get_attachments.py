from app.services.authentication.user_get import get_current_user
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.attachments.get_attachments import fetch_attachment
from app.schemas.attachments.get_attachments import AttachmentOut

router = APIRouter()

@router.get("/projects/{projectId}/tasks/{taskId}/attachments/", response_model=AttachmentOut, tags=["attachments"], summary="Get a file attachment")
async def get_file_attachment(projectId: int, taskId: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    try:
        return fetch_attachment(db, projectId, taskId)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
