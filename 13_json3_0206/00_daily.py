import requests as r
import os
import json


def get_daily_forecast(city):
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {
        'appid': os.environ.get('OWM_KEY'),  # из виртуального окружения получить значение переменной OWM_KEY
        'q': city,
        'units': 'metric',
        'lang': 'ru',
    }
    response = r.get(url, params=params)

    with open(f'forecast_{city}.json', 'w') as file:
        file.write(json.dumps(response.json(), indent=4))  # dumps - преобразует строку в JSON
    return response.json()


minsk = get_daily_forecast('Minsk')
for entry in minsk['list']:
    print(entry['main']['temp'])
    print(entry['weather'][0]['description'])

