import sys

from message import MESSAGE
from requests_manager import get_weather

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('The application consume one required parameter - a city name')
        exit(0)
    city_name = sys.argv[1]
    print(f'The city to determine the weather is: {city_name}')
    response = get_weather(city_name)[0]
    temp_metrics = response['Temperature']['Metric']
    message = MESSAGE.replace('{city}', city_name).replace('{time}', response['LocalObservationDateTime'])\
        .replace('{weather}', response['WeatherText']).replace('{temp_v}', str(temp_metrics['Value']))\
        .replace('{temp_m}', temp_metrics['Unit'])
    print(message)
