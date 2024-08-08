from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.projects.get_project_id import get_project_by_id
from app.schemas.projects.get_project_id import ProjectOut
from typing import List

router = APIRouter()

@router.get("/projects/{projectId}/", response_model=ProjectOut, tags=["projects"], summary="Get project details")
async def get_project_id(projectId: int, db: Session = Depends(get_db)):
    project = get_project_by_id(db, projectId)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project
