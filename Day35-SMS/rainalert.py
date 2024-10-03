import requests


MY_LAT = 35.075500 # Your latitude
MY_LONG = -91.881752 # Your longitude
APP_ID = ''


params = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': APP_ID,
    'units': 'Imperial'
}


response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()
data = response.json()

print(response.status_code)
print(data)