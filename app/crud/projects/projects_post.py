from datetime import datetime
from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.projects.projects_post import ProjectCreate

def create_project(db: Session, project: ProjectCreate, user_id: int) -> Project:
    db_project = Project(
        name=project.name,
        description=project.description,
        start_date=project.start_date,
        end_date=project.end_date,
        created_by=user_id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project
