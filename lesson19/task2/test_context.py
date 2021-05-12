import unittest
from ..task1.context import MyContext


class TestContext(unittest.TestCase):
    def setUp(self) -> None:
        self.test_log_name = 'test_log'
        self.context_instance = MyContext(self.test_log_name)

    def test_init(self):
        self.assertEqual(self.context_instance.get_log_name(), self.test_log_name)

    def test_enter(self):
        current_counter = self.context_instance.get_counter()
        self.context_instance.__enter__()
        self.assertEqual(current_counter + 1, self.context_instance.get_counter())

    def test_exit(self):
        self.assertEqual(self.context_instance.__exit__(None, None, None), None)

    def test_exit_with_error(self):
        self.assertRaises(RuntimeError, self.context_instance.__exit__,
                          'ZeroDivisionError', 'Error_massage', 'Traceback')
