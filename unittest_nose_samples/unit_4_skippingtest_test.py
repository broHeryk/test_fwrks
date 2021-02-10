import unittest
import os
import sys

class PathBuilderTest(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_will_not_be_executed(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(sys.platform.startswith("win"), 'Does not make sense for non linux os')
    def test_format(self):
        path = os.path.abspath(__file__)
        # Checks if module is located under root
        self.assertTrue(path.startswith('/'))

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        path = os.path.abspath(__file__)
        # Checks if module is located on C disc
        self.assertTrue(path.startswith('C:'))

    @unittest.expectedFailure
    def test_check_if_root(self):
        path = os.path.abspath(__file__)
        # Checks if module is located on C disc
        self.assertTrue(path.startswith('/'))
