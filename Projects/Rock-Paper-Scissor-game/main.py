import random

status = False
inputs = ['rock', 'scissor', 'paper']


def take_input():
    player = input("Enter your move:").lower()
    computer_input = inputs[random.randint(0, 2)]
    return player, computer_input


def check_winner(player1,player2):
    if player1 == player2:
        print('Its a Tie')
    elif player1 == 'rock':
        if player2 == 'paper':
            print("Computer wins as %s covers %s" %(player2, player1))
        else:
            print('You Won as %s smashes %s' %(player1, player2))

    elif player1 == 'paper':
        if player2 == 'scissor':
            print("Computer wins as %s cuts %s " %(player2, player1))
        else:
            print("You won! as %s covers %s"%(player1, player2))

    elif player1 == 'scissor':
        if player2 == 'rock':
            print("Computer wins as %s smashes %s"%(player2, player1))
        else:
            print("You Won! as %s cuts %s" %(player2, player1))

    else:
        print("Please enter a valid move for example:Check spellings ")


while(status == False):
    player1, player2 = take_input()
    check_winner(player1, player2)
