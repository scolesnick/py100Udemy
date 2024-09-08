from datetime import datetime, timezone
import requests
MY_LAT = 34.746483
MY_LONG = -92.289597

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# # print(response)
# data = response.json()
# print(data)

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

sunrise = datetime.fromisoformat(data['results']['sunrise'])
sunset = datetime.fromisoformat(data['results']['sunset'])



print(f'sunrise: {sunrise.time()}')
print(f'sunset: {sunset.time()}')
print(f'time now: {datetime.now(tz=timezone.utc).time()}')