import requests
from requests import Response

# For some reason the reddit blocks requests from PyCharm
# As workaround "say" the reddit that request is from browser
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}


def get_content(url: str) -> Response:
    print(f'Performing GET request to {url}')
    return requests.get(url, headers=headers)
