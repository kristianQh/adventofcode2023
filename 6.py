
with open("input") as f:
    ts_t,ds_t = f.read().strip().split('\n')

ts = list(map(int, ts_t.split()[1:]))
ds = list(map(int, ds_t.split()[1:]))

res = 1
for t,d in zip(ts,ds):
    num_ways = 0
    for i, t in enumerate(range(t, -1,-1)):
        if t*i > d:
            num_ways += 1
    res *= num_ways
print(res)

# Apparently we can find the numbers between the two roots of the parabola: 
# y = -x**2 + t*x - d
# a = 1, b = t, c = -d
import math

t2 = int("".join(ts_t.split()[1:]))
d2 = int("".join(ds_t.split()[1:]))
num_ways2_b1 = math.floor((t2 + math.sqrt(t2**2 - 4*d2))/2)
num_ways2_b2 = math.ceil((t2 - math.sqrt(t2**2 - 4*d2))/2)
print(num_ways2_b1 - num_ways2_b2+1)
