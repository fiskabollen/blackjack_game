from random import shuffle
from sys import exit

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players.
    """
    def __init__(self):
        print("Creating New Ordered Deck")
        self.allcards = [(r,s) for s in SUITE for r in RANKS ]

    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allcards)

    def split_deck(self):
        return (self.allcards[:2],self.allcards[2:4],self.allcards[4:])

class Hand:
    """ Defines the rules and sets out player hand. What to do when stick or twist etc.
    """
    def __init__(self,cards):
        self.cards = cards

    def remove_cards(self):
        interim = []
        interim.append(self.cards.pop())
        return interim

    		
    	
        	
        		
class Player:
    """ 
    This is the player class. This will create a player and decide what moves they are going to do.
    """
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand		
	
    def assign_value(self,ranks):
        first = ranks
        
        try:
            x = int(first)
            return x			
            			
        except:
            x = 10
            return x			
        
    
    def value_of_ace(self, ranks):
        value_of_Ace = input('Would you like your Ace card to be worth 1 or 11? ')
        if value_of_Ace == '1':
            Ace_Value = int(value_of_Ace)
            return Ace_Value			
        elif value_of_Ace == '11':
            Ace_Value = int(value_of_Ace)
            return Ace_Value		
        else:
            print('Please put in either 1 or 11')		
    
    def add_to_player_list(self, added_cards):
        return self.hand.cards.extend(added_cards)

    def check_five_card_trick(self,cards):
        if len(self.hand.cards)>= 5:
            return True
        else:
            return False		

		
		

		
		
		
		
	
	
d = Deck()
d.shuffle()
p1_list, p2_list, rest = d.split_deck()

# create players

Dealer = Player('Dealer',Hand(p1_list))
User_Name = input('What is your name? ')
Human = Player(User_Name, Hand(p2_list))
Deck  = Hand(rest)

deal_value = Dealer.hand.cards
user_value = Human.hand.cards

#print(deal_value)
print(User_Name + ' here are your cards!')
print(user_value)

dealer_card_one = deal_value[0][0]
#print(dealer_card_one)
dealer_card_two = deal_value[1][0]
#print(dealer_card_two)

if deal_value[0][0] == 'A':
    deal_card_value = 11 
else:
    deal_card_value = Dealer.assign_value(dealer_card_one)    	
    	
if deal_value[1][0] == 'A':
    if deal_value[1][0] == deal_value[0][0]:
        deal_card_value2 = 1
    else:
        deal_card_value2  = 11	
    
else:
    deal_card_value2 = Dealer.assign_value(dealer_card_two)	
    	
#type_dealer_one = type(deal_card_value)
#type_dealer_two = type(deal_card_value2)
#print(type_dealer_one)
#print(type_dealer_two)
#print(deal_card_value)
#print(deal_card_value2)
final_dealer_round = (deal_card_value) + (deal_card_value2)
#print('dealer after one round')

#print(final_dealer_round)

user_card_one = user_value[0][0]
#print(user_card_one)
user_card_two = user_value[1][0]
#print(user_card_two)

if user_value[0][0] == 'A':
    user_card_value = Human.value_of_ace(user_card_one)
else:
    user_card_value = Human.assign_value(user_card_one)    	
    	
if user_value[1][0] == 'A':
    user_card_value2 = Human.value_of_ace(user_card_two)
else:
    user_card_value2 = Human.assign_value(user_card_two)	

final_user_round = (user_card_value) + (user_card_value2)
#print('user')
#print(user_card_value)
#print(user_card_value2)
#print(final_user_round)


while final_dealer_round < 16:
    interim = Deck.remove_cards()
    #print(interim)
    interim_card = interim[0][0]	
    if interim[0][0] == 'A':
        if final_dealer_round >= 11:
            new_deal_card_value = 1
        else:
            new_deal_card_value = 11		
    else:
        new_deal_card_value = Dealer.assign_value(interim_card)	
    	
    #print('Card has a value of ')
    #print(new_deal_card_value)
    final_dealer_round += new_deal_card_value
    #print('After this round the dealer has')
    #print (final_dealer_round)
    deal_value.extend(interim)
    #print('The dealer now has a hand of ')	
    #print(deal_value)
    interim.clear()  # Added in python3.(? maybe 5?)
    del interim[:]
    #print (interim)
	
user_submit = False
#user_bust = False

while user_submit == False:

    User_Choice = input('Would you like to stick or twist? ')

    if User_Choice == 'stick':
        user_submit = True
    elif User_Choice == 'twist':
        interim = Deck.remove_cards()
        #print(interim)
        interim_card = interim[0][0]	
        if interim[0][0] == 'A':
            new_user_card_value = Human.value_of_ace(interim_card)
        else:
            new_user_card_value = Human.assign_value(interim_card)
        #print('Card has a value of ')
        #print(new_user_card_value)
        final_user_round += new_user_card_value
        #print('After this round the user has')
        #print (final_user_round)
        user_value.extend(interim)
        print('The user now has a hand of ')	
        print(user_value)
        interim.clear()  # Added in python3.(? maybe 5?)
        del interim[:]
    else:
        print('Please specify either stick or twist?')
			
user_five = Human.check_five_card_trick(user_value)
deal_five = Dealer.check_five_card_trick(deal_value)

if user_five != deal_five:
    if user_five:
        if final_user_round <= 21:
            print('The user has won the game with a five card trick')
            exit(0)			
        else:
            print("You're bust!!!")
            print('The dealer has won')			
            exit(0)			
    elif deal_five:
        if final_deal_round > 21:
            print('The dealer has won the game with a five card trick')
            exit(0)			
			
    
	
	
	


if final_user_round > 21 and final_dealer_round > 21:
    print('Both the dealer and you are bust no one wins')
    
elif final_user_round > 21:
    print('You have bust')
    print('The dealer has won')	

elif final_dealer_round > 21:
    print('The dealer has bust')
    print(User_Name + ' has won')

elif final_user_round > final_dealer_round:
    print( User_Name + ' has scored {}'.format(final_user_round))
    print('The dealer has scored {}'.format(final_dealer_round))
    print('You have won')	

else:
    print( User_Name + ' has scored {}'.format(final_user_round))
    print('The dealer has scored {}'.format(final_dealer_round))
    print('The dealer has won.')	


		
	
	
	
	





	
 


    


