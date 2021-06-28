import collections

TREE_SPACE = '    '
DICT_SPACE = '  '


def stylish_formater(diff: dict, diff_result: list, tree_space=''):
    sorted_diff = collections.OrderedDict(sorted(diff.items()))
    for key, value in sorted_diff.items():
        if isinstance(value, dict):
            tree_space += TREE_SPACE
            diff_result.append(f'{tree_space}{key}: {{')
            stylish_formater(value, diff_result, tree_space)
            diff_result.append(f'{tree_space}}}')
            tree_space = tree_space[:-len(TREE_SPACE)]
        if 'changed' in value:
            add_string_to_diff(
                f'- {key}', format_value_special_type(diff[key][0]),
                tree_space, diff_result
            )
            add_string_to_diff(
                f'+ {key}', format_value_special_type(diff[key][1]),
                tree_space, diff_result
            )
        if 'deleted' in value:
            add_string_to_diff(
                f'- {key}', format_value_special_type(diff[key][0]),
                tree_space, diff_result
            )
        if 'added' in value:
            add_string_to_diff(
                f'+ {key}', format_value_special_type(diff[key][0]),
                tree_space, diff_result
            )
        if 'not changed' in value:
            add_string_to_diff(
                f'  {key}', format_value_special_type(diff[key][0]),
                tree_space, diff_result
            )
    result_string = '{\n' + '\n'.join(diff_result) + '\n}'
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


def add_dict_in_dict(tree_space, key, add_dict, in_dict):
    in_dict.append(f'{tree_space}  {key}: {{')
    tree_space += TREE_SPACE
    for k, v in add_dict.items():
        str_dic = f'{k}: {v}'
        if isinstance(v, dict):
            add_dict_in_dict(tree_space, f'  {k}', v, in_dict)
        else:
            in_dict.append(f'{tree_space}{TREE_SPACE}{str_dic}')
    tree_space = tree_space[:-len(TREE_SPACE)]
    in_dict.append(f'{tree_space}{DICT_SPACE}  }}')


def add_string_to_diff(key, value, space, diff_result):
    if isinstance(value, dict):
        add_dict_in_dict(
            space, f'{key}', value, diff_result)
    else:
        diff_result.append(
            f'{space}{DICT_SPACE}{key}: {value}'
        )
