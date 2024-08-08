from fastapi import APIRouter

from app.api.v1.endpoints.authentication.auth_login import (router as auth_login_router)
from app.api.v1.endpoints.authentication.auth_sign_in import (router as auth_sign_in_router)
from app.api.v1.endpoints.authentication.logout import (router as logout_router)
from app.api.v1.endpoints.authentication.user_get import (router as user_get_router)
from app.api.v1.endpoints.projects.projects_get import (router as projects_get_router)
from app.api.v1.endpoints.projects.projects_post import (router as projects_post_router)
from app.api.v1.endpoints.projects.get_project_id import (router as get_project_id_router)
from app.api.v1.endpoints.projects.put_project_id import (router as put_project_id_router)
from app.api.v1.endpoints.projects.delete_project_id import (router as delete_project_id_router)

router = APIRouter()

# Authentication
router.include_router(auth_login_router, prefix="", tags=["auth/"])
router.include_router(auth_sign_in_router, prefix="", tags=["auth/"])
router.include_router(logout_router, prefix="", tags=["auth/"])
router.include_router(user_get_router, prefix="", tags=["auth/"])

# Projects
router.include_router(projects_get_router, prefix="", tags=["projects/"])
router.include_router(projects_post_router, prefix="", tags=["projects/"])
router.include_router(get_project_id_router, prefix="", tags=["projects/"])
router.include_router(put_project_id_router, prefix="", tags=["projects/"])
router.include_router(delete_project_id_router, prefix="", tags=["projects/"])