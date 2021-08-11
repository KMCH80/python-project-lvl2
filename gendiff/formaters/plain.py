import collections

TEXT_COMMENTS = {
    'added': 'was added with value: ',
    'changed': 'was updated. From ',
    'deleted': 'was removed'
}


def plain_formater(diff, diff_result, path=''):
    sorted_diff = collections.OrderedDict(sorted(diff.items()))
    for key, value in sorted_diff.items():
        if value[0] == 'is_dict':
            new_path = path + f'{key}.'
            plain_formater(value[1], diff_result, new_path)
            continue
        if len(value) == 2 and value[1] == "not changed":
            continue
        comment = get_comment(value)
        diff_result.append(f"Property '{path}{key}' {comment}")
    result_string = '\n'.join(diff_result)
    return result_string


def get_comment(value):
    if len(value) and value[1] == "added":
        return get_added_comment(TEXT_COMMENTS[value[1]], value[0])
    if len(value) == 2 and value[1] == "deleted":
        return f'{TEXT_COMMENTS[value[1]]}'
    if len(value) == 3 and value[2] == "changed":
        return get_changed_comment(TEXT_COMMENTS[value[2]], value[0], value[1])


def get_added_comment(text, value):
    if isinstance(value, dict):
        return f'{text}[complex value]'
    return f'{text}{format_special_types(value)}'


def get_changed_comment(text, value1, value2):
    comment1 = format_special_types(value1)
    comment2 = format_special_types(value2)
    if isinstance(value1, dict):
        comment1 = '[complex value]'
    if isinstance(value2, dict):
        comment2 = '[complex value]'
    return (f'{text}{comment1} to {comment2}')


def format_special_types(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    if value is int:
        return value
    return f"'{value}'"
