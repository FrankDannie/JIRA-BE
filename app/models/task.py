from sqlalchemy import Column, String, Text, Date, DateTime, ForeignKey, Integer
from datetime import datetime
from app.db.base import Base

class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text)
    status = Column(String, nullable=False, default="To Do")
    priority = Column(String, nullable=False, default="Medium")
    deadline = Column(Date)
    project_id = Column(Integer, ForeignKey("project.id"), nullable=False)
    assigned_to = Column(Integer, ForeignKey("user.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
