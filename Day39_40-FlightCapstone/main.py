#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

dm = DataManager()
fs = FlightSearch()

data = dm.get_data()

for destination in data['prices']:
    code = fs.get_flight_code(destination['city'])
    destination['iataCode'] = code

dm.post_data(data)

