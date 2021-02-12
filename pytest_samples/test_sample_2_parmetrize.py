import pytest
from logic_functions import is_balanced


def test_is_balanced():
    inp = '{[]}'
    expected = True
    assert is_balanced(inp) == expected


if __name__ == '__main__':
    pytest.main()
















''

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
