from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.models.task import Task

def delete_task(db: Session, task_id: int) -> bool:
    try:
        task = db.query(Task).filter(Task.id == task_id).one()
        db.delete(task)
        db.commit()
        return True
    except NoResultFound:
        db.rollback()
        return False
