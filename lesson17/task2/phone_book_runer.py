from typing import Union

from core.data_provider import DataProvider
from core.CLI_data_provider import CLIDataProvider
from core.messages import PhoneBookMessages
from core.phone_book import PhoneBook
from core.validator import Validator


def get_phonebook_name(data_provider: DataProvider) -> Union[str, None]:
    if Validator.check_arguments(data_provider):
        return data_provider.get_argument()
    return None


def search_item(phonebook: PhoneBook, phonebook_data) -> None:
    state: str = ""
    print(PhoneBookMessages.OPTIONS_TO_SEARCH.value)
    while state != "stop":
        state = input("Select a search option: ")
        if state not in ['sf', 'sp', 'sc', 'stop']:
            print(PhoneBookMessages.OPTIONS_TO_SEARCH.value)
        if state == 'sf':
            full_name = get_input('full_name')
            record = phonebook.search_by_full_name(phonebook_data, full_name)
            print(f'The record for full name {full_name} is: '
                  f'"{full_name}": {record}')
        elif state == 'sp':
            phone_number = get_input('phone_number')
            key_of_record = phonebook.search_by_phone_number(phonebook_data, phone_number)
            print(f'The record for phone number {phone_number} is: '
                  f'"{key_of_record}": {phonebook_data.get(key_of_record, None)}')
        elif state == 'sc':
            city = get_input('city')
            key_of_record = phonebook.search_by_city(phonebook_data, city)
            print(f'The record for city {city} is:'
                  f' "{key_of_record}": {phonebook_data.get(key_of_record, None)}')


def process_notebook_operations(phonebook: PhoneBook, phonebook_data) -> None:
    state: str = ""
    while state != "stop":
        state = input("Select an option: ")
        if state not in ['a', 's', 'd', 'u', 'stop']:
            print(PhoneBookMessages.MENU_MESSAGE.value)
        if state == "a":
            phonebook.add_item(phonebook_data, get_input('full_name'), get_input('phone_number'), get_input('city'))
            print(phonebook_data)
        elif state == "s":
            search_item(phonebook, phonebook_data)
        elif state == "d":
            print('Enter phone number for a record that will be deleted: ')
            phonebook.delete_item(phonebook_data, get_input('phone_number'))
        elif state == "u":
            print('Enter phone number for a record that will be updated: ')
            phone_number = get_input('phone_number')
            key = PhoneBook.get_key_of_record_by_value(phonebook_data, phone_number, 'number')
            print('Enter new data for update: ')
            phonebook.update_item(phonebook_data, key, get_input('full_name'), get_input('phone_number'),
                                  get_input('city'))
            print(phonebook_data)


def get_input(input_name: str) -> str:
    input_value: str = ''
    if 'full_name' == input_name:
        input_value = input('Enter full name: ')
    elif 'phone_number' == input_name:
        input_value = input('Enter phone number: ')
    elif 'city' == input_name:
        input_value = input('Enter city: ')
    return input_value


def process_notebook_flow() -> None:
    data_provider = CLIDataProvider()
    phonebook_file_name = get_phonebook_name(data_provider)
    if phonebook_file_name is None:
        return
    print(PhoneBookMessages.WELCOME_MESSAGE.value)
    phonebook = PhoneBook(phonebook_file_name)
    phonebook.initialise_book(data_provider)
    phone_book_data = phonebook.read_data_from_file()

    process_notebook_operations(phonebook, phone_book_data)
    phonebook.save_to_disk(phone_book_data)


if __name__ == '__main__':
    process_notebook_flow()
