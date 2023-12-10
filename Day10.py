def main(data):
    global map, start, loop, loop_map
    map = data
    start = find_start()
    loop = []
    find_loop_start()
    find_outside()
    loop_map = shrink_loop_map()
    print(f"The furthest number of steps from the start of the loop is {furthest_steps()}.")
    print(f"The number of tiles enclosed by the loop is {enclosed_tiles()}.")


def furthest_steps():
    return len(loop) // 2


def init_map():
    return [[" " for i in range(len(map[0]) * 2)] for j in range(len(map) * 2)]


def enclosed_tiles():
    global loop_map
    count = 0
    for line in loop_map:
        for char in line:
            if char == " ":
                count += 1
    return count


def print_map(map):
    print()
    for line in map:
        for char in line:
            print(char, end="")
        print()


def shrink_loop_map():
    global loop_map
    temp_map = [[" " for i in range(len(map[0]))] for j in range(len(map))]
    for x, line in enumerate(temp_map):
        for y, char in enumerate(line):
            temp_map[x][y] = loop_map[x * 2][y * 2]
    return temp_map



def find_outside():
    global loop_map
    for x, line in enumerate(loop_map):
        for y, char in enumerate(loop_map[x]):
            if x != 0 and x != (len(loop_map) - 1):
                if y != 0 and y != (len(loop_map[x]) - 1):
                    continue
            if char == " ":
                fill_space(loop_map, x, y)


def fill_space(matrix, x, y):
    fill_stack = []
    fill_stack.insert(0, [x, y])
    while fill_stack:
        [x, y] = fill_stack.pop()
        if not valid_coordinates(matrix, x, y):
            continue
        if matrix[x][y] != " ":
            continue
        matrix[x][y] = "O"

        fill_stack.insert(0, [x + 1, y])
        fill_stack.insert(0, [x - 1, y])
        fill_stack.insert(0, [x, y + 1])
        fill_stack.insert(0, [x, y - 1])


def valid_coordinates(matrix, x, y):
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[x])


def check_neighbors(x, y):
    global loop_map
    if (y + 1) < (len(loop_map[x]) - 1) and loop_map[x][y + 1] == " ":
        loop_map[x][y + 1] = "O"
        check_neighbors(x, y + 1)
    if (x + 1) < (len(loop_map) - 1) and loop_map[x + 1][y] == " ":
        loop_map[x + 1][y] = "O"
        check_neighbors(x + 1, y)
    if (y - 1) >= 0 and loop_map[x][y - 1] == " ":
        loop_map[x][y - 1] = "O"
        check_neighbors(x, y - 1)
    if (x - 1) >= 0 and loop_map[x - 1][y] == " ":
        loop_map[x - 1][y] = "O"
        check_neighbors(x - 1, y)


def find_start():
    for x, line in enumerate(map):
        if "S" in line:
            return x, line.find("S")


def find_loop_start():
    global loop, loop_map
    loop_map = init_map()
    loop.append((start[0], start[1]))
    loop_map[start[0] * 2][start[1] * 2] = "█"
    loop_map[(start[0] * 2) - 1][start[1] * 2] = "█"
    find_loop(start[0] - 1, start[1])
    if loop:
        return
    loop_map = init_map()
    loop.append((start[0], start[1]))
    loop_map[start[0] * 2][start[1] * 2] = "█"
    loop_map[start[0] * 2][(start[1] * 2) + 1] = "█"
    find_loop(start[0], start[1] + 1)
    if loop:
        return
    loop_map = init_map()
    loop.append((start[0], start[1]))
    loop_map[start[0] * 2][start[1] * 2] = "█"
    loop_map[(start[0] * 2) + 1][start[1] * 2] = "█"
    find_loop(start[0] + 1, start[1])
    if loop:
        return
    loop_map = init_map()
    loop.append((start[0], start[1]))
    loop_map[start[0] * 2][start[1] * 2] = "█"
    loop_map[start[0] * 2][(start[1] * 2) - 1] = "█"
    find_loop(start[0], start[1] - 1)


