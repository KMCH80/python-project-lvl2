import argparse
import file_reader

from diff import get_matched_data
from formaters.stylish import stylish_formater
from formaters.plain import plain_formater
from formaters.json import json_formater


def generate_diff(file1, file2, format_name=0):
    get_data_from_file1_file2 = file_reader.get_data_from_files(
        file1, file2)
    data1 = format_special_types(get_data_from_file1_file2[0])
    data2 = format_special_types(get_data_from_file1_file2[1])
    diff = get_matched_data(data1, data2)
    diff_result = []
    diff_json_result = {}
    if format_name == 'plain':
        return plain_formater(data1, data2, diff, diff_result)
    elif format_name == 'json':
        return json_formater(data1, data2, diff, diff_json_result)
    else:
        return stylish_formater(data1, data2, diff, diff_result)


def format_special_types(dic):
    dic_of_types = {
        'True': "true",
        'False': "false",
        'None': "null",
    }
    for key, value in dic.items():
        if isinstance(value, dict):
            format_special_types(value)
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
