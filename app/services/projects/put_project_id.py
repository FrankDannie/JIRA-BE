from sqlalchemy.orm import Session
from app.crud.projects.put_project_id import update_project
from app.schemas.projects.put_project_id import ProjectUpdate, ProjectOut
from typing import Optional

def update_existing_project(db: Session, project_id: int, project_update: ProjectUpdate) -> Optional[ProjectOut]:
    updated_project = update_project(db, project_id, project_update.dict(exclude_unset=True))
    if updated_project:
        return ProjectOut.from_orm(updated_project)
    return None
