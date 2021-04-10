#!/usr/bin/env python3

import argparse
import json
import collections


def generate_diff(first_file, second_file):
    diff_res = []
    with open(first_file) as f1:
        template1 = json.load(f1)
    with open(second_file) as f2:
        template2 = json.load(f2)
    union_template = dict(template1.items() | template2.items())
    template_order = collections.OrderedDict(sorted(union_template.items()))
    template_inter = dict(template1.items() & template2.items())
    for key in template_order.keys():
        if key in template_inter.keys():
            diff_res.append(f'{key}: {template_inter[key]}')
        elif key in template1.keys() and key in template2.keys():
            diff_res.append(f'- {key}: {template1[key]}')
            diff_res.append(f'+ {key}: {template2[key]}')
        elif key in template1.keys() and key not in template2.keys():
            diff_res.append(f'- {key}: {template1[key]}')
        else:
            diff_res.append(f'+ {key}: {template2[key]}')

    print(template1)
    print(template2)

    str = '\n'.join(diff_res)
    return str


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
