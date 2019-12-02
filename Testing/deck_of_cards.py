import random as r


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8",
                  "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f'Deck of {len(self.cards)} cards'

    def count(self):
        return len(self.cards)

    def reset(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8",
                  "9", "10", "J", "Q", "K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError('Only full decks can be shuffled')
        r.shuffle(self.cards)
        return self.cards

    def _deal(self, n):
        if self.count() == 0:
            raise ValueError('All cards have been dealt')
        actual = self.count()
        num = min(actual, n)
        hand = self.cards[-num:]
        self.cards = self.cards[:-num]
        return hand

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, n):
        return self._deal(n)
