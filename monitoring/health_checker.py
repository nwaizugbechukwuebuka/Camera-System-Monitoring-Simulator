import time
from backend.utils.logger import get_logger
from backend.utils.config_loader import load_camera_config

logger = get_logger('HealthChecker', 'logs/system_logs/health_checker.log')

def check_camera_health():
    config = load_camera_config()
    health = {}
    for cam in config['cameras']:
        # Simulate health check
        health[cam['id']] = 'online' if cam['enabled'] else 'offline'
    logger.info(f"Health check: {health}")
    return health
