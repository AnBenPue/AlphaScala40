VALID_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
VALID_SUITS = [1, 2, 3, 4]


class Card:
    def __init__(self, number: int, suit: int):

        self.number = None
        self.suit = None

        if number in VALID_NUMBERS and suit in VALID_SUITS:
            self.number = number
            self.suit = suit

        if number == -1 and suit == -1:
            self.number = number
            self.suit = suit
