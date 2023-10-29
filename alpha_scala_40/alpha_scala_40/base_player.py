class Player:
    def __init__(self, name):
        self.name = name

    def evaluate(self, game_state):
        # Method to evaluate the current game state
        # This method could assess the current state of the game and make decisions

        # Example placeholder - print the evaluation of the game state
        print(f"{self.name} is evaluating the game state")

    def pick(self, available_cards):
        # Method to pick a card from available options
        # This method could involve the player's strategy in choosing a card

        # Example placeholder - randomly choose a card (replace this with actual strategy)
        import random
        chosen_card = random.choice(available_cards)
        print(f"{self.name} picked card: {chosen_card}")

        return chosen_card  # Return the chosen card

    def discard(self, card):
        # Method to discard a card from the player's hand
        # This method could involve discarding a card based on certain rules/strategies

        # Example placeholder - just print the discarded card
        print(f"{self.name} discarded card: {card}")

        # Update player's hand or game state after discarding


# Usage example:
# Create a Player instance
player1 = Player("Alice")

# Example usage of the methods
player1.evaluate(game_state={})  # Example of evaluating the game state
# Example of picking a card
chosen_card = player1.pick(available_cards=["Card1", "Card2", "Card3"])
player1.discard(chosen_card)  # Example of discarding a card
