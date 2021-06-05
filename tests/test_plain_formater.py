import pytest
from gendiff import generate_diff


@pytest.fixture
def result_plain():
    with open('tests/fixtures/test7_plain_res.txt') as f:
        result = f.read()
        print(result)
    return result


@pytest.fixture
def file1_test():
    return 'tests/fixtures/test6_tree_file1.json'


@pytest.fixture
def file2_test():
    return 'tests/fixtures/test6_tree_file2.json'


def test_plain_json_diff(file1_test, file2_test, result_plain):
    assert generate_diff(file1_test, file2_test, 'plain') == result_plain


@pytest.fixture
def file1_yml_test():
    return 'files/file4_1.yml'


@pytest.fixture
def file2_yml_test():
    return 'files/file4_2.yml'


def test_plain_yml_diff(file1_yml_test, file2_yml_test, result_plain):
    assert generate_diff(
        file1_yml_test, file2_yml_test, 'plain') == result_plain
