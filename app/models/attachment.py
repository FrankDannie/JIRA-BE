from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime
from app.db.base import Base
import uuid

class Attachment(Base):
    __tablename__ = "attachment"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    file_path = Column(String, nullable=False)
    task_id = Column(String, ForeignKey("task.id"), nullable=False)
    uploaded_by = Column(String, ForeignKey("user.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
