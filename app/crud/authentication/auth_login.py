from sqlalchemy.orm import Session
from app.models.user import User

def get_user_by_username(db: Session, username: str) -> User:
    result = db.query(User).filter(User.username == username).first()
    return result