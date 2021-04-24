import sys
import unittest

from task2.core.CLI_data_provider import CLIDataProvider
from task2.core.validator import Validator


class TestValidator(unittest.TestCase):
    __validator = None
    __data_provider = None

    @classmethod
    def setUpClass(cls):
        cls.__file_example = 'test_data.json'
        cls.__data_provider = CLIDataProvider()
        cls.__validator = Validator()
        sys.argv.insert(1, cls.__file_example)

    def test_check_phonebook_presence(self):
        self.assertTrue(TestValidator.__validator.check_phonebook_presence(TestValidator.__data_provider))

    def test_check_arguments(self):
        self.assertTrue(TestValidator.__validator.check_phonebook_presence(TestValidator.__data_provider))

    @classmethod
    def tearDownClass(cls):
        if len(sys.argv) > 1:
            sys.argv.pop(1)
