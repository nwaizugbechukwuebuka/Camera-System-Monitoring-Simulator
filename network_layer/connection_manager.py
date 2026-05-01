class ConnectionManager:
    def __init__(self):
        self.active_connections = {}

    def add_connection(self, camera_id, connection):
        self.active_connections[camera_id] = connection

    def remove_connection(self, camera_id):
        if camera_id in self.active_connections:
            del self.active_connections[camera_id]

    def get_connection(self, camera_id):
        return self.active_connections.get(camera_id)
