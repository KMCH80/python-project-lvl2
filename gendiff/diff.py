from gendiff import file_reader
from gendiff.format_selector import STYLE_OPT_STYLISH
from gendiff.format_selector import get_selected_format

ADDED_STATUS = 'added'
DELETED_STATUS = 'deleted'
NOT_CHANGED_STATUS = 'not changed'
CHANGED_STATUS = 'changed'
IS_DICT_STATUS = 'is dict'


def generate_diff(file1, file2, format_name=STYLE_OPT_STYLISH):
    data1 = file_reader.get_data_from_file(file1)
    data2 = file_reader.get_data_from_file(file2)
    diff = create_diff(data1, data2)
    return get_selected_format(format_name, diff)


def create_diff(data1: dict, data2: dict):
    diff = {}
    united_keys = data1.keys() | data2.keys()
    for key in united_keys:
        diff[key] = create_element_status(key, data1, data2)
    return diff


def create_element_status(key, data1, data2):
    if key not in data1.keys():
        return ADDED_STATUS, data2[key]
    if key not in data2.keys():
        return DELETED_STATUS, data1[key]
    if data1[key] == data2[key]:
        return NOT_CHANGED_STATUS, data2[key]
    if isinstance(data1[key], dict) and isinstance(data2[key], dict):
        return IS_DICT_STATUS, create_diff(
            data1[key], data2[key])
    return CHANGED_STATUS, (data1[key], data2[key])
