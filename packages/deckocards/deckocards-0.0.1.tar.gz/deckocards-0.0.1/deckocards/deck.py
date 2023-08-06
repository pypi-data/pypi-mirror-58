import random
from card import Card

class Deck():
    def __init__(self, decks):
        self.decks = decks
        deck1 = []
        deck2 = []
        for suit in ['S', 'H', 'D', 'C']:
            for num in range(1, 13):
                deck1.append(Card(num, suit, False))
            for num in range(1, 10):
                deck2.append(Card(num, suit, False))
                if num == 10:
                    deck2.append(Card(num, True))
                    deck2.append(Card(num, True))
                    deck2.append(Card(num, True))
        self.standard_deck = deck1 * self.decks
        self.bj_deck = deck2 * self.decks
    def pick(self, size):
        self.temp_deck1 = self.standard_deck
        random.shuffle(self.temp_deck1)
        shuffled_deck = self.temp_deck1[0:size]
        #final = []
        #for items in shuffled_deck:
            #final.append(str(items.name) + items.suit)
        return shuffled_deck
    def poker(self):
        return self.pick(5)
    def bj(self):
        self.temp_deck1 = self.bj_deck
        random.shuffle(self.temp_deck1)
        shuffled_deck = self.temp_deck1[0:2]
        final = []
        for items in shuffled_deck:
            final.append(str(items.name) + items.suit)
        return final

if __name__ == '__main__':    
    def run():
        x = Deck(1)
        y = 0
        flushnum = 0
        while y < (10000):
            z = x.poker()
            if z[0].suit == z[1].suit == z[2].suit == z[3].suit == z[4].suit:
                print('Flush!')
                flushnum += 1
                a = []
                for card in z:
                    a.append(card.id)
                print(a)
                print(y)
                print(flushnum)
            y += 1
        print(flushnum/y)
    run()
