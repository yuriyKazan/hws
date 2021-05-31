from json_manager import order_data
from file_manager import write_to_file
from requests_manager import get_content

URL = 'https://www.reddit.com/r/shrooms/comments.json'

if __name__ == '__main__':
    response = get_content(URL)
    if response.status_code != 200:
        raise RuntimeError(f'Impossible to proceed, response code is {response.status_code}, body:{response.text}')
    ordered_json = order_data(response)
    write_to_file(ordered_json)
