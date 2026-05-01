from monitoring.dashboard_feed import get_dashboard_data

def test_dashboard_data():
    data = get_dashboard_data()
    assert 'health' in data
    assert 'metrics' in data
    assert 'alerts' in data
