import os
import yaml
import json


def get_data_from_file(file):
    extention = os.path.splitext(file)[1]
    with open(file) as f:
        if (extention.lower() == ".yml") or (extention.lower() == ".yaml"):
            return yaml.safe_load(f)
        elif (extention.lower() == ".json"):
            return json.load(f)
        else:
            return 0
