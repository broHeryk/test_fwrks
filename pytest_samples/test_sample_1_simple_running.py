import pytest



@pytest.fixture(scope="session")
def s2():
    print('Session setup from s2')

def test_len():
    string_to_test = '+'*10
    assert 10 == len(string_to_test)

if __name__ == '__main__':
    pytest.main()