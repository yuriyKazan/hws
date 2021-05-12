class MyContext:
    __counter = 0

    def __init__(self, log_name):
        self.__log_name = log_name

    def __enter__(self):
        MyContext.__counter += 1
        print(f'{self.__log_name}: The context manager was called {MyContext.__counter} times')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if all([exc_type, exc_val, exc_tb]):
            raise RuntimeError(exc_type, exc_val, exc_tb)
        print(f'{self.__log_name}: Closing context manager counter is {self.__counter}')
        return None

    def get_log_name(self):
        return self.__log_name

    @staticmethod
    def get_counter():
        return MyContext.__counter


if __name__ == '__main__':
    with MyContext('log 1') as cont1:
        print(f'Counter = {cont1.get_counter()}')

    with MyContext('log 2') as cont2:
        print(f'The log name is - {cont2.get_log_name()}')
        a = 1/0
