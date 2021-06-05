import pytest
from gendiff import generate_diff


# test removed elements
@pytest.fixture
def result_test1():
    with open('tests/fixtures/test1_file_res.txt') as f:
        result = f.read()
        print(result)
    return result


@pytest.fixture
def file1_test1():
    return 'tests/fixtures/test1_file1.yml'


@pytest.fixture
def file2_test1():
    return 'tests/fixtures/test1_file2.yml'


def test_removes_generate_diff(file1_test1, file2_test1, result_test1):
    assert generate_diff(file1_test1, file2_test1) == result_test1


# test added elements
@pytest.fixture
def result_test2():
    with open('tests/fixtures/test2_file_res.txt') as f:
        result = f.read()
        print(result)
    return result


@pytest.fixture
def file1_test2():
    return 'tests/fixtures/test2_file1.yml'


@pytest.fixture
def file2_test2():
    return 'tests/fixtures/test2_file2.yml'


def test_adds_generate_diff(file1_test2, file2_test2, result_test2):
    assert generate_diff(file1_test2, file2_test2) == result_test2


# test changed elements
@pytest.fixture
def result_test3():
    with open('tests/fixtures/test3_file_res.txt') as f:
        result = f.read()
        print(result)
    return result


@pytest.fixture
def file1_test3():
    return 'tests/fixtures/test3_file1.yml'


@pytest.fixture
def file2_test3():
    return 'tests/fixtures/test3_file2.yml'


def test_changes_generate_diff(file1_test3, file2_test3, result_test3):
    assert generate_diff(file1_test3, file2_test3) == result_test3


# test static elements
@pytest.fixture
def result_test4():
    with open('tests/fixtures/test4_file_res.txt') as f:
        result = f.read()
        print(result)
    return result


@pytest.fixture
def file1_test4():
    return 'tests/fixtures/test4_file1.yml'


@pytest.fixture
def file2_test4():
    return 'tests/fixtures/test4_file2.yml'


def test_static_generate_diff(file1_test4, file2_test4, result_test4):
    assert generate_diff(file1_test4, file2_test4) == result_test4


# test sorted elements
@pytest.fixture
def result_test5():
    with open('tests/fixtures/test5_file_res.txt') as f:
        result = f.read()
        print(result)
    return result


@pytest.fixture
def file1_test5():
    return 'tests/fixtures/test5_file1.yml'


@pytest.fixture
def file2_test5():
    return 'tests/fixtures/test5_file2.yml'


def test_sorted_generate_diff(file1_test5, file2_test5, result_test5):
    assert generate_diff(file1_test5, file2_test5) == result_test5
