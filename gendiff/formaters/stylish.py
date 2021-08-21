TREE_SPACE = '    '
DICT_SPACE = '  '

ADDED_STATUS = 'added'
DELETED_STATUS = 'deleted'
NOT_CHANGED_STATUS = 'not changed'
CHANGED_STATUS = 'changed'
IS_DICT_STATUS = 'is dict'


def stylish_formater(diff: dict):
    formated_list = get_formated_list(diff)
    result_string = '{\n' + '\n'.join(formated_list) + '\n}'
    return result_string


def get_formated_list(diff, tree_space=''):
    result_list = []
    diff_sorted = dict(sorted(diff.items()))
    for key, value in diff_sorted.items():
        status, diff_value = value
        result_list.extend(get_formated_string(
            key, status, diff_value, tree_space))
    return result_list


def get_formated_string(key, status, diff_value, tree_space):
    diff_list = []
    if status == IS_DICT_STATUS:
        tree_space += TREE_SPACE
        diff_list.append(f'{tree_space}{key}: {{')
        diff_list.extend(get_formated_list(diff_value, tree_space))
        diff_list.append(f'{tree_space}}}')
        return diff_list
    if status == CHANGED_STATUS:
        diff_list.append(add_string_to_diff(
            f'- {key}', format_special_types(diff_value[0]),
            tree_space))
        diff_list.append(add_string_to_diff(
            f'+ {key}', format_special_types(diff_value[1]),
            tree_space))
        return diff_list
    key_format = {
        DELETED_STATUS: f'- {key}',
        ADDED_STATUS: f'+ {key}',
        NOT_CHANGED_STATUS: f'  {key}'
    }
    str_key = key_format[status]
    diff_list.append(add_string_to_diff(
        str_key, diff_value, tree_space))
    return diff_list


def add_string_to_diff(str_key, value, space):
    if isinstance(value, dict):
        return add_dict_in_dict(
            space, str_key, value)
    return (
        f'{space}{DICT_SPACE}{str_key}: {format_special_types(value)}'
    )


def add_dict_in_dict(tree_space, key, add_dict):
    in_dict = []
    in_dict.append(f'{tree_space}  {key}: {{')
    tree_space += TREE_SPACE
    for k, v in add_dict.items():
        str_dic = f'{k}: {v}'
        if isinstance(v, dict):
            in_dict.append(add_dict_in_dict(tree_space, f'  {k}', v))
            continue
        in_dict.append(f'{tree_space}{TREE_SPACE}{str_dic}')
    tree_space = tree_space[:-len(TREE_SPACE)]
    in_dict.append(f'{tree_space}{DICT_SPACE}  }}')
    return ('\n'.join(in_dict))


def format_special_types(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return value
