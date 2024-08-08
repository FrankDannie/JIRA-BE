from sqlalchemy.orm import Session
from app.crud.projects.projects_get import get_all_projects
from app.schemas.projects.projects_get import ProjectOut
from typing import List

def fetch_all_projects(db: Session) -> List[ProjectOut]:
    projects = get_all_projects(db)
    print(projects)
    return [ProjectOut.from_orm(project) for project in projects]
