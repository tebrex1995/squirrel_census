import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240502.csv")

colors = data["Primary Fur Color"].to_list()
cinnamon_squirrels = []
gray_squirrels = []
black_squirrels = []
for color in colors:
    if color == "Cinnamon":
        cinnamon_squirrels.append(color)
    elif color == "Gray":
        gray_squirrels.append(color)
    elif color == "Black":
        black_squirrels.append(color)
    else:
        pass
cinnamon = len(cinnamon_squirrels)
gray = len(gray_squirrels)
black = len(black_squirrels)

colors_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

new_data = pd.DataFrame(colors_data)
new_data.to_csv("squirrel_count")
