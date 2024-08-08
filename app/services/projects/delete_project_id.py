from sqlalchemy.orm import Session
from app.crud.projects.delete_project_id import delete_project

def remove_project(db: Session, project_id: int) -> bool:
    return delete_project(db, project_id)
