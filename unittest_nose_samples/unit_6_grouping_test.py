import unittest
from unittest_nose.unit_1_test import TestLen
from unittest_nose.unit_4_skippingtest_test import PathBuilderTest


def suite():
    st = unittest.TestSuite()
    st.addTest(TestLen('test_string_len'))
    st.addTest(PathBuilderTest('test_windows_support'))
    return st


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())