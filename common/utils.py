import json


def convert_response_to_json(data):
    return json.loads(json.dumps(data, default=str, indent=2))


def filter_function():
    pass
