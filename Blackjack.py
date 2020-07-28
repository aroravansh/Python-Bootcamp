import random
values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8
        ,'nine':9,'ten':10,'jack':10,'queen':10,'king':10, 'ace':11}
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
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                create_card = Card(suit,rank)
                self.deck.append(create_card)
    
    def __str__(self):
        deck_comp = ''  
        for card in self.deck:
            deck_comp += '\n '+card.__str__() 
        return 'The deck has:' + deck_comp
        
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal_one(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0    
        
    def add_card(self,card):
        self.cards.append(card)
        self.value+=card.value
        if card.rank=='ace':
            self.aces+=1
    
    def adjust_for_ace(self):
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1

class Chips:
    def __init__(self):
        self.total = 100 
        self.bet = 0
        
    def win_bet(self):
        self.total+=self.bet
    
    def lose_bet(self):
        self.total-=self.bet
            
def take_bet(chip):
    while True:
        try:
            chip.bet = int(input('How much would like to bet: '))
        except:
            print('Sorry write in an integer value')
        else:
            if chip.total<chip.bet:
                print('Not enough to place a bet try again')
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace() 
    
def hit_or_stand(deck,hand):
    global game_on
    while True:
        ans = input('Do you want to hit or stand? ')
        if ans.lower()=='hit':
            hit(deck,hand)
        elif ans.lower()=='stand':
            print('Player stands, Dealer will deal!')
            game_on = False
        else:
            print('Provide a valid input')
            continue
        break
    
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

while True:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())
    
    player_chips = Chips()      
    
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    
    while game_on:  
        
        hit_or_stand(deck,player_hand) 
        
        show_some(player_hand,dealer_hand)  
        
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


     
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        
        show_all(player_hand,dealer_hand)
        
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
     
    print("\nPlayer's winnings stand at",player_chips.total)
    
    
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break    