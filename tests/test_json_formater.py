import pytest
from gendiff import generate_diff


@pytest.mark.parametrize("file1,file2,result_file", [
    ('tests/fixtures/test6_tree_file1.json',
     'tests/fixtures/test6_tree_file2.json',
     'tests/fixtures/test8_json_format_res.txt')
])
def test_diff(file1, file2, result_file):
    with open(result_file) as f:
        result = f.read()
    assert generate_diff(file1, file2, 'json') == result
