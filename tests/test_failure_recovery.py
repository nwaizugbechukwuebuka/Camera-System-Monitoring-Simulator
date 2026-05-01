from backend.services.failure_service import handle_failure
from backend.services.recovery_service import recover_camera

def test_failure_and_recovery():
    fail = handle_failure('cam01')
    assert fail['action'] == 'recovery_initiated'
    rec = recover_camera('cam01')
    assert rec['status'] == 'recovered'
