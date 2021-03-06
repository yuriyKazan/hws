import sys

from ..core.data_provider import DataProvider


class CLIDataProvider(DataProvider):

    __argument: str = ''

    @staticmethod
    def read_cli_argument() -> str:
        try:
            CLIDataProvider.__argument = sys.argv[1]
        except IndexError:
            print('Required argument was not found')
        return CLIDataProvider.__argument

    @staticmethod
    def get_argument() -> str:
        return CLIDataProvider.read_cli_argument()
