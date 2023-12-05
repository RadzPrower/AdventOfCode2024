from word2number import w2n


def main(data):
    digits = find_digits(data)

    print("The sum of the calibration digits is " + str(sum(digits)) + ".")
    return


def find_digits(data):
    first_digit = ""
    second_digit = ""
    digit_list = []
    name_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in data:
        first = True
        for idx, char in enumerate(line):
            for number in name_list:
                if line[idx:idx + len(number)] == number:
                    if first:
                        first_digit = w2n.word_to_num(number)
                        first = False
                    second_digit = w2n.word_to_num(number)
            if char.isdigit():
                if first:
                    first_digit = char
                    first = False
                second_digit = char
        combined_digit = str(first_digit) + str(second_digit)
        digit_list.append(int(combined_digit))
    return digit_list

