import requests

# 1. Create a program that will ask user to search a word. Search this word in Giphy (use their API). Return links to these GIFs as a result
word = input('Enter some word: ')


def giphy_word(word):
    giphy_api = 'https://api.giphy.com/v1/gifs/search?api_key=fyDRJphyuWQ9jABOi7Qa8WHHBVzC5nbU&q=' + word + '&limit=1&offset=0&rating=g&lang=en'
    resp = requests.get(giphy_api)
    for obj in resp.json()['data']:
        return obj['images']['original']['url']


print(giphy_word(word))

# 2. Взяти API-weather, розпарсити і вивезти погоду від користувача (вводить локацію, по цій локації повернеться погода, вологість і тд)
# https://openweathermap.org *Потрібна реєстрація і створення свого api-ключа

location = input('Enter location (city name and country code, e.g. Kyiv, ua): ').split(',')


def current_weather_data(location):
    if len(location) < 2:
        return 'Bad input'
    city_name, country_code = [x.strip() for x in location]
    weather_api = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid=5de9f3fb4964c75555fd02bf141f069f&units=metric'
    resp = requests.get(weather_api)
    resp.status_code
    match resp.status_code:
        case 200:
            print('It\'s OK')
        case 429:
            return 'Try again'
        case 404:
            return 'Not found such city or country'
        case _:
            return resp.status_codeprint(resp.status_code)
    for obj in resp.json()['weather']:
        print(f"Weather condition: {obj['description']}")
    return (f"Temperature: {resp.json()['main']['temp']}°C\
        \nFeels like: {resp.json()['main']['feels_like']}°C\
        \nPressure: {resp.json()['main']['pressure']}hPa\
        \nHumidity: {resp.json()['main']['humidity']}%\
        \nVisibility: {resp.json()['visibility']}m\
        \nWind speed: {resp.json()['wind']['speed']}m/sec")


print(current_weather_data(location))

# 3. Вивезти всіх космонавтів (кількість і імена) http://api.open-notify.org/astros.json

resp = requests.get('http://api.open-notify.org/astros.json')

print(f"The number of astronauts in space: {len(resp.json()['people'])}")
for key in resp.json()['people']:
    print(key['name'])
