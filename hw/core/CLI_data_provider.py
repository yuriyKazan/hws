import sys

from hw.core.data_provider import DataProvider


class CLIDataProvider(DataProvider):

    __argument = ''

    @staticmethod
    def read_cli_argument():
        try:
            CLIDataProvider.__argument = sys.argv[1]
        except IndexError:
            print('Required argument was not found')
        return CLIDataProvider.__argument

    @staticmethod
    def get_argument():
        return CLIDataProvider.read_cli_argument()
