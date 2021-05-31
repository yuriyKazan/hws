import json

from requests import Response


def order_data(response: Response) -> dict:
    data = get_dic_data(response)
    sorted_data = sort_dict_by_created_utc(data)
    return convert_to_dict(sorted_data)


def get_dic_data(response: Response) -> dict:
    return response.json()


def sort_dict_by_created_utc(unsorted_dic: dict) -> list:
    return sorted(unsorted_dic['data']['children'], key=lambda item: item['data']['created_utc'])


def convert_to_dict(list_data: list) -> dict:
    return {"comments": list_data}
