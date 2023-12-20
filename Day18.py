from Day10 import find_outside, fill_space


def main(data):
    global tunnel_map
    print(f"The lagoon could hold {shoelace_theorem(data)} cubic meters of lava")
    #current = {"x": 300, "y": 300}
    #tunnel_map = init_map(current["x"] * 2, current["y"] * 2)
    #tunnel_map[current["x"]][current["y"]] = "#"
    #for line in data:
    #    direction, distance, color = line.split(" ")
    #    current = dig_tunnel(current, direction, int(distance))
    #tunnel_map = find_outside(tunnel_map)
    #print(f"The hole could hold {count_interior(tunnel_map)} cubic meters of lava.")


def shoelace_theorem(data):
    x = 0
    y = 0
    vertices = [(0, 0)]
    directions = extract_hex(data)
    for line in directions:
        direction = int(line[-1])
        distance = int(line[0:-1], 16)
        match direction:
            case 0:
                x += distance
            case 1:
                y += distance
            case 2:
                x -= distance
            case 3:
                y -= distance
        if x != 0 or y != 0:
            vertices.append((x, y))
    left_side = sum_left(vertices)
    right_side = sum_right(vertices)
    return (left_side - right_side) // 2


def sum_left(vertices):
    sum = 0
    for x, vertex in enumerate(vertices):
        y = x + 1
        if y >= len(vertices):
            y = 0
        sum += vertices[x][0] * vertices[y][1]
    return sum


def sum_right(vertices):
    sum = 0
    for y, vertex in enumerate(vertices):
        x = y + 1
        if x >= len(vertices):
            x = 0
        sum += vertices[x][0] * vertices[y][1]
    return sum


def convert_hex_instructions(hex):
    return int(hex, 16),



def extract_hex(data):
    result = []
    for line in data:
        temp = line.split(" ")
        temp = temp[2].replace("(", "").replace(")","").replace("#", "")
        result.append(temp)
    return result


def init_map(x, y):
    return [[" " for i in range(y)] for j in range(x)]


def count_interior(map_data):
    result = 0
    for line in map_data:
        for tile in line:
            if tile != "O":
                result += 1
    return result


def dig_tunnel(start, direction, distance):
    global tunnel_map
    x = start["x"]
    y = start["y"]
    directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    for i in range(distance):
        delta = directions[direction]
        x += delta[0]
        y += delta[1]
        tunnel_map[x][y] = "#"
    return {"x": x, "y": y}


def find_outside(map_data):
    for x, line in enumerate(map_data):
        for y, char in enumerate(map_data[x]):
            if x != 0 and x != (len(map_data) - 1):
                if y != 0 and y != (len(map_data[x]) - 1):
                    continue
            if char == " ":
                fill_space(map_data, x, y)
    return map_data
