# game screen

    # pause button
    # game board
        # ball
    # paddle looks long but it really is not long
    # control speed of ball


from turtle import Screen
from menu import MenuItem
from block import Block
from paddle import Paddle
from ball import Ball

screen = Screen()

# screen.setup(width=1200, height=900)
screen.setup(width=1250, height=950)
screen.bgcolor('black')
screen.colormode(255)
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

border = MenuItem()
border.goto(-600, 390)
border.color('#FF1493')
border.pendown()
border.pensize(2)
border.forward(1190)
border.right(90)
border.forward(830)
border.right(90)
border.forward(1190)
border.right(90)
border.forward(830)
# border.shapesize(.1, 100)
# border.showturtle()

back_row = []
row_four = []
row_three = []
row_two = []
row_one = []
row_zero = []
row_neg = []

back_R = 255
four_R = 255
three_R = 255
two_R = 255
one_R = 255
zero_R = 255
neg_R = 255

for i in range(13):
    block = Block()
    block.penup()
    block.goto(-585 + i * 90, 300)
    block.draw_rectangle(back_R,20, 147)
    back_R = back_R - 10
    back_row.append(block)

for i in range(13):
    block = Block()
    block.penup()
    block.goto(-585 + i * 90, 250)
    block.draw_rectangle(four_R,40, 147 )
    four_R = four_R - 10
    row_four.append(block)

for i in range(13):
    block = Block()
    block.penup()
    block.goto(-585 + i * 90, 200)
    block.draw_rectangle(three_R,60, 147)
    three_R = three_R - 10
    row_three.append(block)

for i in range(13):
    block = Block()
    block.penup()
    block.goto(-585 + i * 90, 150)
    block.draw_rectangle(two_R,80, 147 )
    two_R = two_R - 10
    row_two.append(block)

for i in range(13):
    block = Block()
    block.penup()
    block.goto(-585 + i * 90, 100)
    block.draw_rectangle(one_R,100, 147 )
    one_R = one_R - 10
    row_one.append(block)

for i in range(13):
    block = Block()
    block.penup()
    block.goto(-585 + i * 90, 50)
    block.draw_rectangle(zero_R,120, 147 )
    zero_R = zero_R - 10
    row_zero.append(block)

for i in range(13):
    block = Block()
    block.penup()
    block.goto(-585 + i * 90, 0)
    block.draw_rectangle(neg_R,140, 147 )
    neg_R = neg_R - 10
    row_neg.append(block)

paddle = Paddle()
ball = Ball()



screen.onkey(paddle.move_right, 'Right')
screen.onkey(paddle.move_left, 'Left')

game_on = True

while game_on:
    ball.drop()

    if ball.distance(paddle) < 50 or ball.ycor() > 400:
        ball.bounce_y()

    screen.update()

screen.mainloop()
