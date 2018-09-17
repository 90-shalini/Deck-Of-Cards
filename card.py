class Card:
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

