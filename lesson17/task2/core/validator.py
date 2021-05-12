from os import path

from ..core.data_provider import DataProvider
from ..core.messages import PhoneBookMessages


class Validator:

    @staticmethod
    def check_phonebook_presence(data_provider: DataProvider) -> bool:
        if path.exists(data_provider.get_argument()):
            return True
        else:
            print(f'The provided file: {data_provider.get_argument()} does NOT exist.')
            return False

    @staticmethod
    def check_arguments(data_provider: DataProvider) -> bool:
        if data_provider.get_argument():
            if Validator.check_phonebook_presence(data_provider):
                return True
            else:
                print(PhoneBookMessages.PROVIDE_FILE.value)
                return False
        else:
            print(PhoneBookMessages.PROVIDE_FILE.value)
            return False
