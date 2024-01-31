import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


color_data = data["Primary Fur Color"]

# data = pandas.read_csv("weather_data.csv")

colors = color_data.unique().tolist()

for c in colors:
    print(f"{c}: {color_data.where(color_data == c).count()}")