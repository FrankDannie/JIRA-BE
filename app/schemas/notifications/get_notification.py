from pydantic import BaseModel
from datetime import datetime

class NotificationOut(BaseModel):
    id: int
    content: str
    user_id: int
    read: bool
    created_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True
