import re
import math

puzzleinput = open("puzzleinput2.txt").readlines()

res = 0
res2 = 0
for game in puzzleinput:
    color_bag = {"red": 0, "green": 0, "blue": 0}
    game = re.split('[:,;]', game)
    game_id = game[0][5:]
    for color in game[1:]:
        color_set = re.split('[\n ]', color)
        color_bag[color_set[2]] = max(int(color_set[1]), color_bag[color_set[2]])

    if color_bag["red"] <= 12 and color_bag["green"] <= 13 and color_bag["blue"] <= 14:
        res += int(game_id)
    res2 += math.prod(color_bag.values())

print(res)
print(res2)