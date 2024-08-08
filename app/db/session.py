from sqlalchemy.orm import Session
from .base import SessionLocal

def get_db() -> Session:
    """
    Dependency that provides a database session for FastAPI routes.

    Yields:
        Session: An SQLAlchemy database session.

    Closes the session after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
