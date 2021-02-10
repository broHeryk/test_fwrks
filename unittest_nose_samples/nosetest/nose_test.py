import nose


def test_very_first():
    print(f'Execution test {test_very_first.__name__}')
    assert True


if __name__ == '__main__':
    nose.main()

