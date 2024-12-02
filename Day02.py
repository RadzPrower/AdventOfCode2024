import copy

def main(data):
    safe_reports = determine_safe_reports(data)
    print("There are " + str(safe_reports) + " safe reports.")
    dampened_safe_reports = determine_safe_reports(data, True)
    print("With the Problem Dampener, there are " + str(dampened_safe_reports) + " safe reports.")


def determine_safe_reports(data, dampened: bool = False):
    safe_reports = 0
    for line in data:
        report = [int(x) for x in line.split(" ")]
        safe = compare_values(report)
        # If not initially safe, brute force check for a safe report if one value is removed
        if not safe and dampened:
            for i in range(len(report)):
                new_report = copy.copy(report)
                del new_report[i]
                safe = compare_values(new_report)
                if safe: break
        if safe: safe_reports += 1
    return safe_reports


# Compare the values of the reports to ensure they respect the report direction and no duplicates
def compare_values(report):
    safe = True
    ascending = determine_direction(report)
    for i in range(1, len(report)):
        difference = report[i - 1] - report[i]
        match difference:
            case -3:
                if not ascending: safe = False
            case -2:
                if not ascending: safe = False
            case -1:
                if not ascending: safe = False
            case 0:
                safe = False
            case 1:
                if ascending: safe = False
            case 2:
                if ascending: safe = False
            case 3:
                if ascending: safe = False
            case _:
                safe = False
        if not safe: break
    return safe


# Determine the direction of the report. It is quick and easy if they are pre-sorted but otherwise is determined
# by determining if more pairs are ascending or descending
def determine_direction(report):
    if report == sorted(report): return True
    elif report == sorted(report, reverse = True): return False
    else:
        ascending = 0
        descending = 0
        for i in range(1, len(report)):
            difference = report[i] - report[i - 1]
            if difference > 0: ascending += 1
            elif difference < 0: descending += 1
        if ascending > descending: return True
        else: return False