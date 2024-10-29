import requests

def get_nasa_apod():
    api_key = "CPfpFgQvWkObzhm5hUmGyxkWAv5ivDhlxVE9OcMA"
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        image_url = data['url']
        description = data['explanation']
        print(f"Ссылка на фото: {image_url}")
        print(f"Описание: {description}")
    else:
        print("Не удалось получить данные.")

get_nasa_apod()

