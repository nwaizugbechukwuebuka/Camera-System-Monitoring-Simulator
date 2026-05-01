from backend.models.camera_model import Camera
from backend.utils.config_loader import load_camera_config
from backend.services.failure_simulation_service import get_system_metrics
from backend.state.system_state import _cameras


def _compute_status(total_cameras, offline_cameras, error_rate):
    """
    Computes system status based on camera availability and error rate.
    """

    if total_cameras == 0:
        return "critical"

    if error_rate > 0.08:
        return "unhealthy"

    if offline_cameras == 0:
        return "healthy"

    if offline_cameras < total_cameras / 2:
        return "degraded"

    return "critical"


def initialize_cameras():
    config = load_camera_config()
    cameras_config = config.get("cameras", [])

    if not _cameras:
        for cam in cameras_config:
            try:
                _cameras.append(Camera(**cam))
            except Exception as e:
                print(f"Invalid camera config: {cam} -> {e}")


def get_system_health():
    """
    Aggregates real-time system health using:
    - live camera states (mutated by simulation)
    - dynamic system metrics
    """

    initialize_cameras()

    total_cameras = len(_cameras)
    online_cameras = sum(1 for c in _cameras if getattr(c, "enabled", False))
    offline_cameras = total_cameras - online_cameras

    metrics = get_system_metrics()

    health = {
        "status": _compute_status(
            total_cameras,
            offline_cameras,
            metrics.get("error_rate", 0)
        ),
        "cameras": {
            "total": total_cameras,
            "online": online_cameras,
            "offline": offline_cameras
        },
        "metrics": {
            "avg_latency_ms": metrics.get("avg_latency_ms"),
            "frame_drop_rate": metrics.get("frame_drop_rate"),
            "error_rate": metrics.get("error_rate")
        }
    }

    return health
