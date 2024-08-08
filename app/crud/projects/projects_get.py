from sqlalchemy.orm import Session
from app.models.project import Project

def get_all_projects(db: Session):
    return db.query(Project).all()
