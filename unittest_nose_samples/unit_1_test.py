import unittest


class TestLen(unittest.TestCase):

    def test_string_len(self):
        # Given: Input string
        string_to_test = '1'*10
        # When: len function is called on the target string:
        returned_len = len(string_to_test)
        # Then: Expected len value is returned
        self.assertEqual(returned_len, 10)

    def test_dict_len(self):
        # Given: dictionary to test
        # When: len function is called on the target string:
        returned_len = len(self.target_dict)
        # Then: Expected len value is returned
        self.assertEqual(returned_len, 2)

    def test_false(self):
        self.assertEqual(1, 2)


class TestUpper(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('aaa'.upper(), 'AAA')

# Different runners
# if __name__ == '__main__':
#     pytest.main()
#     unittest.main()
#     # python -m unittest unit_test_1.py
#     # pytest


if __name__ == '__main__':
    unittest.main()
