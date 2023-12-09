def main(incoming):
    global data
    data = incoming
    sum_of_new = 0
    sum_of_old = 0
    extrapolated_values = extrapolate_values()
    for value in extrapolated_values:
        sum_of_old += value[1]
        sum_of_new += value[0]
    print(f"The sum of the extrapolated new values is {sum_of_new}.")
    print(f"The sum of the extrapolated old values is {sum_of_old}.")


def extrapolate_values():
    new_values = []
    for line in data:
        new_values.append(extrapolate_single([int(i) for i in line.split()]))
    return new_values


def extrapolate_single(sequence):
    diff_array = find_diff(sequence)
    return calculate_value(diff_array)

def find_diff(sequence):
    diff_array = []
    new_sequence = []
    diff_array.append(sequence)
    if len(set(sequence)) == 1:
        diff_array.extend([[0] * (len(sequence) - 1)])
        return diff_array
    for x in range(len(sequence) - 1):
        new_sequence.append(sequence[x + 1] - sequence[x])
    diff_array.extend(find_diff(new_sequence))
    return diff_array


def calculate_value(diff_array):
    for idx in range(len(diff_array) - 1, 0, -1):
        diff_array[idx - 1].append(diff_array[idx - 1][-1] + diff_array[idx][-1])
        diff_array[idx - 1].insert(0, diff_array[idx - 1][0] - diff_array[idx][0])
    return diff_array[0][-1], diff_array[0][0]