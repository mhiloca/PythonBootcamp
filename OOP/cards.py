import random as r


class Card:

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:

    def __init__(self):
        values = ['A', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        self.cards = [Card(value, suit) for value in values for suit in suits]

    def __repr__(self):
        return f'Deck of {self.count()} cards'

    def count(self):
        return len(self.cards)

    def _deal(self, n):
        count = self.count()
        actual = min(count, n)
        if count == 0:
            raise ValueError('All cards have been dealt')
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only full decks can be shuffled')
        return r.shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, n):
        return self._deal(n)


my_deck = Deck()
print(my_deck)
my_deck.shuffle()
card = my_deck.deal_card()
print(card)
hand = my_deck.deal_hand(5)
print(hand)
print(my_deck)
