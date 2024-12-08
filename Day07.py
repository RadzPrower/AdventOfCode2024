from itertools import combinations


def main(data):
    equations = parse_data(data)
    total_calibration = calculate_calibration(equations)
    print(total_calibration)
    result = "The total calibration result is " + str(total_calibration) + "."
    return result


def parse_data(data):
    equations = []
    for line in data:
        temp_split = line.split(": ")
        equations.append((int(temp_split[0]), list(map(int, temp_split[1].split()))))
    return equations


def calculate_calibration(equations):
    total = 0
    for equation in equations:
        if len(equation[1]) == 2:
            if (equation[1][0] * equation[1][1] == equation[0] or
                equation[1][0] + equation[1][1] == equation[0] or
                int(str(equation[1][0]) + str(equation[1][1])) == equation[0]):
                total += equation[0]
        else:
            possible_values = [ [] for _ in range(len(equation[1]) - 1)]
            possible_values[0].append(equation[1][0] + equation[1][1])
            possible_values[0].append(equation[1][0] * equation[1][1])
            possible_values[0].append(int(str(equation[1][0]) + str(equation[1][1])))
            for i in range(1, len(possible_values)):
                temp = []
                for value1 in possible_values[i - 1]:
                    value2 = equation[1][i + 1]
                    added = value1 + value2
                    multiplied = value1 * value2
                    concatenated = (int(str(value1) + str(equation[1][i + 1])))
                    if added <= equation[0]: temp.append(added)
                    if multiplied <= equation[0]: temp.append(multiplied)
                    if concatenated <= equation[0]: temp.append(concatenated)
                possible_values[i].extend(temp)
            if equation[0] in possible_values[-1]: total += equation[0]
    return total