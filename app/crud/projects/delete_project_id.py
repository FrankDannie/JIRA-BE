from sqlalchemy.orm import Session
from app.models.project import Project
from sqlalchemy.exc import NoResultFound

def delete_project(db: Session, project_id: int) -> bool:
    try:
        db_project = db.query(Project).filter(Project.id == project_id).one()
        db.delete(db_project)
        db.commit()
        return True
    except NoResultFound:
        return False
