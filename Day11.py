def main(data):
    global galactic_map, expanded_map, expanding_rows, expanding_cols
    galactic_map = data
    expand_map()
    galaxies = create_galaxies()
    print(f"The sum of the lengths between each galaxy is {sum_of_galactic_distances(galaxies, 1000000)}.")


class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

    def calc_distance(self, galaxy):
        x_distance = abs(self.x - galaxy.x)
        y_distance = abs(self.y - galaxy.y)

        return x_distance + y_distance


def create_galaxies():
    list_of_galaxies = []
    for x, line in enumerate(galactic_map):
        for y, char in enumerate(line):
            if char == "#":
                list_of_galaxies.append(Galaxy(x, y))
    return list_of_galaxies


def sum_of_galactic_distances(galaxies, factor=2):
    galactic_pairs = find_all_galactic_pairs(galaxies)
    return calc_larger_distances(galactic_pairs, factor)


def calc_larger_distances(pairs, factor):
    result = 0
    for pair in pairs:
        larger_x, smaller_x = compare_x(pair)
        larger_y, smaller_y = compare_y(pair)
        temp = 0
        for x in range(smaller_x, larger_x):
            if x in expanding_rows:
                temp += factor
            else:
                temp += 1
        for y in range(smaller_y, larger_y):
            if y in expanding_cols:
                temp += factor
            else:
                temp += 1
        result += temp
    return result


def compare_x(pair):
    if pair[0].x >= pair[1].x:
        return pair[0].x, pair[1].x
    else:
        return pair[1].x, pair[0].x


def compare_y(pair):
    if pair[0].y >= pair[1].y:
        return pair[0].y, pair[1].y
    else:
        return pair[1].y, pair[0].y


def find_all_galactic_pairs(galaxies):
    galactic_pairs = []
    length = len(galaxies)
    for i in range(length):
        for j in range(i + 1, length):
            galactic_pairs.append((galaxies[i], galaxies[j]))
    return galactic_pairs


def print_map(printed_map):
    print()
    for line in printed_map:
        for char in line:
            print(char, end="")
        print()


def expand_map():
    global expanding_rows, expanding_cols
    expanding_rows = find_expanding_rows()
    expanding_cols = find_expanding_columns()
    #expand_columns(expanding_cols)
    #expand_rows(expanding_rows)


def find_expanding_rows():
    expanding = []
    for x, row in reversed(list(enumerate(galactic_map))):
        if "#" not in row:
            expanding.append(x)
    return expanding


def find_expanding_columns():
    expanding = []
    for y in reversed(range(len(galactic_map[0]))):
        if not any(sub[y] == "#" for sub in galactic_map):
            expanding.append(y)
    return expanding


def expand_columns(list):
    global expanded_map
    for x, line in enumerate(expanded_map):
        for y in list:
            expanded_map[x] = expanded_map[x][:y] + "." + expanded_map[x][y:]


def expand_rows(list):
    global expanded_map
    insert = "." * len(expanded_map[0])
    for x in list:
        expanded_map.insert(x, insert)