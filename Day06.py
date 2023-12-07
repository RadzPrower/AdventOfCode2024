def main(input):
    global data
    data = input
    print("If you multiply together the number of ways you can win each race, the result is "
           + str(multiply_wins()) + ".")
    print("The number of ways you can win the single, long race is " + str(single_win()) + ".")


def multiply_wins():
    final_result = 1;
    times = [int(i) for i in data[0].split()[1:]]
    distances = [int(i) for i in data[1].split()[1:]]
    for idx, time in enumerate(times):
        hold = 1
        result = 0
        win = False
        total_wins = 0
        while not win or result > distances[idx]:
            result = hold * (time - hold)
            if result > distances[idx]:
                win = True
                total_wins += 1
            hold += 1
        final_result *= total_wins
    return final_result


def single_win():
    time = int("".join(data[0].split()[1:]))
    distance = int("".join(data[1].split()[1:]))
    shortest_hold = shortest_win_hold(time, distance)
    longest_hold = longest_win_hold(time, distance)
    return longest_hold - shortest_hold + 1


def shortest_win_hold(time, distance):
    result = 0
    for hold in range(time):
        result = hold * (time - hold)
        if result > distance:
            return hold


def longest_win_hold(time, distance):
    result = 0
    for hold in reversed(range(time)):
        result = hold * (time - hold)
        if result > distance:
            return hold
