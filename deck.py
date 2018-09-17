from random import shuffle as shuff
from deck_of_cards.card import Card
class Deck:
    def __init__(self):
        suites = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']        
        self.cards = [Card(value, suit) for suit in suites for value in values]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def _deal(self, num):
        count = self.count()
        actual = min(count, num)
        if count == 0:
            raise ValueError('All cards have been dealt')
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def shuffle(self):
        shuff(self.cards)
        return self.cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)



    
    

    