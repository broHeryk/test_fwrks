import pytest
import sys
import os

# pexpect = pytest.importorskip("pexpect")

@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    assert 111 == 222


def test_function():
    if not 2 == 3:
        pytest.skip("unsupported configuration")

@pytest.mark.skipif(sys.platform != "win32", reason="tests for linux only")
def test_windows_path():
    path = os.path.abspath(__file__)
    # Checks if module is located under root
    assert path.startswith('C:')


@pytest.mark.xfail(sys.platform == "win32", reason="bug in a 3rd party library")
def test_linux_path():
    path = os.path.abspath(__file__)
    # Checks if module is located under root
    assert path.startswith('/')


