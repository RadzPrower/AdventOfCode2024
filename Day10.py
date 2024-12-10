import numpy as np


def main(data):
    hiking_map = convert_data_to_grid(data)
    peak_scores, trails_scores = find_trailhead_scores(hiking_map)
    result = "The sum of all trailhead peak scores is " + str(sum(peak_scores)) + "."
    result += "\nThe sum of all trailhead path scores is " + str(sum(trails_scores)) + "."
    return result


def find_trailhead_scores(hiking_map):
    peak_score = []
    trails_score = []
    trailheads = np.where(hiking_map == 0)
    x_coords = trailheads[0]
    y_coords = trailheads[1]
    for i in range(len(x_coords)):
        trailhead_peaks = find_trailhead_peaks(hiking_map, x_coords[i], y_coords[i])
        unique_peaks = []
        for peak in trailhead_peaks:
            if peak not in unique_peaks: unique_peaks.append(peak)
        peak_score.append(len(unique_peaks))
        trails_score.append(len(trailhead_peaks))
    return peak_score, trails_score


def find_trailhead_peaks(hiking_map, x, y):
    trailheads = []
    results1 = []
    results2 = []
    results3 = []
    results4 = []
    if hiking_map[x, y] == 9:
        return [x, y]
    else:
        if in_grid(hiking_map, x + 1, y) and hiking_map[x + 1, y] == hiking_map[x, y] + 1:
            results1 = find_trailhead_peaks(hiking_map, x + 1, y)
        if in_grid(hiking_map, x - 1, y) and hiking_map[x - 1, y] == hiking_map[x, y] + 1:
            results2 = find_trailhead_peaks(hiking_map, x - 1, y)
        if in_grid(hiking_map, x, y + 1) and hiking_map[x, y + 1] == hiking_map[x, y] + 1:
            results3 = find_trailhead_peaks(hiking_map, x, y + 1)
        if in_grid(hiking_map, x, y - 1) and hiking_map[x, y - 1] == hiking_map[x, y] + 1:
            results4 = find_trailhead_peaks(hiking_map, x, y - 1)
    trailheads = format_trailheads(trailheads, results1)
    trailheads = format_trailheads(trailheads, results2)
    trailheads = format_trailheads(trailheads, results3)
    trailheads = format_trailheads(trailheads, results4)
    return trailheads


def format_trailheads(trailheads, results):
    if results:
        if type(results[0]) is list:
            trailheads.extend(results)
        else:
            trailheads.append(results)
    return trailheads


def in_grid(hiking_map, x, y):
    if 0 <= x < len(hiking_map[0]) and 0 <= y < len(hiking_map[0]): return True
    else: return False


def convert_data_to_grid(data):
    temp_array = []
    for line in data:
        array = [i for i in line]
        temp_array.append(array)
    return np.array(temp_array, dtype=np.dtype('i'))