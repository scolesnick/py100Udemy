import requests
import datetime

USERNAME = ''
TOKEN = ''
pixela_endpoint = 'https://pixe.la/v1/users'

# user_params = {
#     'token': TOKEN,
#     'username':USERNAME,
#     'agreeTermsOfService':'yes',
#     'notMinor':'yes'
# }
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
#
# graph_config = {
#     'id':'graph1',
#     'name':'Cycling Graph',
#     'unit':'Km',
#     'type':'float',
#     'color':'ajisai'
# }
#
headers = {
    'X-USER-TOKEN':TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.datetime.now()
# today = datetime.datetime(year=2024, month=10, day=3)
add_endpoint = f'{graph_endpoint}/graph1'
add_config = {
    'date':today.strftime('%Y%m%d'),
    'quantity':'5'
}
# Adding a pixel
# response = requests.post(url=add_endpoint, json=add_config, headers=headers)

put_endpoint = f'{add_endpoint}/'+add_config['date']
put_config = {
    'quantity':'7'
}
# Updating a pixel
# response = requests.put(url=put_endpoint, json=put_config, headers=headers)
# print(response.text)

# Deleting a pixel
delete_endpoint = put_endpoint
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)