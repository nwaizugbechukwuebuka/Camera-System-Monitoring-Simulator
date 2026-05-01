from backend.utils.logger import get_logger

logger = get_logger('AlertEngine', 'logs/failure_logs/alert_engine.log')

def alert_if_anomaly(health, metrics):
    alerts = []
    if any(status == 'offline' for status in health.values()):
        alerts.append('One or more cameras offline!')
    if metrics['latency_ms'] > 100:
        alerts.append('High network latency!')
    if metrics['packet_loss'] > 0.05:
        alerts.append('High packet loss!')
    for alert in alerts:
        logger.error(alert)
    return alerts
