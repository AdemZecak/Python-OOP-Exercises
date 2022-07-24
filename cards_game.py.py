import random 


class Card():

    def __init__(self,suit,value):
        self.suit = suit 
        self.value = value

    def show(self):
        print("{} of {}".format(self.value,self.suit))


class Deck():
    
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        signs = ["Spades","Clubs","Diamonds","Hearts"]
        for i in signs:
            for j in range(1,14):
                self.cards.append(Card(i,j))

    def show(self):
        for k in self.cards:
            k.show()


    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            random_number = random.randint(0,i)
            self.cards[i],self.cards[random_number] = self.cards[random_number], self.cards[i]


    def drawCard(self):
        return self.cards.pop()


class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw(self,deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()



deck = Deck()
deck.shuffle()

player = Player("Mike")
player.draw(deck)
player.showHand()


card = deck.drawCard()
card.show()


