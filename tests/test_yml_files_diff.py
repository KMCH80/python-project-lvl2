import pytest
from gendiff import generate_diff


@pytest.mark.parametrize("file1,file2,result_file", [
    ('tests/fixtures/test1_file1.yml',
     'tests/fixtures/test1_file2.yml',
     'tests/fixtures/test1_file_res.txt'),
    ('tests/fixtures/test2_file1.yml',
     'tests/fixtures/test2_file2.yml',
     'tests/fixtures/test2_file_res.txt'),
    ('tests/fixtures/test3_file1.yml',
     'tests/fixtures/test3_file2.yml',
     'tests/fixtures/test3_file_res.txt'),
    ('tests/fixtures/test4_file1.yml',
     'tests/fixtures/test4_file2.yml',
     'tests/fixtures/test4_file_res.txt'),
    ('tests/fixtures/test5_file1.yml',
     'tests/fixtures/test5_file2.yml',
     'tests/fixtures/test5_file_res.txt')
])
def test_diff(file1, file2, result_file):
    with open(result_file) as f:
        result = f.read()
    assert generate_diff(file1, file2) == result
