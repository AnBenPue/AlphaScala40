from alpha_scala_40.card_deck import FullCardDeck


def test_initialize_full_card_deck():

    new_deck = FullCardDeck()

    for card in new_deck.cards:
        assert card.number is not None, "The number is invalid"
        assert card.suit is not None, "The suit is invalid"

    assert len(new_deck.cards) == 54, "The deck is incomplete"


def test_shuffle_card_deck():
    new_deck = FullCardDeck()

    old_order = new_deck.cards
    new_deck.shuffle()
    new_order = new_deck.cards

    for idx in range(3):
        assert old_order[idx] != new_order[
            idx], f"The deck wasn't shuffled: {new_order}"


test_shuffle_card_deck()


def test_merge_of_two_full_card_deck():
    deck_1 = FullCardDeck()
    deck_2 = FullCardDeck()
    deck_1.merge(deck_2)

    for card in deck_1.cards:
        assert card.number is not None, "The number is invalid"
        assert card.suit is not None, "The suit is invalid"

    assert len(deck_1.cards) == 108, "The deck is incomplete"
