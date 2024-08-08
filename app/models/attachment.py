from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from datetime import datetime
from app.db.base import Base

class Attachment(Base):
    __tablename__ = "attachment"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    file_path = Column(String, nullable=False)
    task_id = Column(Integer, ForeignKey("task.id"), nullable=False)
    uploaded_by = Column(Integer, ForeignKey("user.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
