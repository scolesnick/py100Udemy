#
# with open('weather_data.csv','r') as file:
#     data = file.readlines()

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv('weather_data.csv')
mean_temp = data['temp'].mean()
max_temp = data.temp.max()
max_temp_row = data[data.temp == max_temp]


monday_data = data[data.day == 'Monday']
mon_temp = monday_data.temp

print(mon_temp)
# Convert temp to f
print(mon_temp.mul(9/5.0).add(32))