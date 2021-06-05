import os
import yaml
import json
import sys


def get_data_from_files(file1, file2):
    extention1 = os.path.splitext(file1)[1]
    extention2 = os.path.splitext(file2)[1]
    if (extention1 == ".yml" and extention2 == ".yml"):
        return get_data_from_yml(file1), get_data_from_yml(file2)
    elif (extention1 == ".json" and extention2 == ".json"):
        return get_data_from_json(file1), get_data_from_json(file2)
    else:
        return 0


def get_data_from_yml(file):
    try:
        with open(file) as f:
            return yaml.safe_load(f)
    except OSError:
        print('Could not open file:', file)
        sys.exit()


def get_data_from_json(file):
    try:
        with open(file) as f:
            return json.load(f)
    except OSError:
        print('Could not open file:', file)
        sys.exit()


def main():
    pass


if __name__ == '__main__':
    main()
