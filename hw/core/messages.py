from enum import Enum


class PhoneBookMessages(Enum):
    MENU_MESSAGE = """
    For adding a new record please enter 'a'
    For searching a record please enter 's'
    For deleting a new record please enter 'd'
    For updating a record please enter 'u'
    For quiting please type 'stop'"""

    WELCOME_MESSAGE = """
        Welcome to Phone Book application
    {options_message}""".format(options_message=MENU_MESSAGE)

    PROVIDE_FILE = """
        Please provide as argument the name of phonebook or type 'stop' to quit 
        The phonebook has to be in the current folder"""

    OPTIONS_TO_SEARCH = """
    For searching by full name please enter 'sf'
    For searching by telephone number please enter 'sp'
    For searching by city please enter 'sc'
    For searching by type 'stop'"""
