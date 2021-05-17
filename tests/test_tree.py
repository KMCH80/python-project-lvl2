import pytest
from diff import match_templates
from stylish import str_formater


@pytest.mark.parametrize('tree1, tree2, expected', [
    ({"common": {
        "follow": "false",
        "setting1": "Value 1",
        "setting3": "null",
        "setting4": "blah blah",
        "setting5": {
            "key5": "value5"
        },
        "setting6": {
            "key": "value",
            "ops": "vops",
            "doge": {
                "wow": "so much"
            }
        }
    }
    },
        {"common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": "true",
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": "",
                    "new": 1
                }
            }
        }
    },
        {"common": {
            "follow": "deleted",
            "setting1": "",
            "setting2": "added",
            "setting3": "changed",
            "setting4": "deleted",
            "setting5": "deleted",
            "setting6": {
                "doge": {
                    "wow": "changed",
                    "new": "added"
                },
                "key": "",
                "ops": "deleted"
            }
        }
    }),
])
def test_tree(tree1, tree2, expected):
    assert match_templates(tree1, tree2) == expected


@pytest.mark.parametrize('tree1, tree2, expected', [
    ({"group1": {
        "baz": "bas",
        "foo": "bar",
        "nest": {
            "key": "value"
        }
    },
        "group2": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
    }
    },
        {"group1": {
            "foo": "bar",
            "baz": "bars",
            "nest": "str"
        },
        "group3": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    },
        ['    group1: {',
         '      - baz: bas',
         '      + baz: bars',
         '        foo: bar',
         '      - nest: {',
         '            key: value',
         '        }',
         '      + nest: str',
         '    }',
         '  - group2: {',
         '        abc: 12345',
         '        deep: {',
         '            id: 45',
         '        }',
         '    }',
         '  + group3: {',
         '        deep: {',
         '            id: {',
         '                number: 45',
         '            }',
         '        }',
         '        fee: 100500',
         '    }']),
])
def test_tree2(tree1, tree2, expected):
    diff = match_templates(tree1, tree2)
    diff_res = []
    str = '{\n' + '\n'.join(expected) + '\n}'
    assert str_formater(tree1, tree2, diff, diff_res) == str
