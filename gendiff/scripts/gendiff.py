import argparse
import os
from gendiff import file_reader
from gendiff.formaters.stylish import stylish_formater
from gendiff.formaters.plain import plain_formater
from gendiff.formaters.json import json_formater
from gendiff.diff import get_matched_data


def generate_diff(file1, file2, format_name=0):
    try:
        data1 = file_reader.get_data_from_file(file1)
        data2 = file_reader.get_data_from_file(file2)
    except FileNotFoundError:
        print("File not found!")
    diff = get_matched_data(data1, data2)
    diff_result = []
    diff_json_result = {}
    if format_name == 'plain':
        return plain_formater(diff, diff_result)
    elif format_name == 'json':
        return json_formater(diff, diff_json_result)
    else:
        return stylish_formater(diff, diff_result)


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')
    parser.add_argument('-f', '--format', choices=['plain', 'json'],
                        help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
