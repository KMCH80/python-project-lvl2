import collections

TREE_SPACE = '    '
DICT_SPACE = '  '


def stylish_formater(template1: dict, template2: dict, diff: dict,
                     diff_res: list, tree_space=''):
    diff_sorted = collections.OrderedDict(sorted(diff.items()))
    temp_sorted1 = collections.OrderedDict(sorted(template1.items()))
    temp_sorted2 = collections.OrderedDict(sorted(template2.items()))
    for key, value in diff_sorted.items():
        if isinstance(value, dict):
            tree_space += TREE_SPACE
            diff_res.append(f'{tree_space}{key}: {{')
            stylish_formater(temp_sorted1[key], temp_sorted2[key], value,
                             diff_res, tree_space)
            diff_res.append(f'{tree_space}}}')
            tree_space = tree_space[:-len(TREE_SPACE)]
        elif value == "":
            add_string_to_diff(
                f'  {key}', temp_sorted1[key], tree_space, diff_res
            )
        elif value == "changed":
            add_string_to_diff(
                f'- {key}', temp_sorted1[key], tree_space, diff_res
            )
            add_string_to_diff(
                f'+ {key}', temp_sorted2[key], tree_space, diff_res
            )
        elif value == "deleted":
            add_string_to_diff(
                f'- {key}', temp_sorted1[key], tree_space, diff_res
            )
        else:
            add_string_to_diff(
                f'+ {key}', temp_sorted2[key], tree_space, diff_res
            )
    str = '{\n' + '\n'.join(diff_res) + '\n}'
    return str


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


def add_string_to_diff(key, value, space, diff_res):
    if isinstance(value, dict):
        add_dict_in_dict(
            space, f'{key}', value, diff_res)
    else:
        diff_res.append(
            f'{space}{DICT_SPACE}{key}: {value}'
        )
