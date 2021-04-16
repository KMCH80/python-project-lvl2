import pytest
from gendiff import generate_diff


@pytest.fixture
def result_file():
    with open('tests/fixtures/file_res.txt') as f:
        result = f.read()
        print(result)
    return result


@pytest.fixture
def file1_data():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def file2_data():
    return 'tests/fixtures/file2.json'


def test_generate_diff(file1_data, file2_data, result_file):
    assert generate_diff(file1_data, file2_data) == result_file