def find_loop(x, y):
    global loop, loop_map
    finished = False
    while not finished:
        match map[x][y]:
            case "|":
                if loop[-1] == (x - 1, y) or loop[-1] == (x + 1, y):
                    loop.append((x, y))
                    loop_map[2 * x][2 * y] = "█"
                    if loop[-2] == (x - 1, y):
                        x += 1
                        loop_map[(2 * x) - 1][2 * y] = "█"
                    else:
                        x -= 1
                        loop_map[(2 * x) + 1][2 * y] = "█"
                else:
                    loop = []
                    finished = True
            case "-":
                if loop[-1] == (x, y - 1) or loop[-1] == (x, y + 1):
                    loop.append((x, y))
                    loop_map[2 * x][2 * y] = "█"
                    if loop[-2] == (x, y - 1):
                        y += 1
                        loop_map[2 * x][(2 * y) - 1] = "█"
                    else:
                        y -= 1
                        loop_map[2 * x][(2 * y) + 1] = "█"
                else:
                    loop = []
                    finished = True
            case "L":
                if loop[-1] == (x - 1, y) or loop[-1] == (x, y + 1):
                    loop.append((x, y))
                    loop_map[2 * x][2 * y] = "█"
                    if loop[-2] == (x - 1, y):
                        y += 1
                        loop_map[2 * x][(2 * y) - 1] = "█"
                    else:
                        x -= 1
                        loop_map[(2 * x) + 1][2 * y] = "█"
                else:
                    loop = []
                    finished = True
            case "J":
                if loop[-1] == (x - 1, y) or loop[-1] == (x, y - 1):
                    loop.append((x, y))
                    loop_map[2 * x][2 * y] = "█"
                    if loop[-2] == (x - 1, y):
                        y -= 1
                        loop_map[2 * x][(2 * y) + 1] = "█"
                    else:
                        x -= 1
                        loop_map[(2 * x) + 1][2 * y] = "█"
                else:
                    loop = []
                    finished = True
            case "7":
                if loop[-1] == (x + 1, y) or loop[-1] == (x, y - 1):
                    loop.append((x, y))
                    loop_map[2 * x][2 * y] = "█"
                    if loop[-2] == (x + 1, y):
                        y -= 1
                        loop_map[2 * x][(2 * y) + 1] = "█"
                    else:
                        x += 1
                        loop_map[(2 * x) - 1][2 * y] = "█"
                else:
                    loop = []
                    finished = True
            case "F":
                if loop[-1] == (x + 1, y) or loop[-1] == (x, y + 1):
                    loop.append((x, y))
                    loop_map[2 * x][2 * y] = "█"
                    if loop[-2] == (x + 1, y):
                        y += 1
                        loop_map[2 * x][(2 * y) - 1] = "█"
                    else:
                        x += 1
                        loop_map[(2 * x) - 1][2 * y] = "█"
                else:
                    loop = []
                    finished = True
            case "S":
                finished = True
            case _:
                loop = []
                finished = True


def find_loop_recursive():
    move_north(start[0], start[1])
    if loop:
        return
    move_east(start[0], start[1])
    if loop:
        return
    move_south(start[0], start[1])
    if loop:
        return
    move_west(start[0], start[1])


def move_north(x, y):
    global loop
    loop.append((x, y))
    x -= 1
    match map[x][y]:
        case "S":
            return
        case "7":
            move_west(x, y)
        case "|":
            move_north(x, y)
        case "F":
            move_east(x, y)
        case _:
            loop = []
    return


def move_east(x, y):
    global loop
    loop.append((x, y))
    y += 1
    match map[x][y]:
        case "S":
            return
        case "J":
            move_north(x, y)
        case "-":
            move_east(x, y)
        case "7":
            move_south(x, y)
        case _:
            loop = []
    return


def move_south(x, y):
    global loop
    loop.append((x, y))
    x += 1
    match map[x][y]:
        case "S":
            return
        case "L":
            move_east(x, y)
        case "|":
            move_south(x, y)
        case "J":
            move_west(x, y)
        case _:
            loop = []
    return


def move_west(x, y):
    global loop
    loop.append((x, y))
    y -= 1
    match map[x][y]:
        case "S":
            return
        case "F":
            move_south(x, y)
        case "-":
            move_west(x, y)
        case "L":
            move_north(x, y)
        case _:
            loop = []
    return
