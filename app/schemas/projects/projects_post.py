from pydantic import BaseModel
from datetime import date, datetime
from typing import List

class ProjectCreate(BaseModel):
    name: str
    description: str
    start_date: date
    end_date: date

class ProjectOut(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
    created_by: str
    start_date: date
    end_date: date

    class Config:
        orm_mode = True
        from_attributes = True
