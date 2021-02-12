import pytest

# fixtures documentation order example
order = []


@pytest.fixture(scope="session")
def s1():
    print('Session setup')
    order.append("s1")


@pytest.fixture(scope="module")
def m1():
    print('Module setup')
    order.append("m1")


@pytest.fixture
def f1(f3):
    order.append("f1")


@pytest.fixture
def f3():
    order.append("f3")


@pytest.fixture(autouse=True)
def a1():
    order.append("a1")


@pytest.fixture
def f2():
    order.append("f2")
    print('set up f2')
    yield 'some_value'
    print('teardown f2')


def test_order(f1, m1, f2, s1):
    assert f2 == 'some_value'
    assert order == ["s1", "m1", "a1", "f3", "f1", "f2"]

