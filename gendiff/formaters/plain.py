import collections

TEXT_COMMENTS = {
    'added': 'was added with value: ',
    'changed': 'was updated. From ',
    'deleted': 'was removed'
}
SPECIAL_TYPES = ['true', 'false', 'null']


def plain_formater(diff, diff_result, path=''):
    sorted_diff = collections.OrderedDict(sorted(diff.items()))
    for key, value in sorted_diff.items():
        path += f'{key}'
        if isinstance(value, dict):
            path += '.'
            plain_formater(value, diff_result, path)
            path = path[:-1]
        if "added" in value:
            comment = get_added_comment(TEXT_COMMENTS["added"], value[0])
        elif "changed" in value:
            comment = get_changed_comment(
                TEXT_COMMENTS["changed"], value[0], value[1])
        elif "deleted" in value:
            comment = f'{TEXT_COMMENTS["deleted"]}'
        else:
            path = path[:-len(key)]
            continue
        diff_result.append(f"Property '{path}' {comment}")
        path = path[:-len(key)]
    result_string = '\n'.join(diff_result)
    return result_string


def format_value_special_type(value):
    dic_of_types = {
        'True': "true",
        'False': "false",
        'None': "null",
    }
    if str(value) in dic_of_types:
        return dic_of_types[str(value)]
    else:
        return value


def get_added_comment(text, value):
    if isinstance(value, dict):
        comment = '[complex value]'
    else:
        comment = format_special_types(value)
    return f'{text}{comment}'


def get_changed_comment(text, value1, value2):
    comment1 = format_special_types(value1)
    comment2 = format_special_types(value2)
    if isinstance(value1, dict):
        comment1 = '[complex value]'
    if isinstance(value2, dict):
        comment2 = '[complex value]'
    return (f'{text}{comment1} to {comment2}')


def format_special_types(value):
    value = format_value_special_type(value)
    if value not in SPECIAL_TYPES:
        if type(value) == int or type(value) == float:
            return f"{value}"
        else:
            return f"'{value}'"
    return value
