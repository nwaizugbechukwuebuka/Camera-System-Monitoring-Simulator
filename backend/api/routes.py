from fastapi import APIRouter
from backend.api.camera_routes import router as camera_router
from backend.api.health_routes import router as health_router

router = APIRouter()

# Camera endpoints
router.include_router(
    camera_router,
    prefix="/cameras",
    tags=["Cameras"]
)

# Health endpoints
router.include_router(
    health_router,
    prefix="/health",
    tags=["System Health"]
)
