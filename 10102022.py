import random

# set the cards
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 10,
}

playing = True

# Classes

# Create all the cards


class Card:
    # each card has two attributes: suit and rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # present the card as a string when it is created
    def __str__(self):
        return self.rank + " of " + self.suit


# Create the deck of cards


class Deck:
    def __init__(self):
        self.deck = [Card(s, r) for s in suits for r in ranks]

    def shuffle(self):
        random.shuffle(self.deck)  # shuffle the deck after it is created

    def draw(self):  # draw a card from the deck
        single_card = self.deck.pop()  # remove a card from the deck and return it
        return single_card


class Hand:  # dealer and player's hands
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # keep track of aces

    # Add a card to dealer and player's hand,
    # this card is the card drew from the deck (self.deck.pop())
    # Thus, the action completes (draw a card from the deck and put into someone's hand)
    def add_card(self, card):
        self.cards.append(card)

        # use [card.rank] as key to extract THE value from the dictinary
        # calling a method from `Card` class because it is a card
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1  # track the ace

    def adjust_for_ace(self):
        # If the total points are over 21 with aces in hand:
        while self.value > 21 and self.aces:
            # count one of the aces as 1 until the point is less than 21
            self.value -= 10
            self.aces -= 1


# Functions

# Gameplay
