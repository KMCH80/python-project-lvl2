import os
import yaml
import json


def get_data_from_file(file):
    extention = os.path.splitext(file)[1]
    extention = extention.lower()
    with open(file) as f:
        return parse_data(extention, f)


def parse_data(extention, f):
    if (extention == ".yml") or (extention == ".yaml"):
        return yaml.safe_load(f)
    if (extention == ".json"):
        return json.load(f)
    raise Exception("Wrong file extension!")
