# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for i, row in enumerate(data):
#         if i > 0:
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average_temp = sum(temp_list)/len(temp_list)
print(average_temp)

pandas_avg_temp = data["temp"].mean()
print(pandas_avg_temp)

max_temp = data["temp"].max()
print(max_temp)

print(data["condition"])
print(data.condition)

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(type(monday))
print(monday)


def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


print(monday.temp.apply(celsius_to_fahrenheit))
print(monday)

# Create Dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [75, 56, 65]
}
scores = pandas.DataFrame(data_dict)
print(scores)
scores.to_csv("scores.csv")

