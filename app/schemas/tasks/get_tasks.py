from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str
    priority: str
    deadline: Optional[date]
    project_id: int
    assigned_to: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True
