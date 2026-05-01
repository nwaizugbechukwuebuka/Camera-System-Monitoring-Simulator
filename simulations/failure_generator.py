import random
import time
from backend.utils.logger import get_logger

logger = get_logger('FailureGenerator', 'logs/failure_logs/failure_generator.log')

def inject_failure(camera):
    # Randomly set camera offline
    if random.random() < 0.1:
        camera.status = 'offline'
        logger.error(f"Camera {camera.camera_id} went offline.")
        time.sleep(random.uniform(1, 5))
        camera.status = 'online'
        logger.info(f"Camera {camera.camera_id} recovered.")
