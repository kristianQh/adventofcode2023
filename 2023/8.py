from math import gcd
from functools import reduce

with open("input") as f:
    inst = f.readline().strip()
    nodes = [line.strip() for line in f if line.strip()]

inst = [0 if i == "L" else 1 for i in inst]

d = {}
for n in nodes:
    key, value = n.split("=")
    d[key.strip()] = tuple(value.strip(" ()").split(", "))

def steps(inst, d, node, end_char):
    i = 1
    num_steps = 1
    while not node.endswith(end_char):
        node = d[node][inst[i]]
        i = (i + 1) % len(inst)
        num_steps += 1
    return num_steps

# Part 1
print(steps(inst, d, d["AAA"][inst[0]], "Z"))

# Part 2
# Each path instructions and the node mappings forms one cycle. 
# Calculating the LCM of the lengths of these paths helps can be used in
# LCM to find the earliest step at which all our paths align
start_nodes = [n for n in d if n[2] == "A"]
num_steps_l = [steps(inst, d, d[sn][inst[0]], "Z") for sn in start_nodes]
print(reduce(lambda x, y: x * y // gcd(x, y), num_steps_l))
