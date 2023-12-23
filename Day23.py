import pathfind
from functools import cache


visited = set()
path_map = []


def main(data):
    global path_map
    path_map = data
    graph = generate_graph(data)
    path = pathfind.find(graph, start="1,0", end=f"{len(data[0]) - 2},{len(data) - 1}", method="bfs")
    print(f"The longest possible path taken is {len(path) - 1}.")
    graph.show(trace=path)


def generate_graph(data):
    result = []
    for x, line in enumerate(data):
        data[x] = [str(i) for i in line]
    visited.add((1,0))
    conf = generate_conf((1, 0), (1, 1))
    return pathfind.Graph(conf)

@cache
def generate_conf(previous, current):
    global visited
    last_x, last_y = previous
    x, y = current
    if x >= len(path_map[0]) or y >= len(path_map) or x < 0 or y < 0:
        return
    visited.add(current)
    conf = []
    if last_x >= 0 and last_y >= 0:
        last_symbol = path_map[last_y][last_x]
    else:
        last_symbol = "#"
    if last_symbol == ".":
        weight = 0
        back_weight = 0
    else:
        weight = 0
        back_weight = 9999
    conf.append([f"{previous[0]},{previous[1]}", f"{current[0]},{current[1]}", weight, back_weight])
    while True:
        paths = count_paths(current)
        if len(paths) > 1:
            for path in paths:
                conf += generate_conf(current, path)
        elif paths:
            previous = current
            last_x, last_y = previous
            current = paths[0]
            x, y = current
            visited.add(current)
            if last_x >= 0 and last_y >= 0:
                last_symbol = path_map[last_y][last_x]
            else:
                last_symbol = "#"
            if last_symbol == ".":
                weight = 0
                back_weight = 0
            else:
                weight = 0
                back_weight = 9999
            conf.append([f"{previous[0]},{previous[1]}", f"{current[0]},{current[1]}", weight, back_weight])
        else:
            return conf


def count_paths(current):
    result = []
    x, y = current
    for direction in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        x_next = direction[0]
        y_next = direction[1]
        try:
            if (x_next, y_next) not in visited and path_map[y_next][x_next] != "#":
                result.append((x_next, y_next))
        except IndexError:
            continue
    return result
