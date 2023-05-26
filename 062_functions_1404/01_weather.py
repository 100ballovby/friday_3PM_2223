import requests as r


def get_weather(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    query = {
        'appid': '',
        'units': 'metric',
        'lang': 'ru',
        'q': city,
    }
    response = r.get(url, params=query)  # подключаюсь к API и передаю параметры запроса
    resp_json = response.json()  # трансформируем ответ сервера в словарь
    print(response.url)

    print(f'Сегодня в городе {city}: {resp_json["weather"][0]["description"]}')
    print(f'Температура: {resp_json["main"]["temp"]}\nОщущается как {resp_json["main"]["feels_like"]}\nДавление {resp_json["main"]["pressure"]} мм р.ст.')


cities = ['минск', 'санкт-петербург', 'берлин', 'рим', 'токио', 'париж', 'варшава', 'сидней']
for c in cities:
    get_weather(c)
    print()

city = input('введи город: ')
get_weather(city)