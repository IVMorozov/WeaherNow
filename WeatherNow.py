def get_weather(city: str, API_key: str) -> dict:
    """
    Функция запроса погоды 
        - city: str: Название города для получения прогноза погоды.
        - api_key: str: Ключ API для доступа к сервису.
        - return: Словарь с данными о погоде.
        (используется библиотека `requests` !!!)
    """
    import requests
    # from plyer import notification
    units = "metric"
    language  = "ru"

    url = fr'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units={units}&lang={language}'

    response = requests.get(url)
    print(response.status_code)
    return response.json()