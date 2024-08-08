from sqlalchemy import Column, String, Text, Date, DateTime, ForeignKey
from datetime import datetime
from app.db.base import Base
import uuid

class Task(Base):
    __tablename__ = "task"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, index=True, nullable=False)
    description = Column(Text)
    status = Column(String, nullable=False, default="To Do")
    priority = Column(String, nullable=False, default="Medium")
    deadline = Column(Date)
    project_id = Column(String, ForeignKey("project.id"), nullable=False)
    assigned_to = Column(String, ForeignKey("user.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
