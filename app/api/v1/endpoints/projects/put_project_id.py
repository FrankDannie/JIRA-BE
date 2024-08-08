from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.projects.put_project_id import update_existing_project
from app.schemas.projects.put_project_id import ProjectUpdate, ProjectOut

router = APIRouter()

@router.put("/projects/{projectId}/", response_model=ProjectOut, tags=["projects"], summary="Update a project")
async def update_project(projectId: int, project_update: ProjectUpdate, db: Session = Depends(get_db)):
    updated_project = update_existing_project(db, projectId, project_update)
    if updated_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project
