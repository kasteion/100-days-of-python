import pandas

squirrel_census_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_series = squirrel_census_data["Primary Fur Color"]
distinct_colors = color_series.drop_duplicates()

print(squirrel_census_data[squirrel_census_data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].count())
print(len(squirrel_census_data[squirrel_census_data["Primary Fur Color"] == "Gray"]))

squirrel_color_dict = {
    "Fur Color": [],
    "Count": [],
}
for color in distinct_colors:
    count = color_series.where(color_series == color).count()
    if count > 0:
        squirrel_color_dict["Fur Color"].append(color)
        squirrel_color_dict["Count"].append(count)

squirrel_color_count_df = pandas.DataFrame(squirrel_color_dict)
squirrel_color_count_df.to_csv("squirrel_count.csv")


