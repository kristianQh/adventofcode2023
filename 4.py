import re

example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
# 1 for the first match, then double
# In card 1 you have four winning numbers (48, 83, 17 and 86), a total of 8 points. (1,2,4,8)

with open("input") as f:
    lines = [line.strip() for line in f.readlines()]

total = 0
card_nums = [0] * len(lines)
for i, game in enumerate(lines):
    card_nums[i] += 1
    game = re.split("[:|]", game)
    w_numbers = set(map(int, game[1].split()))
    my_numbers = set(map(int, game[2].split()))
    wins = len(w_numbers & my_numbers)
    if wins > 0:
        total += 2 ** (wins -1)
    for j in range(wins):
        card_nums[i+j+1] += card_nums[i]

print(total)
print(sum(card_nums))