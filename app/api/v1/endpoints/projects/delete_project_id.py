from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.projects.delete_project_id import remove_project

router = APIRouter()

@router.delete("/projects/{projectId}/", status_code=204, tags=["projects"], summary="Delete a project")
async def delete_project(projectId: int, db: Session = Depends(get_db)):
    success = remove_project(db, projectId)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
