import json
from os import stat

from task2.core.data_provider import DataProvider


class PhoneBook:
    def __init__(self, phonebook_name: str):
        self.name = phonebook_name

    def read_data_from_file(self):
        try:
            with open(self.name) as read_file:
                data = json.load(read_file)
        except OSError:
            print(f'Impossible to read data from the file {self.name}')
            raise RuntimeError
        return data

    def save_to_disk(self, data):
        with open(self.name, 'w') as file:
            json.dump(data, file)

    def initialise_book(self, data_provider: DataProvider):
        if stat(data_provider.get_argument()).st_size == 0:
            self.save_to_disk(dict())

    def add_item(self, phonebook_data: dict, full_name: str, phone_number: str, city: str):
        phonebook_data[full_name] = {'number': phone_number, 'city': city}
        self.save_to_disk(phonebook_data)

    def delete_item(self, phonebook_data: dict, phone_number: str):
        key_of_record_to_delete = PhoneBook.get_key_of_record_by_value(phonebook_data, phone_number, 'number')
        record_to_delete = phonebook_data[key_of_record_to_delete]
        phonebook_data.pop(key_of_record_to_delete, None)
        print(f'The record "{key_of_record_to_delete}": {record_to_delete} was successfully deleted')
        self.save_to_disk(phonebook_data)

    def update_item(self, phonebook_data: dict, key: str, full_name: str, phone_number: str, city: str):
        phonebook_data.pop(key, None)
        phonebook_data[full_name] = {'number': phone_number, 'city': city}
        self.save_to_disk(phonebook_data)

    @staticmethod
    def search_by_full_name(phonebook_data, full_name: str):
        return phonebook_data.get(full_name, None)

    @staticmethod
    def search_by_phone_number(phonebook_data, phone_number: str):
        return PhoneBook.get_key_of_record_by_value(phonebook_data, phone_number, 'number')

    @staticmethod
    def search_by_city(phonebook_data, city: str):
        return PhoneBook.get_key_of_record_by_value(phonebook_data, city, 'city')

    @staticmethod
    def get_key_of_record_by_value(phonebook_data: dict, value_to_search: str, item_to_search: str):
        key = ''
        record_exist = False
        for full_name, dict_value in phonebook_data.items():
            for item, value in dict_value.items():
                if item == item_to_search and value == value_to_search:
                    print(f"The record for value {value_to_search} was found")
                    record_exist = True
                    key = full_name
                    break
        if record_exist:
            return key
        else:
            return None
