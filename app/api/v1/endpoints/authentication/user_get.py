from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.authentication.user_get import UserOut
from app.services.authentication.user_get import get_current_user  

router = APIRouter()

@router.get("/auth/user", response_model=UserOut, tags=["Authentication"], summary="Get authenticated user details")
async def user_get(current_user: UserOut = Depends(get_current_user)):
    """
    Get the details of the authenticated user.
    """
    return current_user
