from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.authentication.auth_sign_in import UserCreate, UserResponse
from app.db.session import get_db
from app.crud.authentication.auth_sign_in import auth_sign_in
from app.models.user import User

router = APIRouter()

@router.post("/auth/signup/", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["Authentication"])
def sign_in(user_in: UserCreate, db: Session = Depends(get_db)):
    """
    Sign In new users and check for already existing user
    """
    existing_user = db.query(User).filter(User.email == user_in.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    user = auth_sign_in(db, user_in)
    return user
