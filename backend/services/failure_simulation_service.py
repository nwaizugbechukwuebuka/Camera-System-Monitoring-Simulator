import random
import time
from threading import Lock

from backend.state.system_state import _cameras

# Shared system metrics
_system_metrics = {
    "avg_latency_ms": 10,
    "frame_drop_rate": 0.0,
    "error_rate": 0.0
}

lock = Lock()


def get_system_metrics():
    with lock:
        return _system_metrics.copy()


def simulate_failures():
    while True:
        with lock:
            # 1. Random camera failure
            if _cameras:
                cam = random.choice(_cameras)
                if random.random() < 0.3:
                    cam.enabled = False
                else:
                    cam.enabled = True

            # 2. Simulate latency spike
            _system_metrics["avg_latency_ms"] = random.randint(5, 100)

            # 3. Simulate frame drop
            _system_metrics["frame_drop_rate"] = round(random.uniform(0, 0.2), 3)

            # 4. Simulate error rate
            _system_metrics["error_rate"] = round(random.uniform(0, 0.1), 3)

        time.sleep(5)  # update every 5 seconds
