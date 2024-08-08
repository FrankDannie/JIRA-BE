from fastapi import APIRouter

from app.api.v1.endpoints.authentication.auth_login import (router as auth_login_router)
from app.api.v1.endpoints.authentication.auth_sign_in import (router as auth_sign_in_router)
from app.api.v1.endpoints.authentication.logout import (router as logout_router)
from app.api.v1.endpoints.authentication.user_get import (router as user_get_router)

router = APIRouter()

router.include_router(auth_login_router, prefix="", tags=["auth/"])
router.include_router(auth_sign_in_router, prefix="", tags=["auth/"])
router.include_router(logout_router, prefix="", tags=["auth/"])
router.include_router(user_get_router, prefix="", tags=["auth/"])