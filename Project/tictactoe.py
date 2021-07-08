import pygame as pg, sys

from pygame.locals import *
import time

# Initialis the variables now!!

XO = "player1"
winnerOfGame = None
drawStatuses = False
width = 500
height = 500

whiteRgb = (211, 211, 211)

colorOfLine = (10, 10, 10)

# Setting Up the board
ttt = [[None] * 3, [None] * 3, [None] * 3]

# Now initialise the pygame

pg.init()
framePerSecond = 30
CLOCK = pg.time.Clock()
displayScreen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe Game")

# Loading and resizing the images into game

intro = pg.image.load('tictactoe.jpg', 'opening')
user1 = pg.image.load('X.png', 'player1')
user2 = pg.image.load('O.png', 'player2')

# Resizing
user1 = pg.transform.scale(user1, (100, 100))
user2 = pg.transform.scale(user2, (100, 100))
intro = pg.transform.scale(intro, (width, height + 100))


# In pygame, the blit() function is used on the surface to draw an image on top of another image.
def gameOpening():
    displayScreen.blit(intro, (0, 0))
    pg.display.update()
    time.sleep(1)
    displayScreen.fill(whiteRgb)

    # Draw vertical lines
    # first line
    pg.draw.line(displayScreen, colorOfLine, (width / 3, 0), (width / 3, height), 7)
    # second line
    pg.draw.line(displayScreen, colorOfLine, (width / 3 * 2, 0), (width / 3 * 2, height), 7)

    # Now draw horizontal lines
    # first line
    pg.draw.line(displayScreen, colorOfLine, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(displayScreen, colorOfLine, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    drawStatus()


def drawStatus():
    global drawStatuses

    if winnerOfGame is None:
        message = XO.upper() + "'s Turn.'"
    else:
        message = winnerOfGame.upper() + "is won!"

    if drawStatuses:
        message = "Game Draw!!"

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))

    # copy the rendered message onto the displayboard
    displayScreen.fill((0, 0, 0), (0, 500, 600, 100))
    text_rectangle = text.get_rect(center=(width / 2, 600 - 50))
    displayScreen.blit(text, text_rectangle)
    pg.display.update()


# Function to check winner by analysing

def checkWinner():
    global ttt, winnerOfGame, drawStatuses


# Check for the winning rows

    for row in range(0, 3):
        if (ttt[row][0] == ttt[row][1] == ttt[row][2]
            and (ttt[row][0] is not None)):
        # IF the complete row is filled then he is the winner
            winnerOfGame = ttt[row][0]
            pg.draw.line(displayScreen, (250, 0, 0), (0, (row + 1) * height / 3 - height / 6),
                     (width, (row + 1) * height / 3 - height / 6), 4)
            break

# Check for column winning

    for column in range(0, 3):
        if (ttt[0][column] == ttt[1][column] == ttt[2][column] and (ttt[0][column] is not None)):
        # if the complete column is filled then he is the winner

            winnerOfGame = ttt[0][column]
            pg.draw.line(displayScreen, (250, 0, 0), ((column + 1) * width / 3 - width / 6, 0),
                     ((column + 1) * width / 3 - width / 6, height), 4)
            break

# Check for the diagonal winning

    if (ttt[0][0] == ttt[1][1] == ttt[2][2]) and (ttt[0][0] is not None):
    # winner diagonally
        winnerOfGame = ttt[0][0]
        pg.draw.line(displayScreen, (255, 70, 70), (50, 50), (450, 450), 4)

    if (ttt[0][2] == ttt[1][1] == ttt[2][0]) and (ttt[0][2] is not None):

    # winner diagonally

        winnerOfGame = ttt[0][2]
        pg.draw.line(displayScreen, (255, 70, 70), (450, 50), (50, 450), 4)

    # Checking for draw
    if (all([all(row) for row in ttt]) and winnerOfGame is None):
        drawStatuses = True
    drawStatus()


# Defining the marks in our game

def drawXo(row, column):
    global ttt, XO
    if row == 1:
        posx = 30
    if row == 2:
        posx = width / 3 + 30
    if row == 3:
        posx = width / 3 * 2 + 30

    if column == 1:
        posy = 30
    if column == 2:
        posy = height / 3 + 30
    if column == 3:
        posy = height / 3 * 2 + 30
    ttt[row - 1][column - 1] = XO
    if (XO == "player1"):
        displayScreen.blit(user1, (posy, posx))
        XO = "player2"
    else:
        displayScreen.blit(user2, (posy, posx))
        XO = "player1"
    pg.display.update()


# //check for user winning or not after every move
def clickUser():
    # get coordinates of mouse
    x, y = pg.mouse.get_pos()

    # get column of width
    if (x < width / 3):
        column = 1
    elif (x < width / 3 * 2):
        column = 2
    elif (x < width):
        column = 3
    else:
        column: None

    # Get row of mouse click

    if (y < height / 3):
        row = 1
    elif (y < height / 3 * 2):
        row = 2
    elif (y < height):
        row = 3
    else:
        row = None

    if (row and column and ttt[row - 1][column - 1] is None):
        global XO

        drawXo(row, column)
        checkWinner()


# Resetting game

def resetGame():
    global ttt, winnerOfGame, XO, drawStatuses
    time.sleep(4)
    XO = "player1"
    drawStatuses = False
    gameOpening()
    winnerOfGame = None
    ttt = [[None] * 3, [None] * 3, [None] * 3]


# Run game forever
gameOpening()
    # Run forever
while True:

    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            clickUser()
            if winnerOfGame or drawStatuses:
                resetGame()

    pg.display.update()
    CLOCK.tick(framePerSecond)
