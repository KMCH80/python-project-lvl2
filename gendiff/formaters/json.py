import collections
import json

TREE_SPACE = '  '
SPECIAL_TYPES = ['true', 'false', 'null']


def json_formater(diff: dict, diff_json_result: dict):
    diff_sorted = collections.OrderedDict(sorted(diff.items()))
    for key, value in diff_sorted.items():
        if isinstance(value, dict):
            diff_json_result[key] = {}
            json_formater(value, diff_json_result[key])
        elif "not changed" in value:
            diff_json_result[key] = value[0]
        elif "changed" in value:
            formated_value1 = get_special_formated_value(value[0])
            formated_value2 = get_special_formated_value(value[1])
            diff_json_result[key] = [formated_value1, formated_value2, value[2]]
        elif "deleted" in value:
            formated_value1 = get_special_formated_value(value[0])
            diff_json_result[key] = [formated_value1, value[1]]
        else:
            formated_value2 = get_special_formated_value(value[0])
            diff_json_result[key] = [formated_value2, value[1]]
    str = json.dumps(diff_json_result, indent=2)
    return str


def get_special_formated_value(value):
    dic_of_types = {
        "true": True,
        "false": False,
        "null": None
    }
    if value not in SPECIAL_TYPES:
        return value
    return dic_of_types[value]
