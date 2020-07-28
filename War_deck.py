import random
values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8
        ,'nine':9,'ten':10,'jack':11,'queen':12,'king':13, 'ace':14}
suits= ('Hearts','Diamonds','Spades','Clubs')
ranks= ('two','three','four','five','six','seven','eight','nine','ten',
        'jack','queen','king','ace')
game_on=True

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value= values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                create_card = Card(suit,rank)
                self.all_cards.append(create_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()
    
    

class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
    
    def remove_one(self):
        return self.all_cards.pop(0)
        
    def add_cards(self,new_cards):
        if type(new_cards)== type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

print('Hi, Welcome to Deck Wars!!!!')
print('****************************\n\n\n')
print('Rules\n*****\n\n')
print('A deck of shuffled cards is divided into 2 players')
print('They each draw out a card and compare for higher rank')
print('The player having caard with higher rank takes both cards')
print('In case of draw we get a war!!')
print('In a war 7 cards are drawn and again the player with higher rank takes it all')
print('Players fight against one another till one dies ie out of cards!')

player1= Player('One')
player2= Player('Two')
new_deck= Deck()
new_deck.shuffle()

for x in range(26):
    player1.add_cards(new_deck.deal_one())
    player2.add_cards(new_deck.deal_one())        

round_num=0

while game_on:
    round_num+=1
    print(f'Round {round_num}')
    if len(player1.all_cards)==0:
        print('Player one has lost!!\nTwo Wins!!!')
        game_on= False
        break
    if len(player2.all_cards)==0:
        print('Player two has lost!!\nOne Wins!!!')
        game_on= False
        break
    
    p1 =[]
    p2 =[]
    p1.append(player1.remove_one())
    p2.append(player2.remove_one())
    war = True
    while war:
        if p1[-1].value > p2[-1].value:
            player1.add_cards(p1)
            player1.add_cards(p2)
            war = False
        elif p1[-1].value < p2[-1].value:
            player2.add_cards(p1)
            player2.add_cards(p2)
            war = False
        else:
            print("War!!\n")
            if len(player1.all_cards)<7:
                print('Player one doesnt have cards to declare war')
                print('Player two wins!!')
                game_on= False
                break
            elif len(player2.all_cards)<7:
                print('Player two doesnt have cards to declare war')
                print('Player one wins!!')
                game_on= False
                break
            else:
                for num in range(7):
                     p1.append(player1.remove_one())
                     p2.append(player2.remove_one())
                    
            
    