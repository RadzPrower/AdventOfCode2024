def main(data):
    blinks = 75
    final_sequence = memoized_calculate_sequence(data[0].split(), blinks)
    result = "The total number of stones after " + str(blinks) + " blinks is " + str(sum(final_sequence)) + "."
    return result


def calculate_sequence(sequence, blinks):
    for blink in range(blinks):
        for idx in reversed(range(len(sequence))):
            if sequence[idx] == "0": sequence[idx] = "1"
            elif len(sequence[idx]) % 2 == 0:
                midpoint = len(sequence[idx]) // 2
                value1 = int(sequence[idx][:midpoint])
                value2 = int(sequence[idx][midpoint:])
                sequence[idx] = str(value1)
                sequence.insert(idx + 1, str(value2))
            else: sequence[idx] = str(int(sequence[idx]) * 2024)
    return sequence


def memoized_calculate_sequence(stones, blinks):
    stones_count = {stone: stones.count(stone) for stone in stones}
    for i in range(blinks):
        new_stones_count = {}
        for stone, count in stones_count.items():
            for new_stone in determine_stones(stone):
                new_stones_count[new_stone] = new_stones_count.get(new_stone, 0) + count
        stones_count = new_stones_count
    return stones_count.values()


def determine_stones(stone):
    global cache
    if stone in cache:
        return cache[stone]
    if len(stone) % 2 == 0:
        midpoint = len(stone) // 2
        value1 = int(stone[:midpoint])
        value2 = int(stone[midpoint:])
        new_stones = (str(value1), str(value2))
    else:
        new_stones = (str(int(stone) * 2024),)
    cache[stone] = new_stones
    return new_stones


cache = {"0": ("1",)}