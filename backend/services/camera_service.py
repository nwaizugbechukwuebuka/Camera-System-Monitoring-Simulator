from backend.models.camera_model import Camera
from backend.utils.config_loader import load_camera_config

_cameras = None

def get_all_cameras():
    global _cameras
    if _cameras is None:
        config = load_camera_config()
        _cameras = [Camera(**cam) for cam in config['cameras']]
    return [cam.model_dump() for cam in _cameras]

def get_camera_status(camera_id: str):
    global _cameras
    if _cameras is None:
        get_all_cameras()
    for cam in _cameras:
        if cam.id == camera_id:
            return cam.status()
    return {"error": "Camera not found"}
