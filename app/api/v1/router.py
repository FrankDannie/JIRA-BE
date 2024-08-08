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
from app.api.v1.endpoints.tasks.get_tasks import (router as get_tasks_router)
from app.api.v1.endpoints.tasks.post_tasks import (router as post_tasks_router)
from app.api.v1.endpoints.tasks.get_task_id import (router as get_task_id_router)
from app.api.v1.endpoints.tasks.put_task_id import (router as put_task_id_router)
from app.api.v1.endpoints.tasks.delete_task_id import (router as delete_task_id_router)
from app.api.v1.endpoints.comments.get_comment import (router as get_comment_router)
from app.api.v1.endpoints.comments.post_comment import (router as post_comment_router)
from app.api.v1.endpoints.comments.put_comments import (router as put_comment_router)
from app.api.v1.endpoints.attachments.post_attachments import (router as post_attachments_router)
from app.api.v1.endpoints.attachments.get_attachments import (router as get_attachments_router)
from app.api.v1.endpoints.attachments.delete_attachments import (router as delete_attachments_router)

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

# Tasks
router.include_router(get_tasks_router, prefix="", tags=["tasks/"])
router.include_router(post_tasks_router, prefix="", tags=["tasks/"])
router.include_router(get_task_id_router, prefix="", tags=["tasks/"])
router.include_router(put_task_id_router, prefix="", tags=["tasks/"])
router.include_router(delete_task_id_router, prefix="", tags=["tasks/"])

# Comment
router.include_router(get_comment_router, prefix="", tags=["comments/"])
router.include_router(post_comment_router, prefix="", tags=["comments/"])
router.include_router(put_comment_router, prefix="", tags=["comments/"])

# Attachment
router.include_router(post_attachments_router, prefix="", tags=["comments/"])
router.include_router(get_attachments_router, prefix="", tags=["comments/"])
router.include_router(delete_attachments_router, prefix="", tags=["comments/"])