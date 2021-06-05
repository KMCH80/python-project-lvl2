import pytest
from gendiff import generate_diff


# test removed elements
@pytest.fixture
def result_test():
    with open('tests/fixtures/test8_json_format_res.txt') as f:
        result = f.read()
        print(result)
    return result


@pytest.fixture
def file1_test():
    return 'tests/fixtures/test6_tree_file1.json'


@pytest.fixture
def file2_test():
    return 'tests/fixtures/test6_tree_file2.json'


def test_json_formater(file1_test, file2_test, result_test):
    assert generate_diff(file1_test, file2_test, 'json') == result_test
