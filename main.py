import sys
import os
path = os.path.join(os.path.dirname(__file__), '..')
sys.path.extend([path])

from deck_of_cards.card import Card
from deck_of_cards.deck import Deck

#trying card combinations
# c = Card('A', 'Spades')
# c1 = Card('K', 'Hearts')
# c2 = Card('3', 'Diamonds')
# c3 = Card('10', 'Hearts')

# print(c, c1, c2, c3)

d = Deck()
print(d)
print(d.deal_hand(2))
print('return from count function after deal_hand: ', d.count())
print(d.deal_card())
print('return from count function after deal_card: ', d.count())
print(d.shuffle())



