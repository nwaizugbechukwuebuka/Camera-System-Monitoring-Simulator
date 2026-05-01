import random
import time

def inject_latency(base_latency_ms, jitter_ms):
    latency = random.gauss(base_latency_ms, jitter_ms)
    time.sleep(max(0, latency / 1000.0))
    return latency
