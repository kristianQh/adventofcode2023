with open("input") as f:
    seeds, *maps = f.read().strip().split('\n\n')

seeds = list(map(int, seeds.split()[1:]))

final_seeds = []
for seed in seeds:
    for m in maps:
        for l in m.split('\n')[1:]:
            map_info = l.split()
            dest, source, r_length = map(int, map_info)
            if source <= seed < source + r_length:
                seed += dest - source
                break

    final_seeds.append(seed)

print(min(final_seeds))