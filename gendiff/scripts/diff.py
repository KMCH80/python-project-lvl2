def get_matched_old_data(data1: dict, data2: dict, diff: dict):
    for key1, value1 in data1.items():
        flag = False
        for key2, value2 in data2.items():
            if key1 == key2:
                flag = True
                if isinstance(value1, dict) and isinstance(value2, dict):
                    diff.update({key1: {}})
                    get_matched_old_data(value1, value2, diff[key1])
                else:
                    diff.update(
                        {key1: get_changed_or_not_status(value1, value2)})
                break
        if not flag:
            diff.update({key1: "deleted"})
    return diff


def get_changed_or_not_status(value1, value2):
    if value1 == value2:
        status = ""
    else:
        status = "changed"
    return status


def get_matched_new_data(data1: dict, data2: dict, diff: dict):
    for key1, value1 in data2.items():
        flag = False
        for key2, value2 in data1.items():
            if key1 == key2:
                flag = True
                if value1 != value2 and isinstance(value1, dict):
                    get_matched_new_data(value2, value1, diff[key1])
                break
        if not flag:
            diff.update({key1: "added"})
    return diff


def get_matched_data(data1, data2):
    diff = {}
    diff = get_matched_old_data(data1, data2, diff)
    diff = get_matched_new_data(data1, data2, diff)
    return diff
