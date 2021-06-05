import collections
import json

TREE_SPACE = '  '
SPECIAL_TYPES = ['true', 'false', 'null']


def json_formater(data1: dict, data2: dict, diff: dict,
                  diff_json_result: dict):
    diff_sorted = collections.OrderedDict(sorted(diff.items()))
    temp_sorted1 = collections.OrderedDict(sorted(data1.items()))
    temp_sorted2 = collections.OrderedDict(sorted(data2.items()))
    for key, value in diff_sorted.items():
        if isinstance(value, dict):
            diff_json_result[key] = {}
            json_formater(temp_sorted1[key], temp_sorted2[key], value,
                          diff_json_result[key])
        elif value == "":
            diff_json_result[key] = temp_sorted1[key]
        elif value == "changed":
            formated_value1 = get_special_formated_value(temp_sorted1[key])
            formated_value2 = get_special_formated_value(temp_sorted2[key])
            diff_json_result[key] = [formated_value1, formated_value2, value]
        elif value == "deleted":
            formated_value1 = get_special_formated_value(temp_sorted1[key])
            diff_json_result[key] = [formated_value1, value]
        else:
            formated_value2 = get_special_formated_value(temp_sorted2[key])
            diff_json_result[key] = [formated_value2, value]
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
