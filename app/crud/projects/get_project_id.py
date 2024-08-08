from sqlalchemy.orm import Session
from app.models.project import Project

def get_project(db: Session, project_id: int) -> Project:
    return db.query(Project).filter(Project.id == project_id).first()
