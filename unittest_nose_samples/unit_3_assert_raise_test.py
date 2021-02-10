import unittest


class DivisionTest(unittest.TestCase):

    def test_normal_division(self):
        self.assertAlmostEqual(100/5, 20)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            res = 100 / 0
