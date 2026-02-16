import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = []

for color in data["Primary Fur Color"]:
    if color not in colors and color != "nan":
        colors.append(color)

colors = colors[1:]

def count_color(color):
    color_count = len(data[data["Primary Fur Color"] == color])
    return color_count

final_data = []; 
squirrels_data = {"id":0,"color":"","count":0}

for color in colors:
    squirrels_data["id"] += 1
    squirrels_data["color"] = color
    squirrels_data["count"] = count_color(color)
    final_data.append(squirrels_data.copy())
       
for data in final_data:
    print(data)

try:
    df = pandas.DataFrame(final_data)
    df.to_csv("squirrels_count.csv", index=False)
except Exception as e:
    print("Error: ", e) 