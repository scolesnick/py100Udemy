import requests
import sys
import datetime

APP_ID = sys.argv[1]
API_KEY = sys.argv[2]
HOST = 'https://trackapi.nutritionix.com'
SHEETY_URL = sys.argv[3]
SHEETY_KEY = sys.argv[4]

sheety_header = {
    'Authorization':f'Bearer {SHEETY_KEY}'
}

headers = {
    'x-app-id':APP_ID,
    'x-app-key':API_KEY
}

# test getting exercise stats
post_endpoint = f'{HOST}/v2/natural/exercise'

exercise = input('Tell me which exercises you did: ')
# exercise = 'I ran for 20 minutes and walked for 2Km.'
post_params = {
    'query': exercise
}

response = requests.post(url=post_endpoint, data=post_params, headers=headers)
print(response.json())

# For each exercise listed collect the Exercise Name, Duration, Calories Burned, along with the Date and Time
names = [e['name'][0].upper() + e['name'][1:] for e in response.json()['exercises']]
durations = [e['duration_min'] for e in response.json()['exercises']]
cals = [e['nf_calories'] for e in response.json()['exercises']]
today = datetime.datetime.now()
date = today.strftime('%d/%m/%Y')
# now_time = today.time().strftime('%H:%M:%S')
now_time = today.strftime('%X')

# Connect to Sheety and post the rows
for i in range(len(names)):
    entry = {
        'workout': {
            'date':date,
            'time':now_time,
            'exercise':names[i],
            'duration':durations[i],
            'calories':cals[i]
        }
    }
    response_sheety = requests.post(url=SHEETY_URL, json=entry, headers=sheety_header)
    print(response_sheety.text)