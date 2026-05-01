from monitoring.health_checker import check_camera_health
from monitoring.metrics_collector import collect_metrics
from monitoring.alert_engine import alert_if_anomaly

def get_dashboard_data():
    health = check_camera_health()
    metrics = collect_metrics()
    alerts = alert_if_anomaly(health, metrics)
    return {
        'health': health,
        'metrics': metrics,
        'alerts': alerts
    }
