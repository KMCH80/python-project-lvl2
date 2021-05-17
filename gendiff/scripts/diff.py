def match_templates_old_items(template1: dict, template2: dict, diff: dict):
    for key1, value1 in template1.items():
        flag = False
        for key2, value2 in template2.items():
            if key1 == key2:
                flag = True
                if value1 == value2:
                    diff.update({key1: ""})
                elif isinstance(value1, dict) and isinstance(value2, dict):
                    diff.update({key1: {}})
                    match_templates_old_items(value1, value2, diff[key1])
                else:
                    diff.update({key1: "changed"})
                break
        if not flag:
            diff.update({key1: "deleted"})
    return diff


def match_templates_new(template1: dict, template2: dict, diff: dict):
    for key1, value1 in template2.items():
        flag = False
        for key2, value2 in template1.items():
            if key1 == key2:
                flag = True
                if value1 != value2 and isinstance(value1, dict):
                    match_templates_new(value2, value1, diff[key1])
                break
        if not flag:
            diff.update({key1: "added"})
    return diff


def match_templates(template1, template2):
    diff = {}
    diff = match_templates_old_items(template1, template2, diff)
    diff = match_templates_new(template1, template2, diff)
    return diff
