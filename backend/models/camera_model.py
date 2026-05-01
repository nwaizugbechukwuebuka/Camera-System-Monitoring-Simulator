from pydantic import BaseModel

class Camera(BaseModel):
    id: str
    enabled: bool = True
    location: str = "unknown"

    def status(self):
        return "online" if self.enabled else "offline"
