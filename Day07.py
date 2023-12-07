from functools import cmp_to_key


def main(input):
    data = []
    for idx, x in enumerate(input):
        data.append(x.split(" "))
    ranked_list = sorted(data, key=cmp_to_key(compare_hands))
    total_winnings = calculate_winnings(ranked_list)
    print("Your total winnings are $" + str(total_winnings) + "!")


def calculate_winnings(data):
    result = 0
    for idx, rank in enumerate(data):
        result += int(rank[1]) * (idx +1)
    return result


def compare_hands(item1, item2):
    hand1 = hand(item1[0])
    hand2 = hand(item2[0])
    if hand1 == hand2:
        for idx, i in enumerate(item1[0]):
            card_comparison = compare_cards(item1[0][idx], item2[0][idx])
            if card_comparison != 0:
                return card_comparison
    return hand1 - hand2


def compare_cards(card1, card2):
    card1 = convert_card(card1)
    card2 = convert_card(card2)
    return card1 - card2


def convert_card(card):
    match card:
        case "T":
            return 10
        case "J":
            return 1
        case "Q":
            return 11
        case "K":
            return 12
        case "A":
            return 13
        case _:
            return int(card)


# Find out the score of the hand from 0 (high card) to 6 (five of a kind)
def hand(input):
    unique_cards = set(input)
    unique_cards.discard("J")
    wildcards = input.count("J")
    match len(unique_cards):
        case 0:
            return 6
        case 1:
            return 6
        case 2:
            for card in unique_cards:
                count = input.count(card)
                if count == 1 or (count + wildcards) == 4:
                    return 5
                else:
                    return 4
        case 3:
            for card in unique_cards:
                count = input.count(card)
                if count == 3 or (count + wildcards) == 3:
                    return 3
            return 2
        case 4:
            return 1
        case 5:
            return 0

