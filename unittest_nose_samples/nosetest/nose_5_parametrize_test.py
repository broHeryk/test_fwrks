# from nose2.tools import params
import unittest


# Parmaetrization does not supported out of the box but it could be easily written

#
# @params(1,2,3)
# def test_is_even(num):
#     assert 1 % 2 == 1
#
#
#
# class Test(unittest.TestCase):
#
#     @params((1, 2), (2, 3), (4, 5))
#     def test_less_than(self, a, b):
#         assert a < b

def test_is_even():
    test_data = [(1, 1), (2, 0), (3, 0), (4, 0), (5, 1)]
    for v, exp in test_data:
        assert v % 2 == exp

