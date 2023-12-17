# Solution based on code shared by Lafazar on ResetERA, though rewritten in my style
# in order to try and help me understand what the code is doing better.
#
# Original solution can be found at
# https://www.resetera.com/threads/advent-of-code-2023-ot-ruby-the-rust-nose-reindeer.788355/post-116440602
import heapq


def main(data):
    global max_x, max_y
    for x, line in enumerate(data):
        data[x] = [int(char) for char in line]
    max_x = len(data)
    max_y = len(data[0])
    print("The least heat loss that can occur is " +
          f"{find_warmest_path((0, 0), (max_x - 1, max_y - 1), data)}.")


def find_warmest_path(start, goal, heat_map):
    directions = (("up", -1, 0), ("down", 1, 0), ("left", 0, -1), ("right", 0, 1))
    opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
    least_heat_loss = {}
    to_do = [(0, start, 4, None)]
    while to_do:
        total_heat_loss, (x, y), consecutive_moves, last_direction = heapq.heappop((to_do))
        if (x, y) == goal and 4 <= consecutive_moves <= 10:
            return total_heat_loss
        for (direction, dx, dy) in directions:
            if last_direction != opposites[direction] \
                    and 0 <= x + dx < max_x \
                    and 0 <= y + dy < max_y:
                if direction != last_direction and 4 <= consecutive_moves <= 10 \
                        or direction == last_direction and consecutive_moves < 10:
                    if direction == last_direction:
                        consecutive_next = consecutive_moves + 1
                    else:
                        consecutive_next = 1
                    total_heat_loss_next = total_heat_loss + heat_map[x + dx][y + dy]
                    if least_heat_loss.get(
                            (x + dx, y + dy, consecutive_next, direction), float("inf")) > total_heat_loss_next:
                        least_heat_loss[(x + dx, y + dy, consecutive_next, direction)] = total_heat_loss_next
                        heapq.heappush(to_do, (total_heat_loss_next, (x + dx, y + dy), consecutive_next, direction))
