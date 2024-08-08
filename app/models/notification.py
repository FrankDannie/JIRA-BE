from sqlalchemy import Column, String, Text, Boolean, DateTime, ForeignKey
from datetime import datetime
from app.db.base import Base
import uuid

class Notification(Base):
    __tablename__ = "notification"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    content = Column(Text, nullable=False)
    user_id = Column(String, ForeignKey("user.id"), nullable=False)  # Also store UUIDs as strings
    read = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
