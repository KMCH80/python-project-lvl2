import collections
import json


def json_formater(diff: dict, diff_json_result: dict):
    diff_sorted = collections.OrderedDict(sorted(diff.items()))
    for key, value in diff_sorted.items():
        if value[0] == 'is_dict':
            diff_json_result[key] = {}
            json_formater(value[1], diff_json_result[key])
            continue
        if "not changed" in value and value[0] != "not changed":
            diff_json_result[key] = value[0]
            continue
        if "changed" in value and value[0] != value[1] != "changed":
            diff_json_result[key] = [value[0], value[1], value[2]]
            continue
        if "deleted" in value and value[0] != "deleted" or (
                "added" in value and value[0] != "added"):
            diff_json_result[key] = [value[0], value[1]]
    str = json.dumps(diff_json_result, indent=2)
    return str
