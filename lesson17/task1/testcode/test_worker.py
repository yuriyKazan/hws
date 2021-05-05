import unittest

from ..code.task1 import Boss, Worker


class TestWorker(unittest.TestCase):

    def setUp(self) -> None:
        self.worker_id = 456
        self.worker_name = 'A Worker'
        self.worker_company = 'A company'
        self.worker = Worker(self.worker_id, self.worker_name, self.worker_company)
        self.boss = Boss(654, 'A boss', 'A company')

    def test_create_worker(self):
        self.assertEqual(self.worker_id, self.worker.id)
        self.assertEqual(self.worker_name, self.worker.name)
        self.assertEqual(self.worker_company, self.worker.company)

    def test_get_boss(self):
        self.worker._boss = self.boss
        self.assertEqual(self.worker.boss, self.boss)

    def test_set_boss(self):
        self.worker.boss = self.boss
        self.assertEqual(self.worker._boss, self.boss)

    def test_delete_boss(self):
        del self.worker.boss
        self.assertEqual(self.worker._boss, None)


if __name__ == '__main__':
    unittest.main()
