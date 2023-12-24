# welcome screen
    # graphic header
    # play button
    # high score button

# game screen
    # current lives
    # current score
    # pause button
    # sound on/off button
    # game board
        # blocks
        # ball
        # bar

# game over screen
    # graphic header
    # score
    # enter iniitals to save high score
    # high scores 
    # play again

from turtle import Turtle, Screen
from introScreen.intro_screen import Intro_Screen

screen = Screen()

screen.setup(width=1200, height=900)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)
screen.listen()


intro = Intro_Screen()



screen.exitonclick()