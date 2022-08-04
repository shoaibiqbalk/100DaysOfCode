# # with open("weather_data.csv") as data:
# #     lines = data.readlines()
# # print(lines)
#
# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if 'temp' not in row:
# #             temperatures.append(int(row[1]))
# #         # print(row)
# #
# #     print(temperatures)
# #
#
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# Avg = data["temp"].mean()
# print(Avg)
#
# Max = data["temp"].max()
# print(Max)
#
# # Get Data from Row
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday)
#
# temp_in_fahrenheit = (monday.temp * 9/5) + 32
# print(temp_in_fahrenheit)


# Central Park Squirrel Data Analysis
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

