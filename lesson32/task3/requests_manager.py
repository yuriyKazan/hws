import json

import requests
from requests import Response


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
API_KEY = 'nR9p9RDStIDk4eFkTXXq4TtjnoDGjgYx'
location_api_endpoint = 'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={API_KEY}&q={city}'
current_weather_api_endpoint = 'http://dataservice.accuweather.com/currentconditions/v1/{locationKey}?apikey={API_KEY}'


def get_weather(city_name: str) -> list:
    location_key = get_location_key(city_name)
    return get_current_weather(location_key)


def get_current_weather(location_key: str) -> list:
    url = current_weather_api_endpoint.replace('{locationKey}', location_key).replace('{API_KEY}', API_KEY)
    raw_response = get_content(url)
    return json.loads(raw_response.text)


def get_location_key(city_name: str) -> str:
    url = location_api_endpoint.replace('{API_KEY}', API_KEY).replace('{city}', city_name)
    raw_response = get_content(url)
    return get_key_value(raw_response)


def get_key_value(content: Response) -> str:
    if content.text == '[]':
        print('Can not find provided city')
        exit(1)
    data = json.loads(content.text)
    return data[0]['Key']


def get_content(url: str) -> Response:
    return requests.get(url)
