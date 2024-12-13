import numpy as np


def main(data):
    result = "The total price of fencing is " + str(fencing_total(data)) + "."
    return result


def fencing_total(data):
    price = 0
    global visited
    visited = []
    global farm_map
    farm_map = convert_data_to_grid(data)
    for x in range(len(farm_map)):
        for y in range(len(farm_map[x])):
            if (x, y) not in visited:
                global region
                region = []
                global fences
                fences = 0
                region_id = farm_map[x, y]
                define_region(region_id, x, y)
                price += len(region) * fences
    return price


def define_region(region_id, x, y):
    global visited
    global farm_map
    global region
    global fences
    if 0 <= x < len(farm_map) and 0 <= y < len(farm_map[x]):
        if farm_map[x, y] == region_id:
            if (x, y) not in visited:
                visited.append((x, y))
                region.append((x, y))
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for x_direction, y_direction in directions:
                    define_region(region_id, x + x_direction, y + y_direction)
        else: fences += 1
    else: fences += 1
    return


def convert_data_to_grid(data):
    temp_array = []
    for line in data:
        array = [i for i in line]
        temp_array.append(array)
    return np.array(temp_array)


visited = []
farm_map = []
region = []
fences = 0