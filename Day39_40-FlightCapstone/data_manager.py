import os
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._sheety_host = os.environ['SHEETY_HOST']
        self._sheety_key = os.environ['SHEETY_KEY']
        self._auth = {
            'Authorization':self._sheety_key
        }
        self.data = {}

    def get_data(self):
        response = requests.get(url=self._sheety_host, headers=self._auth)
        self.data = response.json()
        return self.data

    def post_data(self, data):
        self.data = data
        for row in data['prices']:
            new_data = {
                'price':{
                    'iataCode':row['iataCode']
                }
            }
            row_id = row['id']
            response = requests.put(url=f'{self._sheety_host}/{row_id}', json=new_data, headers=self._auth)
            # print(response.text)