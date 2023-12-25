# game screen
    # current lives
    # current score
    # pause button
    # sound on/off button
    # game board
        # blocks
        # ball
        # bar

from turtle import Screen
from menu import MenuItem
from block import Block

screen = Screen()

screen.setup(width=1200, height=900)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)
screen.listen()

LIVES = 4
SCORE = 0
TITLE = 'BREAKOUT'

left_menu = MenuItem()
left_menu.goto(-575,400)
left_menu.write(f'x{LIVES}', font=('VT323', 35, 'normal'))

right_menu = MenuItem()
right_menu.goto(550,400)
right_menu.write(SCORE, font=('VT323', 35, 'normal'))

center_menu = MenuItem()
center_menu.goto(-50,400)
center_menu.write(TITLE, font=('VT323', 35, 'normal'))

back_row = Block()
# back_row.goto(0,0)
# back_row.pendown()
# back_row.color('red')
# back_row.forward(20)
# back_row.right(90)
# back_row.forward(10)
# back_row.right(90)
# back_row.forward(20)
# back_row.right(90)
# back_row.forward(10)
# back_row.right(90)

back_row.draw_rectangle('blue')


screen.exitonclick()