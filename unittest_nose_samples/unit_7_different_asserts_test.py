import unittest

class VarietyOfAssertTest(unittest.TestCase):

    def test_almost_equality(self):
        fraction = (0.1 + 0.1 + 0.1) / 3
        expected = 0.1
        #MUST BE 0.1 but not in python
        self.assertNotEqual(fraction, expected)
        self.assertAlmostEqual((0.1 + 0.1 + 0.1)/3, 0.2, places=4)
        self.assertAlmostEqual(fraction + 0.001, 0.1, places=2)
        self.assertNotAlmostEqual(fraction + 0.01, 0.2, places=2)
        assert round((0.1 + 0.1 + 0.1)/3, 4) == 0.1

    def test_greater_less(self):
        self.assertGreater(5, 4)
        self.assertGreaterEqual(5, 5)
        self.assertLess(4, 5)
        self.assertLessEqual(4, 4)



