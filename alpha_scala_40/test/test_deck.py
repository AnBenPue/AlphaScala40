from alpha_scala_40.card_deck import FullCardDeck


def test_initialize_full_card_deck():

    new_deck = FullCardDeck()

    for card in new_deck.cards:
        assert card.number is not None, "The number is invalid"
        assert card.suit is not None, "The suit is invalid"

    assert len(new_deck.cards) is 54, "The deck is incomplete"


def test_merge_of_two_full_card_deck():
    deck_1 = FullCardDeck()
    deck_2 = FullCardDeck()
    deck_1.merge(deck_2)

    for card in deck_1.cards:
        assert card.number is not None, "The number is invalid"
        assert card.suit is not None, "The suit is invalid"

    assert len(deck_1.cards) is 108, "The deck is incomplete"
