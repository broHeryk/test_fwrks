from nose.tools import raises


@raises(ZeroDivisionError)
def test_raises_zero_error():
    assert (5/0) == 100


@raises(ZeroDivisionError)
def test_no_raises_zero_error():
    assert (5/0)
