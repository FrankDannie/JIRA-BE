from pydantic import BaseModel
from datetime import date, datetime

class ProjectOut(BaseModel):
    id: int
    name: str
    description: str
    start_date: date
    end_date: date
    created_by: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        from_attributes = True
