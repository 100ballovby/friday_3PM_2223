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
    print(f"Дата: {entry['dt_txt']}")
    print(f"Температура: {entry['main']['temp']}, ощущается как: {entry['main']['feels_like']}")
    print(f"Погода: {entry['weather'][0]['description']}")
    print(f"Скорость ветра: {entry['wind']['speed']}\n\n")


