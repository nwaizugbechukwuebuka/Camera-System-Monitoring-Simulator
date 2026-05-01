import pytest
from backend.services.camera_service import get_all_cameras

def test_camera_list():
    cameras = get_all_cameras()
    assert isinstance(cameras, list)
    assert all('id' in cam for cam in cameras)
