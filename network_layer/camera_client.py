import asyncio
import websockets
import json
from backend.utils.logger import get_logger

logger = get_logger('CameraClient', 'logs/camera_logs/camera_client.log')

class CameraClient:
    def __init__(self, uri):
        self.uri = uri

    async def send_frame(self, frame):
        async with websockets.connect(self.uri) as websocket:
            await websocket.send(json.dumps(frame))
            logger.info(f"Sent frame: {frame}")
