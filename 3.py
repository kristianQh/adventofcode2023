import re

with open("puzzleinput3.txt") as f:
    lines = [line.strip() for line in f.readlines()]

neighbor_idx = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

res = 0
gear_neighs = []
for i, line in enumerate(lines):
    for match in re.finditer(r"\d+", line):
        digit_idx = match.start(), match.end() - 1
        num = int(match.group())
        neighbors = [(i + ni, j + nj) for ni, nj in neighbor_idx for j in digit_idx]
        neighbors = set(neighbors)
        for ni, nj in neighbors:
            if 0 <= ni < len(lines) and 0 <= nj < len(lines[ni]): 
                ch = lines[ni][nj]

                if ch != "." and not ch.isdigit():
                    res += num

                if ch == "*":
                    ch_neighbors = {(ni + ni2, nj + nj2) for ni2, nj2 in neighbor_idx}
                    gear_neighs.append((num, ch_neighbors, {(i, j) for j in digit_idx}))

gear_pairs = []
for i, (num1, set1, id_set1) in enumerate(gear_neighs):
    for num2, set2, id_set2 in gear_neighs[i + 1:]:
        if set1 & id_set2:
            gear_pairs += [num1 * num2]

print(res)
print(sum(gear_pairs))