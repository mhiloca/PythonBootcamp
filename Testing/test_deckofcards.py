import unittest
from deck_of_cards import Card, Deck


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("A", "Hearts")

    def test_init(self):
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")

    def tes_repr(self):
        self.assertEqual(repr(self.card), "A of Hearts")


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """all cards should be in a list"""
        self.assertEqual(type(self.deck.cards), list)
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        """should return the amount of cards in the deck"""
        self.assertEqual(repr(self.deck), f'Deck of 52 cards')

    def test_count(self):
        """count should return the amount of cards in the deck"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_reset(self):
        """reset should return a new full deck"""
        self.assertEqual(self.deck.reset(), self.test_init())

    def test_deal_sufficient_cards(self):
        """_deal should deal the number of cards specified"""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_insufficient_cards(self):
        """_deal should deal the number of cards left"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_shuffle(self):
        """should shuffle a full deck"""
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

    def testing_for_errors_shuffle(self):
        """Only full decks can be shuffled"""
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()

    def test_for_no_deal(self):
        """_deal should throw a ValueError if deck is empty"""
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_card(self):
        """Must deal only one card"""
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def tes_deal_hand(self):
        """Must be a list of cards"""
        dealt_hand = self.deck._deal(20)
        self.assertEqual(len(dealt_hand), 20)
        self.assertEqual(self.deck.count(), 32)


if __name__ == '__main__':
    unittest.main()