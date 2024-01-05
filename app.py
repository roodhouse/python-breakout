from turtle import Screen
from menu import MenuItem
from block import Block
from paddle import Paddle
from ball import Ball
import time
import csv
from functools import partial

screen = Screen()

screen.setup(width=1250, height=950)
screen.bgcolor("black")
screen.colormode(255)
screen.title("Breakout")
screen.tracer(0)
screen.listen()

highscores = []

with open('highscore.csv', 'r') as f:
        reader = csv.reader(f)
        print(f'the reader is: {reader}')
        for row in reader:
            highscores.append(row)

for high in highscores:
        high[1] = int(high[1])

highscores = sorted(highscores, key=lambda x: x[1], reverse=True)


LIVES = 4
SCORE = 0
TITLE = "BREAKOUT"
EMPTY = 0
ROUND = 1
USER = ''
game_on = False
GAME = 1
max_chars = 3
chars_entered = 0

def new_guy():
    global chars_entered
    chars_entered = 0
    new_entry = [USER, SCORE]
    print(f'high scores in new guy before pop: {highscores}')
    highscores.pop()
    print(f'high scores in new guy after pop: {highscores}')
    highscores.append(new_entry)
    print(f'high scores in new guy after append: {highscores}')
    
    with open('highscore.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(highscores)
    
    update_highscores()

    screen.onkeypress(None)
    screen.onkey(new_start, 'space')

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
highscores_table.goto(-75, 100)

def update_highscores():
    global highscores
    highscores = sorted(highscores, key=lambda x: x[1], reverse=True)

    highscores_table.clear()
    highscores_table.goto(-75, 100)

    print(highscores)

    highscores_table.write('High Scores', font=("VT323", 40, "underline"))

    highscores_table.goto(-60, highscores_table.ycor() - 40)
    highscores_table.write(f'{highscores[0][0]}', font=("VT323", 35, "normal"))
    highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
    highscores_table.write(f'{highscores[0][1]}', font=("VT323", 35, "normal"))

    highscores_table.goto(-60, highscores_table.ycor() - 40)
    highscores_table.write(f'{highscores[1][0]}', font=("VT323", 35, "normal"))
    highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
    highscores_table.write(f'{highscores[1][1]}', font=("VT323", 35, "normal"))

    highscores_table.goto(-60, highscores_table.ycor() - 40)
    highscores_table.write(f'{highscores[2][0]}', font=("VT323", 35, "normal"))
    highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
    highscores_table.write(f'{highscores[2][1]}', font=("VT323", 35, "normal"))

    highscores_table.goto(-60, highscores_table.ycor() - 40)
    highscores_table.write(f'{highscores[3][0]}', font=("VT323", 35, "normal"))
    highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
    highscores_table.write(f'{highscores[3][1]}', font=("VT323", 35, "normal"))

    highscores_table.goto(-60, highscores_table.ycor() - 40)
    highscores_table.write(f'{highscores[4][0]}', font=("VT323", 35, "normal"))
    highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
    highscores_table.write(f'{highscores[4][1]}', font=("VT323", 35, "normal"))
    
    screen.update()

highscores_table.clear()

prompt = MenuItem()
prompt.goto(-110, -200)

initials = MenuItem()
initials.goto(-20, -360)

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
    print('back row from create board')
    print(back_row)
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

def kill_space():
    print('killed space')

def new_start():
    global ROUND, game_on, game_key, LIVES, SCORE, back_row, row_four, row_three, row_two, row_one, row_zero, row_neg, GAME, USER
    ROUND = 1
    LIVES = 4
    SCORE = 0
    GAME += 1
    USER = ''
    print('new start')
    game_key.clear()
    highscores_table.clear()
    prompt.clear()
    initials.clear()
    game_key.goto(-150,0)
    game_key.write(f'ROUND {ROUND}', font=("VT323", 135, "normal"))
    left_menu.clear()
    right_menu.clear()
    left_menu.write(f"x{LIVES}", font=("VT323", 35, "normal"))
    right_menu.write(f"{SCORE}", font=("VT323", 35, "normal"))
    back_row = []
    row_four = []
    row_three = []
    row_two = []
    row_one = []
    row_zero = []
    row_neg = []
    game_on = False
    screen.onkey(start, 'space')

def play():
    global game_on, LIVES, SCORE, EMPTY, USER, max_chars, chars_entered, GAME
    while game_on:
        if LIVES < 0:
            screen.onkey(kill_space, 'space')
            left_menu.clear()
            left_menu.write("GAME OVER", font=("VT323", 35, "normal"))
            game_key.goto(-220,200)
            game_key.write('GAME OVER', font=("VT323", 135, "normal"))

            def _onkeypress(self, fun, key=None):
                    if fun is None:
                        if key is None:
                            self.cv.unbind("<KeyPress>", None)
                        else:
                            self.cv.unbind("<KeyPress-%s>" % key, None)
                    elif key is None:
                        def eventfun(event):
                            fun(event.char)
                        self.cv.bind("<KeyPress>", eventfun)
                    else:
                        def eventfun(event):
                            fun()
                        self.cv.bind("<KeyPress-%s>" % key, eventfun)

            def letter(character):
                    global USER, max_chars, chars_entered
                    print(f'chars_entereda: {chars_entered}')
                    chars_entered += 1
                    print(f'chars_entereda: {chars_entered}')
                    if chars_entered <= max_chars:
                        initials.write(character, move=True, font=("VT323", 35, 'normal'))
                        USER = USER + character
                        screen.onkey(new_guy, 'Return')
                    else:
                        print('no more')

            if SCORE > highscores[4][1]:
                if GAME > 1:
                    prompt.goto(-110, -200) 
                    prompt.write('It is wonderful!', font=("VT323", 35, 'normal'))
                    prompt.goto(-265, -240)
                    prompt.write('You have achieved a top 5 high score.', font=("VT323", 35, 'normal'))
                    prompt.goto(-265, -280)
                    prompt.write('Enter your initials and press return.', font=("VT323", 35, 'normal'))
                    
                else:
                    prompt.write('It is wonderful!', font=("VT323", 35, 'normal'))
                    prompt.goto(-265, -240)
                    prompt.write('You have achieved a top 5 high score.', font=("VT323", 35, 'normal'))
                    prompt.goto(-265, -280)
                    prompt.write('Enter your initials and press return.', font=("VT323", 35, 'normal'))

                screen._onkeypress = partial(_onkeypress, screen)
                screen.onkeypress(letter)
            
            if GAME > 1:
                highscores_table.clear()
                highscores_table.goto(-75, 100)
                highscores_table.write('High Scores', font=("VT323", 40, "underline"))

                highscores_table.goto(-60, highscores_table.ycor() - 40)
                highscores_table.write(f'{highscores[0][0]}', font=("VT323", 35, "normal"))
                highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
                highscores_table.write(f'{highscores[0][1]}', font=("VT323", 35, "normal"))

                highscores_table.goto(-60, highscores_table.ycor() - 40)
                highscores_table.write(f'{highscores[1][0]}', font=("VT323", 35, "normal"))
                highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
                highscores_table.write(f'{highscores[1][1]}', font=("VT323", 35, "normal"))

                highscores_table.goto(-60, highscores_table.ycor() - 40)
                highscores_table.write(f'{highscores[2][0]}', font=("VT323", 35, "normal"))
                highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
                highscores_table.write(f'{highscores[2][1]}', font=("VT323", 35, "normal"))

                highscores_table.goto(-60, highscores_table.ycor() - 40)
                highscores_table.write(f'{highscores[3][0]}', font=("VT323", 35, "normal"))
                highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
                highscores_table.write(f'{highscores[3][1]}', font=("VT323", 35, "normal"))

                highscores_table.goto(-60, highscores_table.ycor() - 40)
                highscores_table.write(f'{highscores[4][0]}', font=("VT323", 35, "normal"))
                highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
                highscores_table.write(f'{highscores[4][1]}', font=("VT323", 35, "normal"))
            else:
                highscores_table.write('High Scores', font=("VT323", 40, "underline"))

                highscores_table.goto(-60, highscores_table.ycor() - 40)
                highscores_table.write(f'{highscores[0][0]}', font=("VT323", 35, "normal"))
                highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
                highscores_table.write(f'{highscores[0][1]}', font=("VT323", 35, "normal"))

                highscores_table.goto(-60, highscores_table.ycor() - 40)
                highscores_table.write(f'{highscores[1][0]}', font=("VT323", 35, "normal"))
                highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
                highscores_table.write(f'{highscores[1][1]}', font=("VT323", 35, "normal"))

                highscores_table.goto(-60, highscores_table.ycor() - 40)
                highscores_table.write(f'{highscores[2][0]}', font=("VT323", 35, "normal"))
                highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
                highscores_table.write(f'{highscores[2][1]}', font=("VT323", 35, "normal"))

                highscores_table.goto(-60, highscores_table.ycor() - 40)
                highscores_table.write(f'{highscores[3][0]}', font=("VT323", 35, "normal"))
                highscores_table.goto(highscores_table.xcor() + 100, highscores_table.ycor())
                highscores_table.write(f'{highscores[3][1]}', font=("VT323", 35, "normal"))

                highscores_table.goto(-60, highscores_table.ycor() - 40)
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
