import unittest

from task1.test.test_boss import TestBoss
from task1.test.test_worker import TestWorker


def run_all():
    scale_test_suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(TestBoss),
        unittest.TestLoader().loadTestsFromTestCase(TestWorker)
    ])
    result = unittest.TestResult()
    runner = unittest.TextTestRunner()
    print(runner.run(scale_test_suite))
    print('result: ', result)


if __name__ == '__main__':
    run_all()
