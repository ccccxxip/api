import requests


def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    return response.json()


def display_weather(data):
    if data["cod"] != "404":
        main = data["main"]
        wind = data["wind"]
        weather_desc = data["weather"][0]["description"]

        print(f"температура: {main['temp']}°C")
        print(f"давление: {main['pressure']} гПа")
        print(f"влажность: {main['humidity']}%")
        print(f"скорость ветра: {wind['speed']} м/с")
        print(f"описание: {weather_desc.capitalize()}")
    else:
        print("город не найден")


def main():
    api_key = "5257bee177419b3fec7cecb460f0af14"
    city = input("введите название города: ")

    weather_data = get_weather(city, api_key)
    display_weather(weather_data)


if __name__ == "__main__":
    main()

