from gendiff.formaters.stylish import stylish_formater
from gendiff.formaters.plain import plain_formater
from gendiff.formaters.json import json_formater

STYLE_OPT_JSON = 'json'
STYLE_OPT_PLAIN = 'plain'
STYLE_OPT_STYLISH = 'stylish'


def get_selected_format(format_name, diff):
    if format_name == STYLE_OPT_PLAIN:
        return plain_formater(diff)
    if format_name == STYLE_OPT_JSON:
        return json_formater(diff)
    if format_name == STYLE_OPT_STYLISH:
        return stylish_formater(diff)
    raise Exception("Wrong format_name!")
