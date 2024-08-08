from sqlalchemy import Column, Text, DateTime, ForeignKey, String
from datetime import datetime
from app.db.base import Base
import uuid

class Comment(Base):
    __tablename__ = "comment"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    content = Column(Text, nullable=False)
    task_id = Column(String, ForeignKey("task.id"), nullable=False)
    author_id = Column(String, ForeignKey("user.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
