ADDED_STATUS = 'added'
DELETED_STATUS = 'deleted'
NOT_CHANGED_STATUS = 'not changed'
CHANGED_STATUS = 'changed'
IS_DICT_STATUS = 'is dict'
COMPLEX_VALUE = '[complex value]'


def plain_formater(diff):
    formated_list = get_formated_list(diff)
    result_string = '\n'.join(formated_list)
    return result_string


def get_formated_list(diff, path=''):
    result_list = []
    diff_sorted = dict(sorted(diff.items()))
    for key, value in diff_sorted.items():
        status, diff_value = value
        if status == NOT_CHANGED_STATUS:
            continue
        result_list.extend(get_formated_string(
            key, status, diff_value, path))
    return result_list


def get_formated_string(key, status, diff_value, path):
    if status == IS_DICT_STATUS:
        new_path = path + f'{key}.'
        return get_formated_list(diff_value, new_path)
    if status == ADDED_STATUS:
        str = f"Property '{path}{key}' was added with value: " \
            f"{format_special_types(check_complex_value(diff_value))}"
        return [str]
    if status == DELETED_STATUS:
        return [f"Property '{path}{key}' was removed"]
    if status == CHANGED_STATUS:
        str = f"Property '{path}{key}' was updated. " \
            f"From {format_special_types(check_complex_value(diff_value[0]))}" \
            f" to {format_special_types(check_complex_value(diff_value[1]))}"
        return [str]


def check_complex_value(value):
    if isinstance(value, dict):
        return COMPLEX_VALUE
    return value


def format_special_types(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    if value == COMPLEX_VALUE:
        return value
    if isinstance(value, str):
        return f"'{value}'"
    return value
