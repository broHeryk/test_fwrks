import unittest


class ParamsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.params = [(1, 1), (2, 0), (3, 0), (4, 0), (5, 1)]

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i, r in self.params:
            with self.subTest(i=i, r=r):
                self.assertEqual(i % 2, r)

if __name__ == '__main__':
    unittest.main()