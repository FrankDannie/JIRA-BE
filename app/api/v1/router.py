from fastapi import APIRouter

from app.api.v1.endpoints.authentication.auth_login import (
    router as characteristics_actl_status_check_get_router,
)

router = APIRouter()

router.include_router(characteristics_actl_status_check_get_router, prefix="", tags=["auth/"])
