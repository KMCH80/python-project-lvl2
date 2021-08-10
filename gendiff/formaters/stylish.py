import collections

TREE_SPACE = '    '
DICT_SPACE = '  '


def stylish_formater(diff: dict, diff_result: list, tree_space=''):
    sorted_diff = collections.OrderedDict(sorted(diff.items()))
    for key, value in sorted_diff.items():
        if value[0] == 'is_dict':
            tree_space += TREE_SPACE
            diff_result.append(f'{tree_space}{key}: {{')
            stylish_formater(value[1], diff_result, tree_space)
            diff_result.append(f'{tree_space}}}')
            tree_space = tree_space[:-len(TREE_SPACE)]
            continue
        if 'changed' in value and value[0] != value[1] != "changed":
            add_string_to_diff(
                f'- {key}', format_special_types(diff[key][0]),
                tree_space, diff_result
            )
            add_string_to_diff(
                f'+ {key}', format_special_types(diff[key][1]),
                tree_space, diff_result
            )
            continue
        key_format = {
            "deleted": f'- {key}',
            "added": f'+ {key}',
            "not changed": f'  {key}'
        }
        str_key = key_format[value[1]]
        add_string_to_diff(
            str_key, diff[key][0], tree_space, diff_result
        )
    result_string = '{\n' + '\n'.join(diff_result) + '\n}'
    return result_string


def format_special_types(value):
    if value is True:
        return 'true'
    if value is False:
        return 'false'
    if value is None:
        return 'null'
    return value


def add_dict_in_dict(tree_space, key, add_dict, in_dict):
    in_dict.append(f'{tree_space}  {key}: {{')
    tree_space += TREE_SPACE
    for k, v in add_dict.items():
        str_dic = f'{k}: {v}'
        if isinstance(v, dict):
            add_dict_in_dict(tree_space, f'  {k}', v, in_dict)
            continue
        in_dict.append(f'{tree_space}{TREE_SPACE}{str_dic}')
    tree_space = tree_space[:-len(TREE_SPACE)]
    in_dict.append(f'{tree_space}{DICT_SPACE}  }}')


def add_string_to_diff(str_key, value, space, diff_result):
    if isinstance(value, dict):
        add_dict_in_dict(
            space, str_key, value, diff_result)
    else:
        diff_result.append(
            f'{space}{DICT_SPACE}{str_key}: {format_special_types(value)}'
        )
