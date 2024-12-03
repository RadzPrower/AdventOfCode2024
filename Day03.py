import re

def main(data):
    result1 = parse_corrupted_data(data)
    result = "The result of ALL multiply operations is " + str(result1) + "."
    result2 = parse_corrupted_data(data, True)
    result += "\nThe final result is " + str(result2) + "."
    return result


def parse_corrupted_data(data, enable: bool = False):
    result = 0
    active = True
    operations = []
    for line in data:
        operations.extend(re.findall("(?:mul\(\d+\,\d+\)|don't\(\)|do\(\))", line))
    for operation in operations:
        if "mul" in operation and active:
            values = re.findall("\d+", operation)
            result += int(values[0]) * int(values[1])
        elif operation == "don't()" and enable:
            active = False
        elif operation == "do()" and enable:
            active = True
    return result