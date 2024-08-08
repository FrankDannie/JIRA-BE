from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.authentication.auth_sign_in import UserCreate
from app.core.security import get_password_hash

def auth_sign_in(db: Session, user_in: UserCreate) -> User:
    hashed_password = get_password_hash(user_in.password)
    user = User(
        username=user_in.username,
        email=user_in.email,
        hashed_password=hashed_password,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
