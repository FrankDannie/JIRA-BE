from sqlalchemy.orm import Session
from app.crud.projects.get_project_id import get_project
from app.schemas.projects.get_project_id import ProjectOut

def get_project_by_id(db: Session, project_id: int) -> ProjectOut:
    project = get_project(db, project_id)
    if project is None:
        return None
    return ProjectOut.from_orm(project)
