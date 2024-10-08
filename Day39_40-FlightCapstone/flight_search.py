import os
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ['AMADEUS_KEY']
        self._api_secret = os.environ['AMADEUS_SECRET']
        self._token = self.get_new_token()
        self._auth = {
            'Authorization':'Bearer ' + self._token['access_token']
        }
        self._amadeus_host = 'https://test.api.amadeus.com/v1'

    def get_flight_code(self, city_name):
        body = {
            'keyword':city_name
        }
        response = requests.get(url=f'{self._amadeus_host}/reference-data/locations/cities', headers=self._auth, params=body)
        # print(response.text)
        return response.json()['data'][0]['iataCode']

    def get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=f'{self._amadeus_host}/security/oauth2/token', headers=header, data=body)
        return response.json()

    def get_flight_offers(self, origin_code, destination_code):
        pass
        ''' 
            The goal was to search prices for round trip flights across the next six months.
            However, the API only allows you to search for prices with a defined start and endpoint.
            
            To achieve the original goal, we would exceed the API call limit.
            Some comments in the course from the TA have suggested that the instructor plans on removing this project.
            Since I cannot achieve the original goal I'd rather move on to the next project. 
        '''
        # offer_params = {
        #     'originLocationCode': origin_code,
        #     'destinationLocationCode': destination_code,
        #
        # }