from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    timestamp: datetime
    event_type: str
    details: dict
