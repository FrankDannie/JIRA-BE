from pydantic import BaseModel
from datetime import datetime

class CommentOut(BaseModel):
    id: int
    content: str
    task_id: int
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True
