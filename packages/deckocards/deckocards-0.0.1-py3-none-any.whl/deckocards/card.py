import random
class Card():
    def __init__(self, num, suit, bj):
        self.num = num
        self.suit = suit
        if bj == True:
            self.name = self.fix_name(self.num, True)
        else:
            self.name = self.fix_name(self.num, False)
        self.id = str(self.num) + self.suit
    def fix_name(self, num, bj):
        names = ['ace', 'jack', 'queen', 'king']
        if num == 1:
            num = 'ace'
        if bj == True:
            if num == 10:
                num = random.choice([10, 'jack', 'queen', 'king'])
        else:
            if num == 11:
                num = 'jack'
            elif num == 12:
                num = 'queen'
            elif num == 13:
                num = 'king'
        return num
