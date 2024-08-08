from pydantic import BaseModel
from datetime import datetime
from typing import List

class ProjectOut(BaseModel):
    id: str
    name: str
    description: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True
