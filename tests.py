import unittest

from task2.test.test_CLI_data_provider import TestCLIDataProvider
from task2.test.test_phone_book import TestPhoneBook
from task2.test.test_validator import TestValidator


def run_all():
    scale_test_suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(TestCLIDataProvider),
        unittest.TestLoader().loadTestsFromTestCase(TestPhoneBook),
        unittest.TestLoader().loadTestsFromTestCase(TestValidator)
    ])
    result = unittest.TestResult()
    runner = unittest.TextTestRunner()
    print(runner.run(scale_test_suite))
    print('result: ', result)


if __name__ == '__main__':
    run_all()
