from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('#FF1493')
        self.goto(0, -350)
        self.shapesize(stretch_len=15.0, stretch_wid=1.0)
    
    def move_right(self):
        new_right = self.xcor() + 80
        self.goto(new_right, self.ycor())
        
    def move_left(self):
        new_left = self.xcor() - 80
        self.goto(new_left, self.ycor())
    
    def reset(self):
        self.goto(0, -350)