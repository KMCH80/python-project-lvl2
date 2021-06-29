def get_matched_data(data1, data2):
    diff = {}
    diff = get_old_elements_changes(data1, data2, diff)
    diff = get_adds(data1, data2, diff)
    return diff


def get_old_elements_changes(data1: dict, data2: dict, diff: dict):
    for key, value in data1.items():
        if key in data2:
            if isinstance(value, dict) and isinstance(data2[key], dict):
                diff.update({key: {}})
                get_old_elements_changes(value, data2[key], diff[key])
            elif value == data2[key]:
                diff[key] = [value, 'not changed']
            else:
                diff[key] = [value, data2[key], 'changed']
        else:
            diff[key] = [value, 'deleted']
    return diff


def get_adds(data1: dict, data2: dict, diff: dict):
    for key, value in data2.items():
        if key not in data1:
            diff[key] = [value, 'added']
            continue
        if value != data1[key] and isinstance(value, dict) and isinstance(
                data1[key], dict):
            get_adds(data1[key], value, diff[key])
    return diff
