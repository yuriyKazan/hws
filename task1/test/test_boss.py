import unittest

from task1.code.task1 import Boss, Worker


class TestBoss(unittest.TestCase):

    def setUp(self) -> None:
        self.boss_id = 123
        self.boss_name = 'Boss'
        self.boss_company = 'Company'
        self.boss = Boss(self.boss_id, self.boss_name, self.boss_company)

    def test_create_boss(self):
        self.assertEqual(self.boss_id, self.boss.id)
        self.assertEqual(self.boss_name, self.boss.name)
        self.assertEqual(self.boss_company, self.boss.company)

    def test_add_worker(self):
        self.worker = Worker(321, 'Worker', 'Company')
        self.worker._boss = self.boss
        self.boss.add_worker(self.worker)
        self.assertEqual(self.boss.workers[0], self.worker)

    def tearDown(self) -> None:
        del self.boss


if __name__ == '__main__':
    unittest.main()
