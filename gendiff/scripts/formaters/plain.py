import collections

TEXT_COMMENTS = {
    'added': 'was added with value: ',
    'changed': 'was updated. From ',
    'deleted': 'was removed'
}
SPECIAL_TYPES = ['true', 'false', 'null']


def plain_formater(template1, template2, diff, diff_res, path=''):
    diff_sorted = collections.OrderedDict(sorted(diff.items()))
    temp_sorted1 = collections.OrderedDict(sorted(template1.items()))
    temp_sorted2 = collections.OrderedDict(sorted(template2.items()))
    for key, value in diff_sorted.items():
        path += f'{key}'
        if isinstance(value, dict):
            path += '.'
            plain_formater(temp_sorted1[key], temp_sorted2[key], value,
                           diff_res, path)
            path = path[:-1]
        if value == "added":
            comment = get_added_comment(TEXT_COMMENTS[value], temp_sorted2[key])

        elif value == "changed":
            comment = get_changed_comment(
                TEXT_COMMENTS[value], temp_sorted1[key], temp_sorted2[key])
        elif value == "deleted":
            comment = f'{TEXT_COMMENTS[value]}'
        else:
            path = path[:-len(key)]
            continue
        diff_res.append(f"Property '{path}' {comment}")
        path = path[:-len(key)]
    str = '\n'.join(diff_res)
    return str


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
