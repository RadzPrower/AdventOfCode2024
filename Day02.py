import sys


def main(data):
    game_id_sum, power_sum = part1(data)
    print("The sum of the IDs of the winning games is " + str(game_id_sum) + ".")
    print("The sum of the power of each game is " + str(power_sum) + ".")


def part1(data):
    game_id_sum = 0
    power_sum = 0
    max_red = 12
    max_green = 13
    max_blue = 14
    for idx, game in enumerate(data):
        impossible = False
        min_red = 0
        min_green = 0
        min_blue = 0
        game = game.split(": ")
        rounds = game[1].split("; ")
        for round in rounds:
            colors = round.split(", ")
            for color in colors:
                if "red" in color:
                    count = int(color.split(" ")[0])
                    if count > min_red:
                        min_red = count
                    if count > max_red and not impossible:
                        impossible = True
                if "green" in color:
                    count = int(color.split(" ")[0])
                    if count > min_green:
                        min_green = count
                    if count > max_green and not impossible:
                        impossible = True
                if "blue" in color:
                    count = int(color.split(" ")[0])
                    if count > min_blue:
                        min_blue = count
                    if count > max_blue and not impossible:
                        impossible = True
        if not impossible:
            game_id_sum += idx + 1
        power_sum += min_blue * min_red * min_green
    return game_id_sum, power_sum
