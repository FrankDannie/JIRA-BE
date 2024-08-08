from app.services.authentication.user_get import get_current_user
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.notifications.put_notification import mark_notification_read_service
from app.schemas.notifications.get_notification import NotificationOut

router = APIRouter()

@router.put("/notifications/{notificationId}/", response_model=NotificationOut, tags=["notifications"], summary="Mark a notification as read")
async def mark_notification_as_read(notificationId: int, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    try:
        return mark_notification_read_service(db, notificationId)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
