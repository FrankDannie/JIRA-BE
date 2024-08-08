from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.services.projects.projects_get import fetch_all_projects
from app.schemas.projects.projects_get import ProjectOut

router = APIRouter()

@router.get("/projects/", response_model=List[ProjectOut], tags=["projects"], summary="Get all projects")
async def get_all_projects(db: Session = Depends(get_db)):
    projects = fetch_all_projects(db)
    if projects is None:
        raise HTTPException(status_code=404, detail="No projects found")
    return projects
