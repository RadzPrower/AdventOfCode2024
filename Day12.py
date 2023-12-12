from itertools import combinations
from functools import cache


def main(data):
    global spring_map
    spring_map = list(data)
    possible_arrangements = find_arrangements(spring_map, True)
    print(f"The sum of all possible arrangements is {sum(possible_arrangements)}.")


def find_arrangements(spring_map, folded=False):
    result = []
    if folded:
        expand_spring_map(spring_map)
        result = find_recursively(spring_map)
        return result
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
            for idx in range(0,len(temp),3):
                valid = string_compare(temp[idx:idx + 3], individual[idx:idx + 3])
                if not valid:
                    break
            #for idx, char in enumerate(temp):
            #    if char != individual[idx] and individual[idx] != "?":
            #        valid = False
            if valid:
                ind_result += 1
        result.append(ind_result)
    return result


def find_recursively(spring_map):
    result = []
    for line in spring_map:
        if line == "...?#??#?#????#..?...?#??#?#????#..?...?#??#?#????#..?...?#??#?#????#..?...?#??#?#????#.. 10,1,10,1,10,1,10,1,10,1":
            _ = 1
        springs, groups = line.split(" ")
        result.append(recurse(springs, groups))
    return result

@cache
def recurse(remaining_springs, groups):
    result = 0
    if not groups:
        return "#" not in remaining_springs
    groups_int = [int(i) for i in groups.split(",")]
    current_group = int(groups_int[0])
    groups = ",".join(groups.split(",")[1:])
    groups_int = groups_int[1:]
    for i in range(len(remaining_springs) - sum(groups_int) - len(groups_int) - current_group + 1):
        if "#" in remaining_springs[:i]:
            break
        if (nxt := i + current_group) <= len(remaining_springs) \
                and "." not in remaining_springs[i : nxt] \
                and remaining_springs[nxt : nxt + 1] != "#":
            result += recurse(remaining_springs[nxt + 1:], groups)
    return result


@cache
def string_compare(string1, string2):
    result = True
    for idx, char in enumerate(string1):
        result = character_compare(char, string2[idx])
        if result:
            break
    return not result


@cache
def character_compare(char1, char2):
    if char1 != char2 and char2 != "?":
        return True
    return False


def expand_spring_map(spring_map):
    for idx, line in enumerate(spring_map):
        springs, groups = line.split(" ")
        temp_springs = str(springs)
        temp_groups = str(groups)
        for i in range(4):
            temp_springs += "?" + springs
            temp_groups += "," + groups
        spring_map[idx] = temp_springs + " " + temp_groups
