def main(data):
     distance = calc_distance(data)
     print("The distance between the two lists is " + str(distance) + ".")
     similarity_score = calc_similarity_score(data)
     print("The similarity score of the two lists is " + str(similarity_score) + ".")


def calc_distance(data):
    left, right = parse_lists(data)
    # Sort the two respective lists from smallest to largest
    left.sort()
    right.sort()
    # Initialize the final distances list and then populate with the absolute values of the differences
    distances = []
    for idx,value in enumerate(left):
        distances.append(abs(left[idx] - right[idx]))
    return sum(distances)


def parse_lists(data):
    # Initialize lists for the left and right values
    left = []
    right = []
    # Take data and parse through one line at a time splitting it into the left and right values
    for line in data:
        line = line.split("   ")
        left.append(int(line[0]))
        right.append(int(line[1]))
    return left, right


def calc_similarity_score(data):
    left, right = parse_lists(data)
    # Initialize similarity scores list and then populate via multiplying left by occurrences in right
    similarity_scores = []
    for value in left:
        similarity_scores.append(value * right.count(value))
    return sum(similarity_scores)