from fastapi import APIRouter

from app.api.v1.endpoints.authentication.auth_login import (router as auth_login_router)
from app.api.v1.endpoints.authentication.auth_sign_in import (router as auth_sign_in_router)

router = APIRouter()

router.include_router(auth_login_router, prefix="", tags=["auth/"])
router.include_router(auth_sign_in_router, prefix="", tags=["auth/"])