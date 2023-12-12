from itertools import combinations


def main(data):
    global spring_map
    spring_map = list(data)
    possible_arrangements = find_arrangements(spring_map)
    print(f"The sum of all possible arrangements is {sum(possible_arrangements)}.")


def find_arrangements(spring_map, folded=False):
    result = []
    if folded:
        expand_spring_map(spring_map)
    for line in spring_map:
        ind_result = 0
        individual, groups = line.split(" ")
        groups = [int(i) for i in groups.split(",")]
        group_count = len(groups)
        empty_count = len(individual) - sum(groups) - group_count + 1
        possibilities = combinations(range(group_count + empty_count), group_count)
        for p in possibilities:
            valid = True
            temp = ""
            idx = 0
            for index in range(group_count + empty_count):
                if idx < len(p) and index == p[idx]:
                    insert = "#" * groups[idx]
                    temp += insert
                    idx += 1
                    if idx < len(p):
                        temp += "."
                else:
                    temp += "."
            temp = temp + ("." * (len(individual) - len(temp)))
            temp_groups = [i for i in temp.split(".") if i]
            temp_lengths = []
            for group in temp_groups:
                temp_lengths.append(len(group))
            if groups != temp_lengths:
                continue
            for idx, char in enumerate(temp):
                if char != individual[idx] and individual[idx] != "?":
                    valid = False
            if valid:
                ind_result += 1
        result.append(ind_result)
    return result


def expand_spring_map(spring_map):
    for idx, line in enumerate(spring_map):
        springs, groups = line.split(" ")
        temp_springs = str(springs)
        temp_groups = str(groups)
        for i in range(4):
            temp_springs += "?" + springs
            temp_groups += "," + groups
        spring_map[idx] = temp_springs + " " + temp_groups
