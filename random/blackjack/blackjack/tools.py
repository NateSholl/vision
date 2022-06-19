import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck():

    def __init__(self):
        self.allCards = []

        for suit in suits:
            for rank in ranks:
                deck_card = Card(suit,rank)
                self.allCards.append(deck_card)

    def shuffleDeck(self):
        random.shuffle(self.allCards)

    def dealOne(self):
        return self.allCards.pop()

class Player():

    def __init__(self,name,):
        self.name = name
        self.playerCards = []

    def addCards(self,new_cards):
        if type(new_cards) == type([]):
            self.playerCards.extend(new_cards)
        else:
            self.playerCards.append(new_cards)        
        

if __name__ == '__main__':
    test = Deck()