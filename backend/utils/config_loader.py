import yaml

def load_camera_config():
    with open('config/camera_config.yaml', 'r') as f:
        data = yaml.safe_load(f)
        return data or {"cameras": []}

def load_network_config():
    with open('config/network_config.yaml', 'r') as f:
        return yaml.safe_load(f)

def load_system_config():
    with open('config/system_config.yaml', 'r') as f:
        return yaml.safe_load(f)
