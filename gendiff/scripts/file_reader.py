import os
import yaml
import json


def get_dics_from_files(first_file, second_file):
    extention1 = os.path.splitext(first_file)[1]
    extention2 = os.path.splitext(second_file)[1]
    if (extention1 == ".yml" and extention2 == ".yml"):
        return get_dic_yml(first_file), get_dic_yml(second_file)
    elif (extention1 == ".json" and extention2 == ".json"):
        return get_dic_json(first_file), get_dic_json(second_file)
    else:
        return 0


def get_dic_yml(file):
    with open(file) as f:
        return yaml.safe_load(f)


def get_dic_json(file):
    with open(file) as f:
        return json.load(f)


def main():
    pass


if __name__ == '__main__':
    main()
