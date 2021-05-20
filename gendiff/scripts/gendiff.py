import argparse
import file_reader

from diff import match_templates
from formaters.stylish import stylish_formater
from formaters.plain import plain_formater


def generate_diff(first_file, second_file, format_name=0):
    templates = file_reader.get_dics_from_files(first_file, second_file)
    template1 = format_types(templates[0])
    template2 = format_types(templates[1])
    diff = match_templates(template1, template2)
    diff_res = []
    if format_name == 'plain':
        return plain_formater(template1, template2, diff, diff_res)
    else:
        return stylish_formater(template1, template2, diff, diff_res)


def format_types(dic):
    dic_of_types = {
        'True': "true",
        'False': "false",
        'None': "null",
    }
    for key, value in dic.items():
        if isinstance(value, dict):
            format_types(value)
        if str(value) in dic_of_types:
            dic[key] = dic_of_types[str(value)]
    return dic


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
