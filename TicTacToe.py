"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""

    #Select color red and width 10
    color('red')
    width(10)
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    """Draw O player."""

    #Select color blue and width 10
    color('blue')
    width(10)
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


"""Variables for Tic Tac Toe"""
state = {'player': 0}
players = [drawx, drawo]
#draw board with '-' for empty
board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    row = int((y + 200) / 133)
    col = int((x + 200) / 133)

    if board[row][col] == '-':
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
        board[row][col] = 'X' if player == 0 else 'O'


"""initialize the game."""
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()