from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.authentication.user_get import get_current_user 
from app.schemas.authentication.user_get import UserOut
from app.services.projects.projects_post import create_new_project
from app.schemas.projects.projects_post import ProjectCreate, ProjectOut

router = APIRouter()

@router.post("/projects/", response_model=ProjectOut, status_code=status.HTTP_201_CREATED, tags=["projects"], summary="Create a new project")
async def create_project(project: ProjectCreate, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    return create_new_project(db, project, user_id=current_user.username)
