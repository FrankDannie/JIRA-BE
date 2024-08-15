from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.schemas.authentication.auth_login import Token
from app.services.authentication.auth_login import authenticate_user, create_access_token
from app.db.session import get_db

router = APIRouter()

@router.post("/auth/login/", response_model=Token, tags=["Authentication"])
def auth_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.username})
    print(access_token)
    return {"token": access_token, "token_type": "bearer"}
