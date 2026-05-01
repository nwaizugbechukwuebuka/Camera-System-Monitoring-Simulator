import random
import time
from backend.utils.logger import get_logger
from backend.utils.config_loader import load_network_config

logger = get_logger('NetworkSimulator', 'logs/system_logs/network_simulator.log')

class NetworkSimulator:
    def __init__(self):
        self.config = load_network_config()['network']

    def transmit(self, data):
        # Simulate latency
        latency = random.gauss(self.config['latency_ms'], self.config['jitter_ms']) / 1000.0
        time.sleep(max(0, latency))
        # Simulate packet loss
        if random.random() < self.config['packet_loss']:
            logger.warning('Packet lost during transmission.')
            return None
        # Simulate bandwidth (not enforced in this stub)
        logger.info(f"Data transmitted with latency {latency*1000:.2f} ms.")
        return data
