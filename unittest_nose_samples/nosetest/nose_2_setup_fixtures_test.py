from nose import with_setup


def setup_module():
    print('Module setup is called')


def teardown_module():
    print('Module teardown is called')


def setup_func():
    "set up test fixtures"
    print('Function setup is called')
    return {1: 2}


def teardown_func():
    "tear down test fixtures"
    print('Function teardown is called')


@with_setup(setup_func, teardown_func)
def test_simple_nose():
    print(f'Execution test {test_simple_nose.__name__}')
    assert True


def test_another_another_test():
    print(f'Execution test {test_another_another_test.__name__}')
    assert True
