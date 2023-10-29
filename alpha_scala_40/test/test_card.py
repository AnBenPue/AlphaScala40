from alpha_scala_40.card import Card


def test_initialize_valid_card():

    test_cards = [[1, 3], [-1, -1], [2, 2], [11, 3]]
    for c in test_cards:
        new_card = Card(c[0], c[1])
        assert new_card.number is not None, "The number is invalid"
        assert new_card.suit is not None, "The suit is invalid"


def test_initialize_invalid_card():

    test_cards = [[1, 5], [-1, 2], [2, -1]]
    for c in test_cards:
        new_card = Card(c[0], c[1])
        assert new_card.number is None, "The number is valid"
        assert new_card.suit is None, "The suit is valid"
