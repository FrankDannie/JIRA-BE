from sqlalchemy.orm import Session
from app.models.notification import Notification

def mark_notification_as_read(db: Session, notification_id: int) -> Notification:
    notification = db.query(Notification).filter(Notification.id == notification_id).first()
    if notification:
        notification.read = True
        db.commit()
        db.refresh(notification)
        return notification
    return None
