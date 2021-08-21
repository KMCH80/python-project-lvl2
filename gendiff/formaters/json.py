import json

ADDED_STATUS = 'added'
DELETED_STATUS = 'deleted'
NOT_CHANGED_STATUS = 'not changed'
CHANGED_STATUS = 'changed'
IS_DICT_STATUS = 'is dict'


def json_formater(diff: dict):
    formated_dict = get_formated_dict(diff)
    str = json.dumps(formated_dict, indent=2)
    return str


def get_formated_dict(diff: dict):
    result_dict = {}
    diff_sorted = dict(sorted(diff.items()))
    for key, value in diff_sorted.items():
        status, diff_value = value
        if status == IS_DICT_STATUS:
            result_dict[key] = get_formated_dict(diff_value)
            continue
        if status == DELETED_STATUS or status == ADDED_STATUS:
            result_dict[key] = [diff_value, status]
            continue
        if status == NOT_CHANGED_STATUS:
            result_dict[key] = diff_value
            continue
        if status == CHANGED_STATUS:
            result_dict[key] = [diff_value[0], diff_value[1], status]
    return result_dict
