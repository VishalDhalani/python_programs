"""
This is a python progrom to simulate a simple tic tac toe game
"""

# Function Definitions :

def display_board(board):

	"""
	Display the board when the function is called
	"""
	print("\n" *100)
	print('\nThe tic toe board is displayed below :')
	print('Lets start the game !!\n')
	print(f' {board[7]}  |  {board[8]}  |  {board[9]} ')
	print('----------------')
	print(f' {board[4]}  |  {board[5]}  |  {board[6]} ')
	print('----------------')
	print(f' {board[1]}  |  {board[2]}  |  {board[3]} ')


def choose_player(player_list):
	"""
	Choose a random lpayer to start teh game
	""" 
	random.shuffle(player_list)
	return (player_list)

def player_pick(selected_player):
	"""
	Let the chosen player select the marker they want
	"""
	marker = 'Default'
	while marker not in ('X','O'):
	 	print(f'\n{selected_player} Please select your marke (X or O)')
	 	marker = input('').upper()
	if marker == 'X':
		return ('X','O')
	else:
		return ('O','X')

def position_select():
	"""
	Get Input from the player on the position they want to select to place their marker
	"""
	allowed_values = ['1','2','3','4','5','6','7','8','9']
	position = 'Default'
	while position not in allowed_values:
	 	print('\nPlease select a position to place your marker (1-9)')
	 	position = input('')
	return int(position)
	

def position_empty(board,position):
	""" Check if the position selected is available """
	return (board[position] == ' ')

def board_update(board,position,mark):
	""" Update the board with the selected position """
	board[position] = mark

def check_win(board,player):
	"""
	See if the player has won
	"""
	win = False
	if board[7]+board[8]+board[9] == player*3:     	# Horizontal Top
		win = True
	elif board[4]+board[5]+board[6] == player*3:	# HM	
		win = True
	elif board[1]+board[2]+board[3] == player*3:	# HB
		win = True
	elif board[1]+board[4]+board[7] == player*3:	# VL
		win = True
	elif board[2]+board[5]+board[8] == player*3:	# VC
		win = True
	elif board[3]+board[6]+board[9] == player*3:	# VR
		win = True
	elif board[1]+board[5]+board[9] == player*3:	# D1
		win = True
	elif board[3]+board[5]+board[7] == player*3:	# D2
		win = True
	else:
		pass
	return win

def check_draw(board):
	"""
	Check is teh match is a draw
	"""
	full = True
	for item in board:
		if item == ' ':
			full = False
		else:
			pass
	return full	

def replay():
	"""
	Check to see if the players wannt to play another game or exit
	"""

	play = ''
	global playon
	while play not in ('Y','N'):
		print('\nDo you want to restart (Y to restart /N to exit):')
		play = input('').upper()
		if play == 'N':
			print('\nThanks for playing. Goodbye !! ')
			playon = False
	
## Main Logic 

import random

playon = True

while playon == True:

	player_list = ['Player1','Player2']
	test_board = ['#']
	for value in range(9):
		test_board.append(' ')

	game = True
	# Display the board
	display_board(test_board)
	# Choose a random player to Start
	random_player_select = choose_player(player_list)[0]
	# Store teh PLayers choice
	player1_choice,player2_choice = player_pick(random_player_select)
	my_choice = player1_choice

	while game:

	# If Player 1 

		if my_choice == 'X':

			player_position = position_select()

			if position_empty(test_board,player_position) == True:
				board_update(test_board,player_position,player1_choice)
				display_board(test_board)
				my_choice = 'O'
				if check_win(test_board,player1_choice) == True:
					print (f'\n{choose_player(player_list)[0]} has won !!!')
					print ('Game Over')
					game = False
					replay()
					break
				else:
					pass
				if check_draw(test_board) == True:
					game = False 
					print('The match is a draw')
					print('Game Over')
					replay()
					break
				else:
					pass
			else:
				print('Position is not empty.')
				display_board(test_board)

		else:

			player_position = position_select()

			if position_empty(test_board,player_position) == True:
				board_update(test_board,player_position,player2_choice)
				display_board(test_board)
				my_choice = 'X'
				if check_win(test_board,player2_choice) == True:
					print (f'\n{choose_player(player_list)[0]} has won !!!')
					print ('Game Over')
					game = False
					replay()
					break
				if check_draw(test_board) == True:
					game = False 
					print('The match is a draw')
					print('Game Over')
					replay()
					break
			else:
				print('Position is not empty.')
				display_board(test_board)
