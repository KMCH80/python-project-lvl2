import pytest
from gendiff import generate_diff


# test removed elements
@pytest.fixture
def result_test6():
    with open('tests/fixtures/test6_tree_file_res.txt') as f:
        result = f.read()
        print(result)
    return result


@pytest.fixture
def file1_test6():
    return 'tests/fixtures/test6_tree_file1.json'


@pytest.fixture
def file2_test6():
    return 'tests/fixtures/test6_tree_file2.json'


def test_generate_diff(file1_test6, file2_test6, result_test6):
    assert generate_diff(file1_test6, file2_test6) == result_test6
