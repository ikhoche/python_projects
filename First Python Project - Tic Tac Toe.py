import random

# Original Display board
def display_board(board):
    print('')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-' + '|'+ '-' + '|'+ '-' )
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-' + '|'+ '-' + '|'+ '-' )
    print(board[1]+'|'+board[2]+'|'+board[3])


# Determines who plays first
def whichplayer_first():
    whichplayerfirst = random.randint(1,2)
    
    print(f'Player {whichplayerfirst}, you go first!')


# Sets the Marker for the first player
def marker_choice():
    firstplayer = 'Wrong'
    markerchoice = ['X','O']
    while firstplayer not in markerchoice:
        
        firstplayer = input("Please Enter X or O:") 
    
    return firstplayer
    

# Sets the Marker position
def location_choice():
    location = 'wrong'
    acceptable_range = range(1,10)
    within_range = False
    
    while location.isdigit()== False or within_range == False:
        
        location = input("Please select where you want to place the marker. Pick a number between 1 and 9:")
        
        if location.isdigit() == False:
            print("Sorry, that is not a digit!")
        
        if location.isdigit():
            if int(location) in acceptable_range:
                within_range = True
            else:
                pass
            
    return int(location)


# Checks to see if a position is full or not
def space_check(board, position):
    if board[position] == 'X' or board[position] == 'O':
        return False
    else:
        return True


# If a position is full -> pick a different one
def player_choice(board):
    
    position = location_choice()
    while space_check(board, position) == False:
            print('Sorry, that position is already full! Please pick a different number!')
            position = location_choice()
    return position


# Checks to see if someone won
def win_check(board):
    
    if board[1] == board[2] == board[3] or board[4] == board[5] == board[6] or board[7] == board[8] == board[9] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[3] == board[6] == board[9] or board[1] == board[5] == board[9] or board[3] == board[5] == board[7]:
        return True
    else:
        return False


def full_board_check(board):
    if board[1] != '1' and board[2] != '2' and board[3] != '3'and board[4] != '4'and board[5] != '5'and board[6] != '6'and board[7] != '7'and board[8] != '8'and board[9] != '9':
        return True
    else:
        return False



# Checks to see if players want to play again
def replay():
    
    # This original choice value can be anything that isn't a Y or N
    choice = 'wrong'
    
    # While the choice is not a digit, keep asking for input.
    while choice not in ['Y','N']:
        
        # we shouldn't convert here, otherwise we get an error on a wrong input
        choice = input("Would you like to keep playing? Y or N ")

        
        if choice not in ['Y','N']:
            choice = input("Would you like to keep playing? Y or N")
    
    if choice == "Y":
        # Game is still on
        return True
    else:
        # Game is over
        return False

    
###Starting the Game###

stillplaying = True

while stillplaying == True:
    
    print("Welcome to Tic Tac Toe!")
    print("Here is the starting board with each number representing a marker position:")
    #while True:
    # First, display the starting board with maker positions.
    start_board = ['#','1','2', '3','4','5', '6','7','8', '9']
    display_board(start_board)
    print("Decide who will be Player 1 and who will be Player 2")
    print("")

    # Randomly decide which player will go first.
    print('I have randomly selected which player goes first.')
    whichplayer_first()

    # Assign markers to each player.
    firstplayer = marker_choice()
    secondplayer = ''

    if firstplayer == 'X':
        secondplayer = 'O'
    else:
        secondplayer = 'X'

    print('')
    print (f'First Player, you are {firstplayer}. Second Player, you are {secondplayer}')

    # Game is on
    game_on = True

    while game_on:
    
        #firstplayer
    
        print('First Player, your turn:')
        # Check and place the marker.
        position = player_choice(start_board)
        start_board[position] = firstplayer
        # Check to see if firstplayer won  and then show the board.
        if win_check(start_board) == True:
            print ('Tic Tac Toe!')
            display_board(start_board)
            break
        else:
            pass
        if full_board_check(start_board) == True:
            print ('Tied Game! Board is Full')
            display_board(start_board)
            break
        else:
            pass
        display_board (start_board)
        print('')

        
        #secondplayer
    
        print('Second Player, your turn:')
        # Check and place the marker.
        position = player_choice(start_board)
        start_board[position] = secondplayer
        # Check to see if second player won and then show the board.
        if win_check(start_board) == True:
            print ('Tic Tac Toe!')
            display_board(start_board)
            break
        else:
            pass
        if full_board_check(start_board) == True:
            print ('Tied Game! Board is Full')
            display_board(start_board)
            break
        else:
            pass
        display_board (start_board)
        print('')
        
    
    stillplaying = replay()







