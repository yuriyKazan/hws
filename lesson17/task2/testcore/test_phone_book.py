import json
import os
import sys
import unittest

from ..core.CLI_data_provider import CLIDataProvider
from ..core.phone_book import PhoneBook


def get_data_from_file(file_name):
    with open(file_name) as read_file:
        data = json.load(read_file)
    return data


def write_data_to_file(data, file_name):
    with open(file_name, 'w') as write_file:
        json.dump(data, write_file)


class TestPhoneBook(unittest.TestCase):
    __phone_book = None
    __data_provider = None
    __file_example = ''
    __mock_data = dict(John_Deer=dict(number="098765432", city="Los-Angeles"))
    __mock_data2 = dict(John_Deer2=dict(number="0987654322", city="Los-Angeles2"))

    @classmethod
    def setUpClass(cls):
        cls.__file_example = 'test_data.json'
        cls.__phone_book = PhoneBook(cls.__file_example)
        cls.__data_provider = CLIDataProvider()

    def setUp(self):
        write_data_to_file(TestPhoneBook.__mock_data, TestPhoneBook.__file_example)

    def test_read_data_from_file(self):
        self.assertEqual(TestPhoneBook.__phone_book.read_data_from_file(), TestPhoneBook.__mock_data,
                         f'Expected and actual data are not equal')

    def test_save_to_disk(self):
        TestPhoneBook.__phone_book.save_to_disk(TestPhoneBook.__mock_data2)
        data = get_data_from_file(TestPhoneBook.__file_example)
        self.assertEqual(data, TestPhoneBook.__mock_data2, f'Expected and actual data are not equal')

    def test_initialise_book(self):
        test_file = 'testcode.json'
        if not os.path.exists(test_file):
            with open(test_file, "w") as file:
                json.dump(dict(), file)
        sys.argv.insert(1, test_file)

        TestPhoneBook.__phone_book.initialise_book(TestPhoneBook.__data_provider)
        data = get_data_from_file(test_file)
        self.assertEqual(data, dict(), f'Expected and actual data are not equal')

        if os.path.exists(test_file):
            os.remove(test_file)
        sys.argv.pop(1)

    def test_add_item(self):
        phonebook_data = get_data_from_file(TestPhoneBook.__file_example)
        full_name = 'Full_name'
        phone_number = "123"
        city = 'City'
        TestPhoneBook.__phone_book.add_item(phonebook_data, full_name, phone_number, city)
        phonebook_data[full_name] = {'number': phone_number, 'city': city}
        phonebook_data2 = get_data_from_file(TestPhoneBook.__file_example)
        self.assertEqual(phonebook_data2, phonebook_data, f'Expected and actual data are not equal')

    def test_delete_item(self):
        phonebook_data = get_data_from_file(TestPhoneBook.__file_example)
        phone_number = '098765432'
        TestPhoneBook.__phone_book.delete_item(phonebook_data, phone_number)
        phonebook_data.pop("John Deer", None)
        self.assertEqual(phonebook_data, phonebook_data, f'Expected and actual data are not equal')

    def test_update_item(self):
        phonebook_data = get_data_from_file(TestPhoneBook.__file_example)
        full_name = 'Full_name2'
        phone_number = "1232"
        city = 'City2'
        TestPhoneBook.__phone_book.update_item(phonebook_data, full_name, full_name, phone_number, city)
        phonebook_data[full_name] = {'number': phone_number, 'city': city}
        phonebook_data2 = get_data_from_file(TestPhoneBook.__file_example)
        self.assertEqual(phonebook_data2, phonebook_data, f'Expected and actual data are not equal')

    def test_search_by_full_name(self):
        phonebook_data = get_data_from_file(TestPhoneBook.__file_example)
        full_name = 'Full_name2'
        actual_result = TestPhoneBook.__phone_book.search_by_full_name(phonebook_data, full_name)
        expected_result = phonebook_data.get(full_name, None)
        self.assertEqual(actual_result, expected_result, f'Expected and actual data are not equal')

    def test_search_by_phone_number(self):
        phonebook_data = get_data_from_file(TestPhoneBook.__file_example)
        phone_number = "098765432"
        full_name = 'John_Deer'
        self.assertEqual(TestPhoneBook.__phone_book.search_by_phone_number(phonebook_data, phone_number), full_name,
                         f'Expected and actual data are not equal')

    def test_search_by_city(self):
        phonebook_data = get_data_from_file(TestPhoneBook.__file_example)
        city = 'Los-Angeles'
        full_name = 'John_Deer'
        self.assertEqual(TestPhoneBook.__phone_book.search_by_city(phonebook_data, city), full_name,
                         f'Expected and actual data are not equal')

    def test_get_key_of_record_by_value(self):
        phonebook_data = get_data_from_file(TestPhoneBook.__file_example)
        city = 'City2'
        TestPhoneBook.__phone_book.get_key_of_record_by_value(phonebook_data, city, 'City2')

    def tearDown(self):
        write_data_to_file(dict(), TestPhoneBook.__file_example)


if __name__ == '__main__':
    unittest.main()
