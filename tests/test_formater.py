import pytest
from gendiff.diff import generate_diff


@pytest.mark.parametrize("file1,file2,format_name,result_file", [
    ('tests/fixtures/test6_tree_file1.json',
     'tests/fixtures/test6_tree_file2.json',
     'json',
     'tests/fixtures/test8_json_format_res.txt'),
    ('tests/fixtures/test6_tree_file1.json',
     'tests/fixtures/test6_tree_file2.json',
     'plain',
     'tests/fixtures/test7_plain_res.txt'),
    ('tests/fixtures/test6_tree_file1.json',
     'tests/fixtures/test6_tree_file2.json',
     'stylish',
     'tests/fixtures/test6_tree_file_res.txt')
])
def test_diff(file1, file2, format_name, result_file):
    with open(result_file) as f:
        result = f.read()
    assert generate_diff(file1, file2, format_name) == result
