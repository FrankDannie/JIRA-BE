from sqlalchemy.orm import Session
from app.crud.projects.projects_post import create_project
from app.schemas.projects.projects_post import ProjectCreate, ProjectOut

def create_new_project(db: Session, project: ProjectCreate, user_id: int) -> ProjectOut:
    db_project = create_project(db, project, user_id)
    return ProjectOut.from_orm(db_project)
