import time
import random
import threading
from backend.utils.logger import get_logger
from backend.utils.config_loader import load_camera_config

logger = get_logger('CameraSimulator', 'logs/camera_logs/camera_simulator.log')

class CameraSimulator(threading.Thread):
    def __init__(self, camera_id, location, ip, enabled=True):
        super().__init__()
        self.camera_id = camera_id
        self.location = location
        self.ip = ip
        self.enabled = enabled
        self.running = True
        self.status = 'online'

    def run(self):
        logger.info(f"Camera {self.camera_id} at {self.location} started.")
        while self.running and self.enabled:
            # Simulate frame capture
            frame = self.capture_frame()
            # Simulate sending frame to server (placeholder)
            logger.info(f"Camera {self.camera_id} sent frame: {frame}")
            time.sleep(random.uniform(0.05, 0.2))

    def capture_frame(self):
        # Simulate frame data
        return {
            'camera_id': self.camera_id,
            'timestamp': time.time(),
            'data': random.randint(0, 255)
        }

    def stop(self):
        self.running = False
        logger.info(f"Camera {self.camera_id} stopped.")


def start_all_cameras():
    config = load_camera_config()
    cameras = []
    for cam in config['cameras']:
        if cam['enabled']:
            camera = CameraSimulator(cam['id'], cam['location'], cam['ip'], cam['enabled'])
            camera.start()
            cameras.append(camera)
    return cameras
