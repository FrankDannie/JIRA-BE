from pydantic import BaseModel
from datetime import datetime

class CommentUpdate(BaseModel):
    content: str

class CommentOut(BaseModel):
    id: int
    content: str
    task_id: int
    author_id: str
    created_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True
