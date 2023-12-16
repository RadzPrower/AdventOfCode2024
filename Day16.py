

def main(data):
    global energized_map, beam_map, blank_map
    beam_map = data
    print(f"The optimal configuration will energize {find_optimal_start()} tiles.")
    #print(f"The number of energized tiles in the default configuation is {count_energized()}.")


def find_optimal_start():
    result = 0
    for x, line in enumerate(beam_map):
        for y, tile in enumerate(line):
            if x <= 0:
                init_energized_map()
                beam_down(-1, y)
                result = higher_energy(count_energized(), result)
            if y <= 0:
                init_energized_map()
                beam_right(x, -1)
                result = higher_energy(count_energized(), result)
            if x >= len(beam_map) - 1:
                init_energized_map()
                beam_up(len(beam_map), y)
                result = higher_energy(count_energized() + 1, result)
            if y >= len(beam_map[x]) - 1:
                init_energized_map()
                beam_left(len(beam_map) - 1, y + 1)
                result = higher_energy(count_energized(), result)
    return result


def print_map():
    print()
    print(" ", end="")
    for i in range(len(beam_map[0])):
        print("-", end="")
    print()
    for x, line in enumerate(energized_map):
        print("|", end="")
        for y, tile in enumerate(line):
            if tile[0][0] in "\\/-|" and tile[0] != "":
                print(tile[0][0], end="")
            elif tile[1] > 1:
                print(tile[1], end="")
            else:
                print(tile[0][-1], end="")
        print("|")
    print(" ", end="")
    for i in range(len(beam_map[0])):
        print("-", end="")
    print()


def higher_energy(value1, value2):
    if value1 > value2:
        return value1
    return value2


def init_energized_map():
    global energized_map
    energized_map = []
    for x, line in enumerate(beam_map):
        energized_map.append([])
        for y, item in enumerate(line):
            energized_map[x].append(list([beam_map[x][y], 0]))


def count_energized():
    global energized_map
    result = 0
    for line in energized_map:
        for tile in line:
            if tile[1] > 0:
                result += 1
    return result


def beam_right(x, y):
    global energized_map
    while True:
        y += 1
        if y >= len(beam_map):
            return
        if ">" in energized_map[x][y][0]:
            return
        energized_map[x][y][1] += 1
        match beam_map[x][y]:
            case "\\":
                beam_down(x, y)
                return
            case "/":
                beam_up(x, y)
                return
            case "|":
                beam_up(x, y)
                beam_down(x, y)
                return
            case _:
                energized_map[x][y][0] += ">"


def beam_down(x, y):
    global energized_map
    while True:
        x += 1
        if x >= len(beam_map[0]):
            return
        if "v" in energized_map[x][y][0]:
            return
        energized_map[x][y][1] += 1
        match beam_map[x][y]:
            case "\\":
                beam_right(x, y)
                return
            case "/":
                beam_left(x, y)
                return
            case "-":
                beam_right(x, y)
                beam_left(x, y)
                return
            case _:
                energized_map[x][y][0] += "v"


def beam_left(x, y):
    global energized_map
    while True:
        y -= 1
        if y < 0:
            return
        if "<" in energized_map[x][y][0]:
            return
        energized_map[x][y][1] += 1
        match beam_map[x][y]:
            case "\\":
                beam_up(x, y)
                return
            case "/":
                beam_down(x, y)
                return
            case "|":
                beam_up(x, y)
                beam_down(x, y)
                return
            case _:
                energized_map[x][y][0] += "<"


def beam_up(x, y):
    global energized_map
    while True:
        x -= 1
        if x < 0:
            return
        if "^" in energized_map[x][y][0]:
            return
        energized_map[x][y][1] += 1
        match beam_map[x][y]:
            case "\\":
                beam_left(x, y)
                return
            case "/":
                beam_right(x, y)
                return
            case "-":
                beam_left(x, y)
                beam_right(x, y)
                return
            case _:
                energized_map[x][y][0] += "^"
