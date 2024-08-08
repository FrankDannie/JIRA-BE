from datetime import datetime
from sqlalchemy.orm import Session
from app.models.project import Project
from typing import Optional

def update_project(db: Session, project_id: int, project_update: dict) -> Optional[Project]:
    db_project = db.query(Project).filter(Project.id == project_id).first()
    if db_project:
        for key, value in project_update.items():
            setattr(db_project, key, value)
        db_project.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(db_project)
        return db_project
    return None
