import requests
from requests import Response


def get_content(url: str) -> Response:
    return requests.get(url)
