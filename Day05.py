def main(data):
    good_result, bad_result = check_page_order(data)
    result = "The sum of the middle pages of correctly-ordered updates is " + str(good_result) + "."
    result += "\nThe sum of the middle pages of the corrected updates is " + str(bad_result) + "."
    return result


def check_page_order(data):
    rules, pages = parse_data(data)
    good_result, bad_result = check_pages(rules, pages)
    return good_result, bad_result


def parse_data(data):
    rules = []
    pages = []
    switch = False
    for line in data:
        if line == "": switch = True
        elif not switch: rules.append(line.split("|"))
        else: pages.append(line.split(","))
    return rules, pages


def check_pages(rules, pages):
    good_result = 0
    bad_result = 0
    bad_pages = []
    for set in pages:
        for rule in rules:
            if rule[0] in set and rule[1] in set:
                if set.index(rule[0]) > set.index(rule[1]):
                    bad_pages.append(set)
                    break
    good_pages = [x for x in pages if x not in bad_pages]
    for set in good_pages:
        middle_index = len(set)//2
        good_result += int(set[middle_index])
    for set in bad_pages:
        change_count = 99999
        while change_count > 0:
            change_count = 0
            for rule in rules:
                if rule[0] in set and rule[1] in set:
                    index0 = set.index(rule[0])
                    index1 = set.index(rule[1])
                    if index0 > index1:
                        set[index0], set[index1] = set[index1], set[index0]
                        change_count += 1
        middle_index = len(set)//2
        bad_result += int(set[middle_index])
    return good_result, bad_result