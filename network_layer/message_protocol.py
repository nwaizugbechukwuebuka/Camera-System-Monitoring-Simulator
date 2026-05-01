import json

def encode_message(data):
    return json.dumps(data)

def decode_message(message):
    return json.loads(message)
