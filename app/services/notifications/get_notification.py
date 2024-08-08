from sqlalchemy.orm import Session
from app.crud.notifications.get_notification import get_notifications_for_user
from app.schemas.notifications.get_notification import NotificationOut

def retrieve_user_notifications(db: Session, user_id: int):
    notifications = get_notifications_for_user(db, user_id)
    return [NotificationOut.from_orm(notification) for notification in notifications]
