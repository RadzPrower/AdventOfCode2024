import numpy
import copy


def main(data):
    grid = convert_data_to_grid(data)
    positions_visited, potential_obstructions = parse_guard_path(grid)
    result = "The guard will visit " + str(positions_visited) + " unique points."
    result += "\nThere are " + str(potential_obstructions) + " potential obstruction placements."
    return result


def parse_guard_path(grid):
    loop_count = 0
    start = numpy.where(grid == "^")
    x = start[0][0]
    y = start[1][0]
    x_start = copy.copy(x)
    y_start = copy.copy(y)
    grid_copy = copy.copy(grid)
    direction = "up"
    grid[x, y] = "."
    while 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]:
        if direction == "up":
            x, y, _ = move_up(grid, x, y)
            direction = "right"
        elif direction == "right":
            x, y, _ = move_right(grid, x, y)
            direction = "down"
        elif direction == "down":
            x, y, _ = move_down(grid, x, y)
            direction = "left"
        elif direction == "left":
            x, y, _ = move_left(grid, x, y)
            direction = "up"
    count = numpy.count_nonzero(grid == "X")
    route = numpy.where(grid == "X")
    for idx in range(route[0].shape[0]):
        x_coord = route[0][idx]
        y_coord = route[1][idx]
        x = copy.copy(x_start)
        y = copy.copy(y_start)
        if x == x_coord and y == y_coord: continue
        test_grid = copy.copy(grid_copy)
        test_grid[x_coord, y_coord] = "#"
        direction = "up"
        test_grid[x, y] = "."
        while 0 <= x < test_grid.shape[0] and 0 <= y < test_grid.shape[1]:
            loops = False
            if direction == "up":
                x, y, loops = move_up(test_grid, x, y, True)
                direction = "right"
            elif direction == "right":
                x, y, loops = move_right(test_grid, x, y, True)
                direction = "down"
            elif direction == "down":
                x, y, loops = move_down(test_grid, x, y, True)
                direction = "left"
            elif direction == "left":
                x, y, loops = move_left(test_grid, x, y, True)
                direction = "up"
            if loops:
                loop_count += 1
                break
    return count, loop_count


def convert_data_to_grid(data):
    temp_array = []
    for line in data:
        array = [i for i in line]
        temp_array.append(array)
    return numpy.array(temp_array, dtype=numpy.dtype("U20"))


def move_up(grid, x, y, trace = False):
    stopped = False
    loops = False
    while x >= 0 and not stopped:
        if "^" in grid[x, y] and not loops:
            loops = True
            break
        if not trace: grid[x, y] = "X"
        elif grid[x, y] == ".": grid[x, y] = "^"
        else: grid[x, y] += "^"
        if x > 0 and grid[x - 1, y] == "#": stopped = True
        else: x -= 1
    return x, y, loops


def move_right(grid, x, y, trace = False):
    stopped = False
    loops = False
    while y < grid.shape[0] and not stopped:
        if ">" in grid[x, y] and not loops:
            loops = True
            break
        if not trace: grid[x, y] = "X"
        elif grid[x, y] == ".": grid[x, y] = ">"
        else: grid[x, y] += ">"
        if y < grid.shape[0] - 1 and grid[x, y + 1] == "#": stopped = True
        else: y += 1
    return x, y, loops


def move_down(grid, x, y, trace = False):
    stopped = False
    loops = False
    while x < grid.shape[0] and not stopped:
        if "v" in grid[x, y] and not loops:
            loops = True
            break
        if not trace: grid[x, y] = "X"
        elif grid[x, y] == ".": grid[x, y] = "v"
        else: grid[x, y] += "v"
        if x < grid.shape[0] - 1 and grid[x + 1, y] == "#": stopped = True
        else: x += 1
    return x, y, loops


def move_left(grid, x, y, trace = False):
    stopped = False
    loops = False
    while y >= 0 and not stopped:
        if "<" in grid[x, y] and not loops:
            loops = True
            break
        if not trace: grid[x, y] = "X"
        elif grid[x, y] == ".": grid[x, y] = "<"
        else: grid[x, y] += "<"
        if y > 0 and grid[x, y - 1] == "#": stopped = True
        else: y -= 1
    return x, y, loops