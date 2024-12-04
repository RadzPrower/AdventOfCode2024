def main(data):
    global grid, x_length, y_length
    grid = data
    x_length = len(grid)
    y_length = len(grid[0])
    count, count_x = search_grid()
    result = "The total number of \"XMAS\" found is " + str(count) + "."
    result += "\nThe total number of \"X-MAS\" found is " + str(count_x) + "."
    return result


def search_grid():
    count = 0
    count_x = 0
    for x,row in enumerate(grid):
        for y,value in enumerate(row):
            match value:
                case "X":
                    if check_up_diagonal_left(x, y): count += 1
                    if check_up(x, y): count +=1
                    if check_up_diagonal_right(x, y): count += 1
                    if check_left(x, y): count += 1
                    if check_right(x, y): count += 1
                    if check_down_diagonal_left(x, y): count += 1
                    if check_down(x, y): count += 1
                    if check_down_diagonal_right(x, y): count += 1
                case "A":
                    if check_x(x, y): count_x += 1
    return count, count_x


def check_up_diagonal_left(x, y):
    for letter in "XMAS":
        if grid[x][y] is not letter: return False
        x -= 1
        y -= 1
        if letter != "S" and check_outside_grid(x, y): return False
    return True


def check_up(x, y):
    for letter in "XMAS":
        if grid[x][y] is not letter: return False
        x -= 1
        if letter != "S" and check_outside_grid(x, y): return False
    return True


def check_up_diagonal_right(x, y):
    for letter in "XMAS":
        if grid[x][y] is not letter: return False
        x -= 1
        y += 1
        if letter != "S" and check_outside_grid(x, y): return False
    return True


def check_left(x, y):
    for letter in "XMAS":
        if grid[x][y] is not letter: return False
        y -= 1
        if letter != "S" and check_outside_grid(x, y): return False
    return True


def check_right(x, y):
    for letter in "XMAS":
        if grid[x][y] is not letter: return False
        y += 1
        if letter != "S" and check_outside_grid(x, y): return False
    return True


def check_down_diagonal_left(x, y):
    for letter in "XMAS":
        if grid[x][y] is not letter: return False
        x += 1
        y -= 1
        if letter != "S" and check_outside_grid(x, y): return False
    return True


def check_down(x, y):
    for letter in "XMAS":
        if grid[x][y] is not letter: return False
        x += 1
        if letter != "S" and check_outside_grid(x, y): return False
    return True


def check_down_diagonal_right(x, y):
    for letter in "XMAS":
        if grid[x][y] is not letter: return False
        x += 1
        y += 1
        if letter != "S" and check_outside_grid(x, y): return False
    return True


def check_x(x, y):
    if x == 0 or x >= x_length - 1: return False
    if y == 0 or y >= y_length - 1: return False
    cross_1 = [grid[x - 1][y - 1], grid[x + 1][y + 1]]
    cross_2 = [grid[x + 1][y - 1], grid[x - 1][y + 1]]
    if "M" in cross_1 and "S" in cross_1 and "M" in cross_2 and "S" in cross_2: return True
    return False


def check_outside_grid(x, y):
    if x < 0 or x >= x_length: return True
    if y < 0 or y >= y_length: return True
    return False