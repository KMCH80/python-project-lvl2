import pytest
from gendiff import generate_diff


@pytest.mark.parametrize("file1,file2,result_file", [
    ('tests/fixtures/test6_tree_file1.json',
     'tests/fixtures/test6_tree_file2.json',
     'tests/fixtures/test7_plain_res.txt'),
    ('files/file4_1.yml',
     'files/file4_2.yml',
     'tests/fixtures/test7_plain_res.txt')
])
def test_diff(file1, file2, result_file):
    with open(result_file) as f:
        result = f.read()
    assert generate_diff(file1, file2, 'plain') == result
