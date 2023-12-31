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
        self.move_speed = 0.07

    def drop(self):
        new_y = self.ycor() - self.y_move
        new_x = self.xcor() - self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def wall_hit(self):
        self.x_move *= -1
    
    def reset(self):
        self.goto(0, -200)
        self.move_speed = 0.07
        # self.drop()
    