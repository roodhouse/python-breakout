# game over
    # hide board, ball and paddle
    # print out the high scores
    # if player score is higher than lowest highscore than offer input to put in name and save into highscores

from turtle import Screen
import turtle
from menu import MenuItem
from block import Block
from paddle import Paddle
from ball import Ball
import time
import csv

screen = Screen()

screen.setup(width=1250, height=950)
screen.bgcolor("black")
screen.colormode(255)
screen.title("Breakout")
screen.tracer(0)
screen.listen()

prompt = turtle.Turtle()

highscores = []
print(highscores)
with open('highscore.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        highscores.append(row)

print(highscores)
print(type(highscores[0][1]))

for high in highscores:
    high[1] = int(high[1])

print(type(highscores[0][1]))
highscores = sorted(highscores, key=lambda x: x[1], reverse=True)

print(highscores)

LIVES = 1
SCORE = 0
TITLE = "BREAKOUT"
EMPTY = 0
ROUND = 1

left_menu = MenuItem()
left_menu.goto(-575, 400)
left_menu.write(f"x{LIVES}", font=("VT323", 35, "normal"))

right_menu = MenuItem()
right_menu.goto(550, 400)
right_menu.write(SCORE, font=("VT323", 35, "normal"))

center_menu = MenuItem()
center_menu.goto(-50, 400)
center_menu.write(TITLE, font=("VT323", 35, "normal"))

highscores_table = MenuItem()
highscores_table.goto(-50, -100)

paddle = Paddle()
paddle.hideturtle()
ball = Ball()
ball.hideturtle()

screen.onkey(paddle.move_right, "Right")
screen.onkey(paddle.move_left, "Left")

game_key = MenuItem()
game_key.goto(-150,0)
game_key.write(f'ROUND {ROUND}', font=("VT323", 135, "normal"))

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

screen.update()

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

all_rows = []

def create_board():
    global back_row, back_R, row_four, four_R, row_three, three_R, row_two, two_R, row_one, one_R, row_zero, zero_R, row_neg, neg_R
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

    all_rows.append(row_neg)
    all_rows.append(row_zero)
    all_rows.append(row_one)
    all_rows.append(row_two)
    all_rows.append(row_three)
    all_rows.append(row_four)
    all_rows.append(back_row)
 
game_on = False

paused_x = None
paused_y = None
pause_direction = None

def unpause():
    global paused_x, paused_y, paused_dx, paused_dy, pause_direction
    ball.x_move = paused_x
    ball.y_move = paused_y
    ball.setheading(pause_direction)

    ball.showturtle()
    paddle.showturtle()

    for row in all_rows:
        for item in row:
            full_color = item.color()[0]    
            item.draw_rectangle(int(full_color[0]), int(full_color[1]), int(full_color[2]))

    print('unpaused')
    game_key.clear()
    game_key.hideturtle()

    screen.onkey(start, 'space')
    screen.onkey(paddle.move_right, "Right")
    screen.onkey(paddle.move_left, "Left")

def start():
    global game_on, paddle, ball, all_rows, back_R, four_R, three_R, two_R, one_R, zero_R, neg_R, EMPTY, paused_x, paused_y, pause_direction
    if not game_on:
        game_on = True
        print(game_on)
        all_rows.clear()
        back_R = 255
        four_R = 255
        three_R = 255
        two_R = 255
        one_R = 255
        zero_R = 255
        neg_R = 255
        create_board()
        paddle.reset()
        ball.reset()
        paddle.showturtle()
        ball.showturtle()
        game_key.clear()
        game_key.hideturtle()
        EMPTY = 0
        play()
    else:
        print('game is paused')
        paused_x = ball.x_move
        paused_y = ball.y_move
        pause_direction = ball.heading()
        ball.x_move = 0
        ball.y_move = 0
        ball.hideturtle()
        paddle.hideturtle()

        for row in all_rows:
            for item in row:
                item.clear()

        game_key.write('PAUSED', font=("VT323", 135, "normal"))
        screen.onkey(None, key='Right')
        screen.onkey(None, key='Left')
        screen.onkey(unpause, 'space')

screen.onkey(start, 'space')

def winner():
    global ROUND, LIVES, game_on
    game_on = False
    print('board is clear')
    ROUND += 1
    LIVES += 1
    ball.hideturtle()
    paddle.hideturtle()
    game_key.write(f'ROUND {ROUND}', font=("VT323", 135, "normal"))
    left_menu.clear()
    left_menu.write(f"x{LIVES}", font=("VT323", 35, "normal"))
    screen.update()

# condition for when the all_rows is completely empty

def play():
    global game_on, LIVES, SCORE, EMPTY
    while game_on:
        if LIVES < 0:
            print(f'the score is {SCORE}')
            left_menu.clear()
            left_menu.write("GAME OVER", font=("VT323", 35, "normal"))
            game_key.goto(-220,0)
            game_key.write('GAME OVER', font=("VT323", 135, "normal"))

            if SCORE > highscores[4][1]:
                print('this guy was better')
                # screen.textinput('Enter your name', 'What is your name?')
                

# here: trying to add prompt within screen...

                def new_score(key):
                    if key == 'Return':
                        user = prompt
                        print(user)
                    else:
                        prompt.write(key, align='left', font=("VT323", 35, "normal"))
                
                # screen.onkey(new_score, "Return")
                new_score()


            highscores_table.write('High Scores', font=("VT323", 40, "underline"))

            highscores_table.goto(highscores_table.xcor(), highscores_table.ycor() - 40)
            highscores_table.write('Name', font=("VT323", 35, "normal"))
            highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
            highscores_table.write('Score', font=("VT323", 35, "normal"))

            highscores_table.goto(-50, highscores_table.ycor() - 40)
            highscores_table.write(f'{highscores[0][0]}', font=("VT323", 35, "normal"))
            highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
            highscores_table.write(f'{highscores[0][1]}', font=("VT323", 35, "normal"))

            highscores_table.goto(-50, highscores_table.ycor() - 40)
            highscores_table.write(f'{highscores[1][0]}', font=("VT323", 35, "normal"))
            highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
            highscores_table.write(f'{highscores[1][1]}', font=("VT323", 35, "normal"))

            highscores_table.goto(-50, highscores_table.ycor() - 40)
            highscores_table.write(f'{highscores[2][0]}', font=("VT323", 35, "normal"))
            highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
            highscores_table.write(f'{highscores[2][1]}', font=("VT323", 35, "normal"))

            highscores_table.goto(-50, highscores_table.ycor() - 40)
            highscores_table.write(f'{highscores[3][0]}', font=("VT323", 35, "normal"))
            highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
            highscores_table.write(f'{highscores[3][1]}', font=("VT323", 35, "normal"))

            highscores_table.goto(-50, highscores_table.ycor() - 40)
            highscores_table.write(f'{highscores[4][0]}', font=("VT323", 35, "normal"))
            highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
            highscores_table.write(f'{highscores[4][1]}', font=("VT323", 35, "normal"))

            game_on = False
            ball.hideturtle()
            paddle.hideturtle()

            for row in all_rows:
                for item in row:
                    item.clear()

            screen.update()

        else:
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
                LIVES -= 1
                if LIVES >= 0:
                    print('the whiff')
                    paddle.reset()
                    ball.reset()
                    left_menu.clear()
                    left_menu.write(f"x{LIVES}", font=("VT323", 35, "normal"))
                else:
                    left_menu.clear()
                    left_menu.write("GAME OVER", font=("VT323", 35, "normal"))
                
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
                        
                        if row == all_rows[0]:
                            ball.move_speed = ball.move_speed
                            SCORE += 1
                            right_menu.clear()
                            right_menu.write(SCORE, font=("VT323", 35, "normal"))

                        if len(row) == 0:
                            EMPTY += 1
                            print('row removed')
                            if EMPTY == 7:
                                winner()
                            
                        elif row == all_rows[1]:
                            SCORE += 2
                            right_menu.clear()
                            right_menu.write(SCORE, font=("VT323", 35, "normal"))
                            if ball.move_speed <= 0.06:
                                ball.move_speed = ball.move_speed
                            else:
                                ball.move_speed = 0.06
                        elif row == all_rows[2]:
                            SCORE += 3
                            right_menu.clear()
                            right_menu.write(SCORE, font=("VT323", 35, "normal"))
                            if ball.move_speed <= 0.05:
                                ball.move_speed = ball.move_speed
                            else:
                                ball.move_speed = 0.05
                        elif row == all_rows[3]:
                            SCORE += 4
                            right_menu.clear()
                            right_menu.write(SCORE, font=("VT323", 35, "normal"))
                            if ball.move_speed <= 0.04:
                                ball.move_speed = ball.move_speed
                            else:
                                ball.move_speed = 0.04
                        elif row == all_rows[4]:
                            SCORE += 5
                            right_menu.clear()
                            right_menu.write(SCORE, font=("VT323", 35, "normal"))
                            if ball.move_speed <= 0.03:
                                ball.move_speed = ball.move_speed
                            else:
                                ball.move_speed = 0.03
                        elif row == all_rows[5]:
                            SCORE += 6
                            right_menu.clear()
                            right_menu.write(SCORE, font=("VT323", 35, "normal"))
                            if ball.move_speed <= 0.02:
                                ball.move_speed = ball.move_speed
                            else:
                                ball.move_speed = 0.02
                        elif row == all_rows[6]:
                            SCORE += 7
                            right_menu.clear()
                            right_menu.write(SCORE, font=("VT323", 35, "normal"))
                            if ball.move_speed <= 0.01:
                                ball.move_speed = ball.move_speed
                            else:
                                ball.move_speed = 0.01
                        else:
                            print('no')


screen.mainloop()
