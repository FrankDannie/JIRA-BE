from app.schemas.notifications.get_notification import NotificationOut
from app.services.authentication.user_get import get_current_user
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.notifications.get_notification import retrieve_user_notifications

router = APIRouter()

@router.get("/notifications/", response_model=list[NotificationOut], tags=["notifications"], summary="Get all notifications for the user")
async def get_all_notifications(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    try:
        return retrieve_user_notifications(db, current_user.id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
