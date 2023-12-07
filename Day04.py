def main(incoming):
    global data
    data = incoming
    points, cards = check_cards()
    print(f"The number of points awarded is {points}.")
    print(f"The number of total scratchcards is {cards}.")


def check_cards():
    total_points = 0
    card_counts = [1] * len(data)
    for idx, card in enumerate(data):
        points = 0
        temp = card.split("|")
        winners = temp[0].split()[2:]
        choices = temp[1].split()
        matches = [x for x in winners if x in choices]
        for i in range(len(matches)):
            card_counts[idx + i + 1] += 1 * card_counts[idx]
            if points > 0:
                points = points * 2
            else:
                points += 1
        total_points += points
    return total_points, sum(card_counts)
