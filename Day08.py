import itertools
import numpy as np
from Day06 import convert_data_to_grid


def main(data):
    antenna_grid = convert_data_to_grid(data)
    antinode_count = count_antinodes(antenna_grid)
    result = "There are " + str(antinode_count) + " antinode locations."
    return result


def count_antinodes(grid):
    frequencies = list(np.unique(grid))
    frequencies.remove(".")
    for frequency in frequencies:
        antenna_list = []
        antenna_coords = np.where(np.char.find(grid, frequency) != -1)
        for i in range(len(antenna_coords[0])):
            antenna_list.append([antenna_coords[0][i], antenna_coords[1][i]])
        antenna_pairs = list(itertools.combinations(antenna_list, 2))
        for pair in antenna_pairs:
            x_diff = pair[0][0] - pair[1][0]
            y_diff = pair[0][1] - pair[1][1]
            for antenna in pair:
                find_antinodes(antenna, frequency, grid, x_diff, y_diff, True)
                find_antinodes(antenna, frequency, grid, x_diff, y_diff, False)
    antinodes = np.where(np.char.find(grid, "#") != -1)
    return len(antinodes[0])


def find_antinodes(antenna, frequency, grid, x_diff, y_diff, addition):
    if addition:
        coord_x = antenna[0] + x_diff
        coord_y = antenna[1] + y_diff
    else:
        coord_x = antenna[0] - x_diff
        coord_y = antenna[1] - y_diff
    if (grid.shape[0] > coord_x >= 0 and
            grid.shape[1] > coord_y >= 0):
        if grid[coord_x, coord_y] == ".":
            grid[coord_x, coord_y] = "#"
        else:
            grid[coord_x, coord_y] += "#"
        find_antinodes([coord_x, coord_y], frequency, grid, x_diff, y_diff, addition)