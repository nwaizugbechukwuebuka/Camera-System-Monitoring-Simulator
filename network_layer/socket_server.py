import asyncio
import websockets
from backend.utils.logger import get_logger

logger = get_logger('SocketServer', 'logs/system_logs/socket_server.log')

class SocketServer:
    def __init__(self, host='0.0.0.0', port=8765):
        self.host = host
        self.port = port
        self.clients = set()

    async def handler(self, websocket, path):
        self.clients.add(websocket)
        logger.info(f"Client connected: {websocket.remote_address}")
        try:
            async for message in websocket:
                logger.info(f"Received: {message}")
        finally:
            self.clients.remove(websocket)
            logger.info(f"Client disconnected: {websocket.remote_address}")

    def start(self):
        asyncio.get_event_loop().run_until_complete(
            websockets.serve(self.handler, self.host, self.port)
        )
        logger.info(f"Socket server started on {self.host}:{self.port}")
        asyncio.get_event_loop().run_forever()
