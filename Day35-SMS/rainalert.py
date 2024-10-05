import requests


MY_LAT = 30.332184
MY_LONG = -81.655647
# MY_LAT = 35.075500
# MY_LONG = -91.881752
APP_ID = ''

params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': APP_ID,
    'cnt': 4,
    'units': 'Imperial'
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()
data = response.json()

# print(response.status_code)
# print(data)

rain = False
for e in data['list']:
    if e['weather'][0]['id'] < 700:
        rain = True
        break
print(f'It will rain: {rain}')
