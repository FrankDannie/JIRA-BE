from pydantic import BaseModel
from datetime import datetime

class AttachmentOut(BaseModel):
    id: int
    file_path: str
    task_id: int
    uploaded_by: int
    created_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True
