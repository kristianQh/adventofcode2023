from collections import Counter
from functools import cmp_to_key

with open("input") as f:
    games = f.read().strip().split("\n")

cards = ["A", "K", "Q", "X", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def hand_strength(hand, p2):
    c = Counter(hand)
    if p2:
        c["J"] = 0
        if "J" in hand:
            handn = hand.replace("J", max(c, key=c.get))
            c = Counter(handn)
    else:
        hand = hand.replace("J", "X")
    vals = c.values()
    if 2 in vals and 3 in vals:
        return hand, 3.5
    if list(vals).count(2) == 2:
        return hand, 2.5
    else:
        return hand, max(c.values())

def compare_hands(hand1, hand2, p2):
    hand1 = hand1.split(" ")[0]
    hand2 = hand2.split(" ")[0]
    hand1, str1 = hand_strength(hand1, p2)
    hand2, str2 = hand_strength(hand2, p2)

    if str1 > str2:
        return -1
    elif str2 > str1:
        return 1
    else:
        for c1, c2 in zip(hand1, hand2):
            if cards.index(c1) < cards.index(c2):
                return -1
            elif cards.index(c2) < cards.index(c1):
                return 1

for p in [False, True]:
    sorted_games = sorted(games, key=cmp_to_key(lambda x, y: compare_hands(x, y, p)))
    print(sum(
        (len(games) - i) * int(g.split(" ")[1]) for i, g in enumerate(sorted_games)
    ))
