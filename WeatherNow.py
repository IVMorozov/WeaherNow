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

def format_weather_message(weather_dict: dict) -> str:
    """
    Функция форматирования данных о погоде для читаемого вида
     - weather_dict: dict: Словарь с данными о погоде.
     - return: Форматированное сообщение о погоде.    
    """
    location = weather_dict['name']
    temp = weather_dict['main']['temp']
    feels_like = weather_dict['main']['feels_like']
    description = weather_dict['weather'][0]['description']
    return  f'Локация: {location}\nТемпература: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}'

def notify_weather(message: str) -> None:
    """
    Функция отправления уведомления пользователю с информацией о погоде
     - message: str: Сообщение о погоде для уведомления.
     - return: None.   
     (используется библиотека `plyer` !!!) 
    """
    from plyer import notification
    notification.notify(
        title="Погода",
        message=message,
        app_name="Погода",
        app_icon=None,
        timeout=10,
        toast=False,
    )

def main():
    """
    Запускает программу, выполняет вызовы функций запроса погоды, форматирования данных о погоде для читаемого вида и обрабатывает вывод.
     - return: None. 
    """
    weather_dict = get_weather(CITY, API_KEY)
    message = format_weather_message(weather_dict)
    notify_weather(message)