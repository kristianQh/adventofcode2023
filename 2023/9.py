with open("input") as f:
    histories = [list(map(int, line.split())) for line in f]

def f(h):
    subs = list(map(lambda a, b: b - a, h[:-1], h[1:]))
    return h[-1] + f(subs) if len(h) != 0 else 0

print(sum(f(hist) for hist in histories))
print(sum(f(hist[::-1]) for hist in histories))
