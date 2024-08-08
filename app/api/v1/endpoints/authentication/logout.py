from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.authentication.logout import Message  
from app.services.authentication.logout import logout_user  

router = APIRouter()

@router.post("/auth/logout", response_model=Message, tags=["Authentication"], summary="User logout")
async def logout(db: Session = Depends(get_db)):
    """
    Handle user logout.
    """
    result = logout_user(db)
    if not result:
        raise HTTPException(status_code=400, detail="Logout failed")
    return {"message": "Successful logout"}
