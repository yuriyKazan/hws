import random


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_worker(self, worker):
        if not isinstance(worker, Worker):
            raise ValueError(f'Incorrect value of "worker", expected type Worker, but got {type(worker).__name__}')
        if not self.id == worker.boss.id:
            raise RuntimeError(f'Could not assign worker {worker.name} with id {worker.id}.'
                               f'This worker has already assigned boss {worker.boss.name} with id {worker.boss.id}')
        self.workers.append(worker)

    def __str__(self):
        return f'Instance of Boss class. ID:{self.id}; Name:{self.name}; Company:{self.company}; ' \
               f'Workers:{self.workers}'


class Worker:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss: Boss):
        if not isinstance(boss, Boss):
            raise ValueError(f'Incorrect value of "boss", expected type Boss, but got {type(boss).__name__}')
        self._boss = boss

    @boss.deleter
    def boss(self):
        self._boss = None

    def __str__(self):
        return f'Instance of Worker class. ID:{self.id}; Name:{self.name}; Company:{self.company};'


# worker_id = random.randint(1, 1000)
# boss_id = random.randint(1, 1000)
# w = Worker(worker_id, 'Some name', 'Some company')
# w.boss = Boss(boss_id, 'A name', 'A company')
# print(w, w.boss.id, w.boss.name)
# del w.boss
# print(w, w.boss)
# b = Boss(random.randint(1, 1000), 'A name', 'A company')
# w.boss = b
# b.add_worker(w)
# print(b)
# w2 = Worker(random.randint(1, 1000), 'Some name2', 'Some company2')
# w2.boss = Boss(random.randint(1, 1000), 'A name', 'A company')
# b.add_worker(w2)
