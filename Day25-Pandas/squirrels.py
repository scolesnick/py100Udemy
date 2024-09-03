import pandas

df = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

fur_colors = df.groupby('Primary Fur Color')['Primary Fur Color'].count()

fur_colors.to_csv('new_data.csv')