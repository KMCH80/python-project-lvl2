from gendiff import file_reader
from gendiff.formaters.stylish import stylish_formater
from gendiff.formaters.plain import plain_formater
from gendiff.formaters.json import json_formater

STYLE_OPT_JSON = 'json'
STYLE_OPT_PLAIN = 'plain'
STYLE_OPT_STYLISH = 'stylish'


def generate_diff(file1, file2, format_name=STYLE_OPT_STYLISH):
    data1 = file_reader.get_data_from_file(file1)
    data2 = file_reader.get_data_from_file(file2)
    diff = get_elements_changes(data1, data2, diff={})
    if format_name == STYLE_OPT_PLAIN:
        return plain_formater(diff, diff_result=[])
    if format_name == STYLE_OPT_JSON:
        return json_formater(diff, diff_json_result={})
    if format_name == STYLE_OPT_STYLISH:
        return stylish_formater(diff, diff_result=[])
    raise Exception("Wrong format_name!")


def get_united_data(data1, data2):
    return {**data2, **data1}


def get_elements_changes(data1: dict, data2: dict, diff: dict):
    united_data = get_united_data(data1, data2)
    for key, value in united_data.items():
        if key not in data1:
            diff[key] = (value, 'added')
            continue
        if key not in data2:
            diff[key] = (value, 'deleted')
            continue
        if data1[key] == data2[key]:
            diff[key] = (value, 'not changed')
            continue
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.update({key: ('is_dict', {})})
            get_elements_changes(data1[key], data2[key], diff[key][1])
            continue
        diff[key] = (value, data2[key], 'changed')
    return diff
