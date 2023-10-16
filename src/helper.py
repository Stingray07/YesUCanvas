import json


def format_data(data):
    print(json.dumps(data, indent=4))