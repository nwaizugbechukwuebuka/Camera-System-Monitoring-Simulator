from fastapi import APIRouter
from backend.services.monitoring_service import get_system_health

router = APIRouter()


@router.get("/", summary="Get system health")
def system_health():
    """
    Returns aggregated system health metrics including:
    - camera status
    - latency
    - error rates
    - uptime
    """
    return get_system_health()
