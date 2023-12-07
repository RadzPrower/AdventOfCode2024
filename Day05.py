from itertools import chain
import portion

def main(data):
    seeds = populate_lists(data)
    print("The lowest location number is " + str(min(seeds)) + ".")


def populate_lists(data):
    seed_changed = []
    ranges = []
    seeds = []
    for line in data:
        if "seeds: " in line:
            data = [int(i) for i in line.replace("seeds: ", "").split(" ")]
            for idx, entry in enumerate(data):
                if (idx % 2) == 0:
                    start = entry
                else:
                    span = entry - 1
                    ranges.append([start, start + span])
            intervals = [portion.closed(a, b) for a, b in ranges]
            seeds = list(portion.iterate(portion.Interval(*intervals), step=1))
            for seed in seeds:
                seed_changed.append(True)
        else:
            if line == "":
                for idx, seed in enumerate(seeds):
                    seed_changed[idx] = True
            elif line[0].isdigit():
                map_values = [int(i) for i in line.split(" ")]
                shift = map_values[1] - map_values[0]
                map_range = range(map_values[1], map_values[1] + map_values[2])
                for idx, seed in enumerate(seeds):
                    if seed in map_range and seed_changed[idx]:
                        seeds[idx] -= shift
                        seed_changed[idx] = False
    return seeds
