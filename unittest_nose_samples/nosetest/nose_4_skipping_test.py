from nose.tools import nottest


def test_function():
    print('Another test')
    assert 1 == 1


@nottest
def test_function_will_be_skipped():
    assert 10 == 100
