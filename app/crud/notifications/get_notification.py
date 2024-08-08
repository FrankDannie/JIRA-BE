from sqlalchemy.orm import Session
from app.models.notification import Notification

def get_notifications_for_user(db: Session, user_id: int):
    return db.query(Notification).filter(Notification.user_id == user_id).all()
