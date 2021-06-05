import collections

TEXT_COMMENTS = {
    'added': 'was added with value: ',
    'changed': 'was updated. From ',
    'deleted': 'was removed'
}
SPECIAL_TYPES = ['true', 'false', 'null']


def plain_formater(data1, data2, diff, diff_result, path=''):
    sorted_diff = collections.OrderedDict(sorted(diff.items()))
    sorted_data1 = collections.OrderedDict(sorted(data1.items()))
    sorted_data2 = collections.OrderedDict(sorted(data2.items()))
    for key, value in sorted_diff.items():
        path += f'{key}'
        if isinstance(value, dict):
            path += '.'
            plain_formater(sorted_data1[key], sorted_data2[key], value,
                           diff_result, path)
            path = path[:-1]
        if value == "added":
            comment = get_added_comment(TEXT_COMMENTS[value], sorted_data2[key])

        elif value == "changed":
            comment = get_changed_comment(
                TEXT_COMMENTS[value], sorted_data1[key], sorted_data2[key])
        elif value == "deleted":
            comment = f'{TEXT_COMMENTS[value]}'
        else:
            path = path[:-len(key)]
            continue
        diff_result.append(f"Property '{path}' {comment}")
        path = path[:-len(key)]
    result_string = '\n'.join(diff_result)
    return result_string


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
    if value not in SPECIAL_TYPES:
        return f"'{value}'"
    return value
