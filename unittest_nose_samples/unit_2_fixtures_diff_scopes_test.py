import unittest
import os

def setUpModule():
    print(f'\nSetting up the module {__name__}')

def tearDownModule():
    print(f'Tearing down the module {__name__}')


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls._connection = {'connection_id': 10}
        print(f'\nClass {cls.__name__} setup is called, connection is established {cls._connection}')

    @classmethod
    def tearDownClass(cls):
        del(cls._connection['connection_id'])
        print(f'\nClass {cls.__name__} teardown is called, connection is destroyed {cls._connection}')

    def setUp(self) -> None:
        self.request_data = [1, 2, 3]
        print(f'\nFunction set up is called {self.request_data}')

    def tearDown(self) -> None:
        print(f'\nFunction teardown is called {self.request_data}')

    def test_send_to_connection(self):
        # print(os.environ)
        print('Sending to connection')
        print(self.__class__._connection)
        print(self.request_data)
        self.assertEqual(self.__class__._connection['connection_id'], 10)


class AnotherTest(unittest.TestCase):

    def test_something(self):
        print(f'executing test function from {self.__class__.__name__}')
        self.assertEqual(1, 1)
