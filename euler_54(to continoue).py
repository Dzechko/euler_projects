### To long to finish define each rank


numerical_cards = ['2', '3', '4', '5', '6', '7', '8', '9']
face_cards = ["J", "Q", "K", "A", "T"]
shapes = ["H", "C", "D", "S"]

player1 = []
player2 = []
with open("poker.txt", 'r') as file:
    for line in file:
        characters = line.split()
        player1.append(characters[:5])
        player2.append(characters[5:])

rank_values = {
    "Royal Flush": 10,
    "Straight Flush": 9,
    "Four of a Kind": 8,
    "Full House": 7,
    "Flush": 6,
    "Straight": 5,
    "Three of a Kind": 4,
    "Two Pairs": 3,
    "One Pair": 2,
    "High Card": 1
}


def is_royal_flush(hand):
    first_part = [hand[k][0] for k in range(5)]
    if all(element in face_cards for element in first_part):
        return True


def is_full_house(hand):
    first_part = [hand[k][0] for k in range(5)]
    count_values = []
    counts = 0
    for j in range(len(numerical_cards)):
        if numerical_cards[j] in first_part:
            counts += 1


is_full_house(['8C', '8S', '4C', '4H', '4S'])
