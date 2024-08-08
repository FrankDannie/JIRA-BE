from sqlalchemy.orm import Session
from app.crud.notifications.put_notification import mark_notification_as_read
from app.schemas.notifications.get_notification import NotificationOut

def mark_notification_read_service(db: Session, notification_id: int) -> NotificationOut:
    notification = mark_notification_as_read(db, notification_id)
    if notification:
        return NotificationOut.from_orm(notification)
    else:
        raise ValueError("Notification not found or could not be updated")
