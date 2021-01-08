"""
Black Jack Game
"""

class Card():
	"""
	Card class is used to defie the suits, ranks and values for each rank
	"""
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return f'Value of {self.rank} of {self.suit} is {self.value}'

class Deck():
	"""
	Deck class is used to create a deck using the Card class, shuffle the pack and also remove a card
	"""
	def __init__(self):
		
		self.deck_cards = []

		for suit in suits:
			for rank in ranks:
				self.deck_cards.append(Card(suit,rank))

	def shuffle_cards(self):
		random.shuffle(self.deck_cards)

	def remove_card(self):
		return self.deck_cards.pop()

class Hand():
	"""
	Hand card is used to each player and has functions like 
	    hit 			- to ask for another card
	    add_cards 		- to get sum of the current hand
	""" 
	def __init__(self,name,handvalue=0,pot=0):
		
		self.name = name
		self.hand_cards = []
		self.handvalue = handvalue
		self.cardvalue = 0
		self.pot = pot

	def hit(self,new_card):
		
		self.hand_cards.append(new_card)


	def add_cards(self):
		
		self.cardvalue = 0
		for cards in range(len(self.hand_cards)):

			if type(self.hand_cards[cards].value) == type([]):
				
				if abs(21 - self.cardvalue ) < 12:
					self.cardvalue  = self.cardvalue  + (self.hand_cards[cards].value[0])
				else:
					self.cardvalue  = self.cardvalue  + (self.hand_cards[cards].value[1])
			else:	
				self.cardvalue  = self.cardvalue  + (self.hand_cards[cards].value)
		return self.cardvalue

	def check_bet(self):

		bet_value = 0
		
		while bet_value not in range(1,self.handvalue+1):
			print('\n'*100)
			print (f'\nYou can select upto {self.handvalue} chips')
			print (f'Please select a bet amount:')
			bet_value = int(input(''))
		return bet_value

	def lose_handv(self,value):
		self.handvalue -= value

	def win_handv(self,value):
		self.handvalue += value

	def add_pot(self,value):
		self.pot += value*2

	def empty_pot(self):
		self.pot = 0


def display(who,cards):
	"""
	Display function will display the full hand for the player and only one card for the dealer
	"""
	if who == 'player':
		print('\nYou have the following cards')
		for list1 in range(len(player.hand_cards)):
			print(f'{player.hand_cards[list1].rank} of {player.hand_cards[list1].suit}')
			print(f'Value is : {player.hand_cards[list1].value} ')
	else:
		print('\nDealer has the following card')
		print(f'{dealer.hand_cards[0].rank} of {dealer.hand_cards[0].suit}')
		print(f'Value is : {dealer.hand_cards[0].value} ')
		print('The other card cannot be shown. It is hidden')


def ask_player():
	"""
	ask_player function checks if teh player wants to hit to get another card or stay
	"""
	answer = "default"
	while answer not in ['Yes','No']:
		print('\nPlease confirm if you want to hit or stay : Yes for Hit and No to stay')
		answer = input('').capitalize()
	return answer


def check_winner():
	"""
	check_winner function is used to check who teh winner is after the player stays
	"""
	if check_bust(dealer.add_cards()):
		print('Dealer has gone BUST. The player WINS')
#		mini_game = False
		player.win_handv(player.pot)
		player.empty_pot()

	elif player.add_cards() > dealer.add_cards():
		print('Player Wins')
		print(f'Player card value is : {player.add_cards()}')
		print(f'Dealer card value is : {dealer.add_cards()}')
#		mini_game = False
		player.win_handv(player.pot)
		player.empty_pot()

	elif player.add_cards() < dealer.add_cards():
		print('Dealer Wins')
		print(f'Player card value is : {player.add_cards()}')
		print(f'Dealer card value is : {dealer.add_cards()}')
#		mini_game = False
		player.empty_pot()
	
	else:
		print ('Its is a draw !!!')
#		mini_game = False
		player.win_handv(player.pot/2)
		player.empty_pot()
	

def check_bust(cardvalue):
	"""
	check is a simple check to see if the aggregate value of teh cards is above 21 and return true
	"""
	return (cardvalue > 21)

def continue_play():
	"""
	"""
	playc = 'default'
	while playc not in ['Yes','No']:
		print('\nDo you want to contiue playing ? Yes or No')
		playc = input('').capitalize()
	if playc == 'Yes':
		return True
	else:
		print ('\nThank you for playing. Goodbye !')
		main_game = False
		return False
	
## Code Logic 	

# Import random to use shuffle
import random

# define teh suits, ranks and values
suits = ('Club','Spades','Diamond','Hearts')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':[1,11]}

dealer = Hand('Dealer')
player = Hand('Player',1000)

main_game = True

print ('\n'*100)
print ('   Welcome to the Game  ')
print ('    B L A C K J A C K   ')

while main_game:

	# Check player has chips to play

	if player.handvalue == 0:
		print('\nSorry, you do not have any chips to play. The game is over')
		main_game = False
		break
	else: 
		if continue_play() == False:
			break
		pbet = player.check_bet()
		print('\n'*100)
		print(f'\nYou have added {pbet} to the pot')
		player.lose_handv(pbet)
		player.add_pot(pbet)
		print(f'The pot value is {player.pot}')


	# Create a deck of 52 cards
	my_deck = Deck()

	# Shuffle the deck 5 times
	for count in range(5):
		my_deck.shuffle_cards()

	player.hand_cards=[]
	dealer.hand_cards=[]

	# Distribute 2 cards each to the dealer and player
	for i in range(2):
		dealer.hit(my_deck.remove_card())
		player.hit(my_deck.remove_card())

	# Display the players cards and 1 card of the dealer
	display('player',player.hand_cards)
	display('dealer',dealer.hand_cards)

	# Varaibles
	player_stay = False
	mini_game = True
	round = 0
	pbet = 0 

	# Game Loop
	while mini_game:

		# If aggregate of players cards is above 21 - Game over
		if player.add_cards() == 21:
			print ('Its a BLACKJACK. The Player has WON !!')
			mini_game = False
			player.win_handv(player.pot)
			player.empty_pot()
			break

		round += 1
		#print (f'\nRound : {round}')

		#print(player.pot,player.handvalue)

		# If player says Hit, give one more card to the player
		if ask_player() == 'Yes':
			player.hit(my_deck.remove_card())
			print('\n'*100)
			display('player',player.hand_cards)
			print(f'\nThe total value of your hand is : {player.add_cards()}')
			if check_bust(player.add_cards()) == True:
				print('\nI am sorry, you has gone BUST. You have lost this round')
				mini_game = False
				player.empty_pot()
				break
		# If plays says stay, hold players cards and move to dealer
		else:
			player_stay = True
					
		while player_stay == True:
			
			# If dealer aggregate is 17 or higher, go to check who is the winner
			if dealer.add_cards() >= 17:
				print(f'The dealer total is {dealer.add_cards()}')
				player_stay = False
				mini_game = False
				check_winner()
				break
			# If dealer aggregate is < 17, hit a card for the dealer
			else:
				dealer.hit(my_deck.remove_card())
				