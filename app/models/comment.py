from sqlalchemy import Column, Text, DateTime, ForeignKey, String, Integer
from datetime import datetime
from app.db.base import Base

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(Text, nullable=False)
    task_id = Column(Integer, ForeignKey("task.id"), nullable=False)
    author_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
