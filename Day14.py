def main(data):
    global tilted_map, map_history
    tilted_map = [list("".join(item)) for item in data]
    map_history = []
    match_pattern1 = []
    match_pattern2 = []
    cycles = 1000000000
    for i in range(cycles):
        cycle_map()
        if tilted_map in map_history:
            if tilted_map not in match_pattern1:
                match_pattern1.append(list(map(list, tilted_map)))
            elif tilted_map not in match_pattern2:
                match_pattern2.append(list(map(list, tilted_map)))
            else:
                tilted_map = pattern_extrapolation(match_pattern1, i, cycles)
                break
        else:
            map_history.append(list(map(list, tilted_map)))
            match_pattern1 = []
            match_pattern2 = []
    print(f"The total load on the north beam is {calculate_north_beam_load(tilted_map)}.")


def pattern_extrapolation(pattern, i, cycles):
    global map_history
    remaining_cycles = cycles - i - 1
    pattern_idx = remaining_cycles % len(pattern)
    return pattern[pattern_idx]


def calculate_north_beam_load(rock_map):
    result = 0
    for idx, line in enumerate(rock_map):
        result += line.count("O") * (len(rock_map) - idx)
    return result


def cycle_map():
    tilt_map_north()
    tilt_map_west()
    tilt_map_south()
    tilt_map_east()
    return


def tilt_map_north():
    global tilted_map
    rock_moved = False
    for x, line in enumerate(tilted_map):
        if x + 1 >= len(tilted_map):
            break
        for y, space in enumerate(line):
            if space == "." and tilted_map[x + 1][y] == "O":
                tilted_map[x][y] = "O"
                tilted_map[x + 1][y] = "."
                rock_moved = True
    if rock_moved:
        tilt_map_north()
    return True


def tilt_map_west():
    global tilted_map
    rock_moved = False
    for x, line in enumerate(tilted_map):
        for y in range(len(line) - 1):
            if tilted_map[x][y] == "." and tilted_map[x][y + 1] == "O":
                tilted_map[x][y] = "O"
                tilted_map[x][y + 1] = "."
                rock_moved = True
    if rock_moved:
        tilt_map_west()
    return True


def tilt_map_south():
    global tilted_map
    rock_moved = False
    for x, line in enumerate(reversed(tilted_map)):
        if x + 1 >= len(tilted_map):
            break
        reversed_x = len(tilted_map) - x - 1
        for y, space in enumerate(line):
            if space == "." and tilted_map[reversed_x - 1][y] == "O":
                tilted_map[reversed_x][y] = "O"
                tilted_map[reversed_x - 1][y] = "."
                rock_moved = True
    if rock_moved:
        tilt_map_south()
    return True


def tilt_map_east():
    global tilted_map
    rock_moved = False
    for x, line in enumerate(tilted_map):
        for y in reversed(range(1,len(line))):
            if tilted_map[x][y] == "." and tilted_map[x][y - 1] == "O":
                tilted_map[x][y] = "O"
                tilted_map[x][y - 1] = "."
                rock_moved = True
    if rock_moved:
        tilt_map_east()
    return True
