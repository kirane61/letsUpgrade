#Write a function that can print on a board
#set your board as a list
#Where each index 1-9 corresponds with a number on a number pad
#You get a 3 by 3 board representation

# from IPython.display import clear_output

def display_board(board):
    # clear_output()
    print('--------------------------')
    print('       |        |   ')
    print('   '+ board[6] +'   |   '+board[7]+'    |   '+board[8])
    print('       |        |   ')
    print('--------------------------')
    print('       |        |   ')
    print('   '+ board[3] +'   |   '+board[4]+'    |   '+board[5])
    print('       |        |   ')
    print('--------------------------')
    print('       |        |   ')
    print('   '+ board[0] +'   |   '+board[1]+'    |   '+board[2])
    print('       |        |   ')
    print('--------------------------')


test_board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(test_board)

# Write a function that can take in a player input and assign their marker as 'X' or 'O'


def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player1: Do you want to be X or O").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Write a function that takes in the board list object , a marker ('x' or'O),dESIRED NUMBER(1-9)

def place_maker(test_board, marker, position):
    test_board[position - 1] = marker

# Write a function takes in a board and check to see if someone has wons?

def check_winner(board, mark):
    return ((board[6] == mark and board[7] == mark and board[8] == mark) or  # across top row
            (board[3] == mark and board[4] == mark and board[5] == mark) or  # across middle row
            (board[0] == mark and board[1] == mark and board[2] == mark) or  # across bottom row

            (board[0] == mark and board[3] == mark and board[6] == mark) or  # across left column
            (board[1] == mark and board[4] == mark and board[7] == mark) or  # across middle column
            (board[2] == mark and board[5] == mark and board[8] == mark) or  # across right coumn

            (board[0] == mark and board[4] == mark and board[8] == mark) or  # across left to right diagonal
            (board[2] == mark and board[4] == mark and board[6]) == mark  # across right to left diagonal
            )

# Write a function that uses the random module to randomly decided which player goes first ?
# You may to lookup random randint() return a string at at which player went first?

import random
def choose_first():
    if(random.randint(0,1)==0):
        return 'player1'
    else:
        return 'player2'

#Write a functio that returns a boolean indicating whether a space on the board is freely available?
def space_check(board,position):
    if board[position-1]==' ':
        return True
    else:
        return False


#Write a function that check if the board is full and return a boolean value - True is full. Otherwise False
def full_board_check(board):
    for i in range(9):
        if(space_check(board, i)):
            return False

    return True

#Step 8:Write a function that asks for a players next position (as anumber 1-9)
# And then uses the function from step 6 to check if its a free position.
#If it is then return the position for later use

def player_choice(board):
    position = 10

    while position-1 not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or not space_check(test_board, position - 1):
        position = int(input("Choice your next  position (1-9)"))

    return position

#STEP 9:
# write a function that asks the player if they want to play again and return a boolean.
#If they want to play again and returns a boolean True if they do want to play


def check_for_replay():
    user_input = input("Press Y to play again or N to stop it")
    return user_input

#Step 10:
# Here use the while loop and the functions you have made to run the game

print("Welcome to Tic Tac Toe")
while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + "will go first.")

    if check_for_replay().lower()[0] == 'y':
        game_on = True

    else:
        game_on = False

    while game_on:
        if turn == 'player1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_maker(theBoard, player1_marker, position)
            display_board(theBoard)

            if check_winner(theBoard, player1_marker):
                display_board(theBoard)
                print("Congratulations! You have won the game !")
                game_on = False

            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is draw !")

                else:
                    turn = "player2"
        else:
            turn = 'player2'
            display_board(theBoard)
            position = player_choice(theBoard)
            place_maker(theBoard, player2_marker, position)
            display_board(theBoard)

            if check_winner(theBoard, player2_marker):
                display_board(theBoard)
                print("Congratulations! "+player2_marker+"  won the game!")
                game_on = False

            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("The game is draw!")
                else:
                    turn = "player1"
        
        if not check_replay():
            break


