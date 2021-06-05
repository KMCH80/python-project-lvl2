import collections

TREE_SPACE = '    '
DICT_SPACE = '  '


def stylish_formater(data1: dict, data2: dict, diff: dict,
                     diff_result: list, tree_space=''):
    sorted_diff = collections.OrderedDict(sorted(diff.items()))
    sorted_data1 = collections.OrderedDict(sorted(data1.items()))
    sorted_data2 = collections.OrderedDict(sorted(data2.items()))
    for key, value in sorted_diff.items():
        if isinstance(value, dict):
            tree_space += TREE_SPACE
            diff_result.append(f'{tree_space}{key}: {{')
            stylish_formater(sorted_data1[key], sorted_data2[key], value,
                             diff_result, tree_space)
            diff_result.append(f'{tree_space}}}')
            tree_space = tree_space[:-len(TREE_SPACE)]
        elif value == "":
            add_string_to_diff(
                f'  {key}', sorted_data1[key], tree_space, diff_result
            )
        elif value == "changed":
            add_string_to_diff(
                f'- {key}', sorted_data1[key], tree_space, diff_result
            )
            add_string_to_diff(
                f'+ {key}', sorted_data2[key], tree_space, diff_result
            )
        elif value == "deleted":
            add_string_to_diff(
                f'- {key}', sorted_data1[key], tree_space, diff_result
            )
        else:
            add_string_to_diff(
                f'+ {key}', sorted_data2[key], tree_space, diff_result
            )
    result_string = '{\n' + '\n'.join(diff_result) + '\n}'
    return result_string


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
