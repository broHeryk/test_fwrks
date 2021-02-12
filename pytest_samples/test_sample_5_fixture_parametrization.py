# content of test_module.py
import pytest

from logic_functions import is_balanced

#
# @pytest.fixture(scope="module", params=["mod1", "mod2"])
# def modarg(request):
#     param = request.param
#     print("\n  SETUP modarg", param)
#     yield param
#     print("\n  TEARDOWN modarg", param)
#
#
# @pytest.fixture(scope="function", params=[1, 2])
# def otherarg(request):
#     param = request.param
#     print("\n  SETUP otherarg", param)
#     yield param
#     print("\n  TEARDOWN otherarg", param)
#
#
# def test_0(otherarg):
#     print("  RUN test0 with otherarg", otherarg)
#
#
# def test_1(modarg):
#     print("  RUN test1 with modarg", modarg)
#
#
# def test_2(otherarg, modarg):
#     print("  RUN test2 with otherarg {} and modarg {}".format(otherarg, modarg))


testdata =[
    ('{}', True),
    ('[', False)
]
@pytest.mark.parametrize("inp,expected", testdata)
def test_is_balanced(inp, expected):
    assert is_balanced(inp) == expected





# testdata = [
#     ('{[()]}', True),
#     ('{[(])}', False),
#     ('{{[[(())]]}}', True),
#     ('{(([])[])[]}', False),
#     ('{(([])[])[]]}', False),
#     ('{(([])[])[]}[]', True),
#     ('{(([])[])[]}[[[', False),
# ]
#

# testdata = [
#     ('{[()]}', True),
#     ('{[(])}', False),
#     ('{{[[(())]]}}', True),
#     ('{(([])[])[]}', False),
#     ('{(([])[])[]]}', False),
#     ('{(([])[])[]}[]', True),
#     ('{(([])[])[]}[[[', False),
# ]
# @pytest.mark.parametrize("inp,expected", testdata)
