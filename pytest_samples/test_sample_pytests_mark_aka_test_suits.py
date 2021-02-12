import pytest


@pytest.mark.stringtest
def test_len_function_for_string():
    expected_len = 20
    test_string = '1'*expected_len
    assert len(test_string) == expected_len


@pytest.mark.dicttest
def test_len_function_for_dict():
    expected_len = 20
    test_dict = {i: f'val_{i}' for i in range(expected_len)}
    assert len(test_dict) == expected_len


@pytest.mark.stringtest
def test_set_function_for_string():
    expected_range = 10
    test_string = ''.join([str(i) for i in range(expected_range)])
    set_of_chars = set(test_string)
    for i in range(expected_range):
        assert str(i) in set_of_chars


@pytest.mark.dicttest
def test_set_function_for_dict():
    expected_range = 20
    test_string = {i: i for i in range(expected_range)}
    set_of_chars = set(test_string)
    for i in range(expected_range):
        assert i in set_of_chars

#pytest -v -m dicttest
#pytest -v -m stringtest
