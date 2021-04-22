import argparse
import file_reader
import collections


def generate_diff(first_file, second_file):
    diff_res = []
    templates = file_reader.get_dics_from_files(first_file, second_file)
    template1 = format_types(templates[0])
    template2 = format_types(templates[1])

    union_template = dict(template1.items() | template2.items())
    template_order = collections.OrderedDict(sorted(union_template.items()))
    template_intersect = dict(template1.items() & template2.items())
    for key in template_order.keys():
        if key in template_intersect.keys():
            diff_res.append(f'    {key}: {template_intersect[key]}')
        elif key in template1.keys() and key in template2.keys():
            diff_res.append(f'  - {key}: {template1[key]}')
            diff_res.append(f'  + {key}: {template2[key]}')
        elif key in template1.keys() and key not in template2.keys():
            diff_res.append(f'  - {key}: {template1[key]}')
        else:
            diff_res.append(f'  + {key}: {template2[key]}')
    str = '{\n' + '\n'.join(diff_res) + '\n}'
    return str


def format_types(dic):
    for key, value in dic.items():
        if value is True:
            dic[key] = 'true'
        elif value is False:
            dic[key] = 'false'
        elif value is None:
            dic[key] = 'null'
    return dic


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
