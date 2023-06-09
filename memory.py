# Memory, puzzle game of number pairs.

# Import modules
from random import (clear, shape, stamp, update, ontimer,
                    write, shuffle, setup, addshape, hideturtle,
                    tracer, onscreenclick, done)
from turtle import (up, goto, down, color, begin_fill, forward,
                    left, end_fill)

from freegames import path

# Define variables
car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64


# Draw white square with black outline at (x, y).
def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


# Convert (x, y) coordinates to tiles index.
def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


# Convert tiles count to (x, y) coordinates
def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


# Update mark and hidden tiles based on tap.
def tap(x, y):
    spot = index(x, y)
    mark = state['mark']
    # Count the number of taps
    state['tap_count'] = state.get('tap_count', 0) + 1
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    # Display the number of taps
    print(f"Tap count: {state['tap_count']}")


# Draw image and tiles.
def draw():
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)
    # Mostrar cuando el juego fue terminado
    if all(not h for h in hide):
        up()
        goto(0, -150)
        color('black')
        write('¡Juego terminado!', align='center',
              font=('Arial', 24, 'normal'))


# Initialize the game
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
