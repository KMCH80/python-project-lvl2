import argparse
from gendiff.diff import STYLE_OPT_JSON, STYLE_OPT_PLAIN, STYLE_OPT_STYLISH
from gendiff.diff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')
    parser.add_argument('-f', '--format', choices=[STYLE_OPT_STYLISH,
                        STYLE_OPT_PLAIN, STYLE_OPT_JSON],
                        default=STYLE_OPT_STYLISH, help='set format of output')
    args = parser.parse_args()
    try:
        print(generate_diff(args.first_file, args.second_file, args.format))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
