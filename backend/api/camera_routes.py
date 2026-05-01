from fastapi import APIRouter
from backend.services.camera_service import get_all_cameras, get_camera_status

router = APIRouter()

@router.get("/", summary="List all cameras")
def list_cameras():
    return get_all_cameras()

@router.get("/{camera_id}/status", summary="Get camera status")
def camera_status(camera_id: str):
    return get_camera_status(camera_id)
