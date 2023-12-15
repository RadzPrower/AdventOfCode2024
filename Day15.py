def main(data):
    print(f"The sum of the HASH results is {sum_of_hash(data)}")


def sum_of_hash(data):
    result = []
    for step in data[0].split(","):
        result.append(calc_full_hash(step))
    return sum(result)


def calc_full_hash(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def calc_label_hash(string):
    current_value = 0
    for char in string[0:1]:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value
