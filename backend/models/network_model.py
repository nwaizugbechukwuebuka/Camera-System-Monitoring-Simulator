from pydantic import BaseModel

class NetworkConfig(BaseModel):
    latency_ms: int
    packet_loss: float
    jitter_ms: int
    max_bandwidth_mbps: int
