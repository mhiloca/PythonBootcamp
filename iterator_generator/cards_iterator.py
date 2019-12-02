from random import shuffle


class Cards:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:
    def __init__(self, num):
        self.num = num
        suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
        values = ['A', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Cards(value, suit) for value in values for suit in suits]

    def __repr__(self):
        return f'{self.num} deck(s) of {len(self.cards)} cards'

    def __iter__(self):
        return iter(self.cards)

    def reset(self):
        suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
        values = ['A', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Cards(value, suit) for value in values for suit in suits]
        return self.cards

    def count(self):
        return len(self.cards)

    def _deal(self, n):
        count = self.count()
        actual = min(count, n)
        if count == 0:
            raise ValueError('All cards have been dealt')
        card = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return card

    def shuffle(self):
        return shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, numb):
        return self._deal(numb)


my_deck = Deck(1)
print(my_deck)
my_deck.shuffle()
hand = my_deck.deal_hand(5)
print(hand)
print(my_deck)
my_deck.reset()
my_deck.shuffle()
print(my_deck)
for card in my_deck:
    print(card)

