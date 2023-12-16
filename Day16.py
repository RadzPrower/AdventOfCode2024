

def main(data):
    global energized_map, beam_map
    beam_map = data
    energized_map = [list([""] * len(data[0])) for _ in range(len(data))]
    beam_right(0, -1)
    print_map(energized_map)
    print(f"The number of energized tiles in the default configuation is {count_energized()}.")


def print_map(printed_map):
    print()
    for line in printed_map:
        for string in line:
            if len(string) > 1:
                print(len(string), end="")
            elif len(string) == 1:
                print(string, end="")
            else:
                print(" ", end="")
        print()


def count_energized():
    result = 0
    for line in energized_map:
        for tile in line:
            if tile:
                result += 1
    return result


def beam_right(x, y):
    global energized_map
    while True:
        y += 1
        if y >= len(beam_map):
            return
        if ">" in energized_map[x][y]:
            return
        energized_map[x][y] += ">"
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


def beam_down(x, y):
    global energized_map
    while True:
        x += 1
        if x >= len(beam_map[0]):
            return
        if "v" in energized_map[x][y]:
            return
        energized_map[x][y] += "v"
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


def beam_left(x, y):
    global energized_map
    while True:
        y -= 1
        if y < 0:
            return
        if "<" in energized_map[x][y]:
            return
        energized_map[x][y] += "<"
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


def beam_up(x, y):
    global energized_map
    while True:
        x -= 1
        if x < 0:
            return
        if "^" in energized_map[x][y]:
            return
        energized_map[x][y] += "^"
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
