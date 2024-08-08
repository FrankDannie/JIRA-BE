from sqlalchemy import Column, String, Text, Boolean, DateTime, ForeignKey, Integer
from datetime import datetime
from app.db.base import Base

class Notification(Base):
    __tablename__ = "notification"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)  # Also store UUIDs as strings
    read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
