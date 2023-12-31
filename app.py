# game screen

# pause button
# game board
# add scoring
# add lose of life when ball missed by paddle
# add extra life upon clearing board
# add board reset upon clearing of the board

from turtle import Screen
from menu import MenuItem
from block import Block
from paddle import Paddle
from ball import Ball
import time

screen = Screen()

screen.setup(width=1250, height=950)
screen.bgcolor("black")
screen.colormode(255)
screen.title("Breakout")
screen.tracer(0)
screen.listen()

LIVES = 4
SCORE = 0
TITLE = "BREAKOUT"

left_menu = MenuItem()
left_menu.goto(-575, 400)
left_menu.write(f"x{LIVES}", font=("VT323", 35, "normal"))

right_menu = MenuItem()
right_menu.goto(550, 400)
right_menu.write(SCORE, font=("VT323", 35, "normal"))

center_menu = MenuItem()
center_menu.goto(-50, 400)
center_menu.write(TITLE, font=("VT323", 35, "normal"))

border = MenuItem()
border.goto(-600, 390)
border.color("#FF1493")
border.pendown()
border.pensize(2)
border.forward(1190)
border.right(90)
border.forward(830)
border.right(90)
border.forward(1190)
border.right(90)
border.forward(830)

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
    x_cor = -585 + i * 90
    block = Block()
    block.penup()
    block.goto(x_cor, 300)
    block.draw_rectangle(back_R, 20, 147)
    block.sety(300)
    block.setx(x_cor)
    back_R = back_R - 10
    back_row.append(block)

for i in range(13):
    x_cor = -585 + i * 90
    block = Block()
    block.penup()
    block.goto(x_cor, 250)
    block.draw_rectangle(four_R, 40, 147)
    block.sety(250)
    block.setx(x_cor)
    four_R = four_R - 10
    row_four.append(block)

for i in range(13):
    x_cor = -585 + i * 90
    block = Block()
    block.penup()
    block.goto(x_cor, 200)
    block.draw_rectangle(three_R, 60, 147)
    block.sety(200)
    block.setx(x_cor)
    three_R = three_R - 10
    row_three.append(block)

for i in range(13):
    x_cor = -585 + i * 90
    block = Block()
    block.penup()
    block.goto(x_cor, 150)
    block.draw_rectangle(two_R, 80, 147)
    block.sety(150)
    block.setx(x_cor)
    two_R = two_R - 10
    row_two.append(block)

for i in range(13):
    x_cor = -585 + i * 90
    block = Block()
    block.penup()
    block.goto(x_cor, 100)
    block.draw_rectangle(one_R, 100, 147)
    block.sety(100)
    block.setx(x_cor)
    one_R = one_R - 10
    row_one.append(block)

for i in range(13):
    x_cor = -585 + i * 90
    block = Block()
    block.penup()
    block.goto(x_cor, 50)
    block.draw_rectangle(zero_R, 120, 147)
    block.sety(50)
    block.setx(x_cor)
    zero_R = zero_R - 10
    row_zero.append(block)

for i in range(13):
    x_cor = -585 + i * 90
    block = Block()
    block.penup()
    block.goto(x_cor, 0)
    block.draw_rectangle(neg_R, 140, 147)
    block.sety(0)
    block.setx(x_cor)
    neg_R = neg_R - 10
    row_neg.append(block)

paddle = Paddle()
ball = Ball()

screen.onkey(paddle.move_right, "Right")
screen.onkey(paddle.move_left, "Left")

game_on = True

all_rows = []
all_rows.append(row_neg)
all_rows.append(row_zero)
all_rows.append(row_one)
all_rows.append(row_two)
all_rows.append(row_three)
all_rows.append(row_four)
all_rows.append(back_row)

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.drop()

    # paddle hit
    if ball.ycor() == -330 and ball.distance(paddle) < 150 or ball.ycor() > 375:
        ball.bounce_y()

    # wall hit
    if ball.xcor() == -590 or ball.xcor() == 580:
        ball.wall_hit()

    # ball miss
    if ball.ycor() == -450:
        print('the whiff')
        paddle.reset()
        ball.reset()


    # block hit
    for row in all_rows:
        for index, block in enumerate(row):
            if (
                ball.ycor() >= block.ycor() - 40
                and ball.ycor() <= block.ycor()
                and ball.xcor() >= block.xcor()
                and ball.xcor() <= block.xcor() + 80
            ):
                ball.bounce_y()
                block.clear()
                row.pop(index)
                print(ball.move_speed)
                if row == all_rows[0]:
                    ball.move_speed = ball.move_speed
                elif row == all_rows[1]:
                    if ball.move_speed <= 0.06:
                        ball.move_speed = ball.move_speed
                    else:
                        ball.move_speed = 0.06
                elif row == all_rows[2]:
                    if ball.move_speed <= 0.05:
                        ball.move_speed = ball.move_speed
                    else:
                        ball.move_speed = 0.05
                elif row == all_rows[3]:
                    if ball.move_speed <= 0.04:
                        ball.move_speed = ball.move_speed
                    else:
                        ball.move_speed = 0.04
                elif row == all_rows[4]:
                    if ball.move_speed <= 0.03:
                        ball.move_speed = ball.move_speed
                    else:
                        ball.move_speed = 0.03
                elif row == all_rows[5]:
                    if ball.move_speed <= 0.02:
                        ball.move_speed = ball.move_speed
                    else:
                        ball.move_speed = 0.02
                elif row == all_rows[6]:
                    if ball.move_speed <= 0.01:
                        ball.move_speed = ball.move_speed
                    else:
                        ball.move_speed = 0.01
                else:
                    print('no')


screen.mainloop()
