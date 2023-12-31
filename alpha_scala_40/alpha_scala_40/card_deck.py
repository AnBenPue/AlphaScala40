from alpha_scala_40.card import Card, VALID_NUMBERS, VALID_SUITS
from typing import List
from random import sample


class CardDeck:
    def __init__(self):
        self.cards = []

    def add(self, new_card: Card):
        self.cards.append(new_card)

    def remove(self, new_card: Card):
        self.cards.remove(new_card)

    def merge(self, deck):
        for card in deck.cards:
            self.cards.append(card)

    def shuffle(self):
        self.cards = sample(self.cards, len(self.cards))


class FullCardDeck(CardDeck):
    def __init__(self):
        self.cards = []

        for suit in VALID_SUITS:
            for number in VALID_NUMBERS:
                self.cards.append(Card(number, suit))

        self.cards.append(Card(-1, -1))
        self.cards.append(Card(-1, -1))


if __name__ == "__main__":

    deck_1 = FullCardDeck()
    deck_2 = FullCardDeck()

    deck_1.merge(deck_2)
