from turtle import Turtle

SPEED = [1, 3, 6, 10]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('#FF1493')
        self.shape('circle')
        self.penup()
        self.goto(0, -200)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def drop(self):
        new_y = self.ycor() - self.y_move
        self.goto(self.xcor(), new_y)

    def bounce_y(self):
        self.y_move *= -1
    