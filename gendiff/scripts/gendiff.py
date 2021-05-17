import argparse
import file_reader

from diff import match_templates
from stylish import str_formater


def generate_diff(first_file, second_file):
    templates = file_reader.get_dics_from_files(first_file, second_file)
    template1 = format_types(templates[0])
    template2 = format_types(templates[1])
    diff = match_templates(template1, template2)
    diff_res = []
    return str_formater(template1, template2, diff, diff_res)


def format_types(dic):
    for key, value in dic.items():
        if isinstance(value, dict):
            format_types(value)
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
    # print(generate_diff('files/file3_1.json', 'files/file3_2.json'))

if __name__ == '__main__':
    main()
