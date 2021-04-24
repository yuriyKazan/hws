import unittest
import sys

from hw.core.CLI_data_provider import CLIDataProvider


class TestCLIDataProvider(unittest.TestCase):
    __file_example = ''
    __data_provider = None

    @classmethod
    def setUpClass(cls):
        cls.__file_example = 'test_data.json'
        cls.__data_provider = CLIDataProvider()
        sys.argv.insert(1, cls.__file_example)

    def test_get_argument(self):
        self.assertEqual(TestCLIDataProvider.__data_provider.get_argument(), TestCLIDataProvider.__file_example,
                         f'Expected and actual arguments are not equal')

    def test_read_cli_argument(self):
        self.assertEqual(TestCLIDataProvider.__data_provider.read_cli_argument(), TestCLIDataProvider.__file_example,
                         f'Expected and actual arguments are not equal')

    @classmethod
    def tearDownClass(cls):
        if len(sys.argv) > 1:
            sys.argv.pop(1)
