from sqlalchemy import Column, String, Text, Date, DateTime, ForeignKey
from datetime import datetime
from app.db.base import Base
import uuid

class Project(Base):
    __tablename__ = "project"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True, nullable=False)
    description = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    created_by = Column(String, ForeignKey("user.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
