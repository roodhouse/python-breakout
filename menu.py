from turtle import Turtle

class MenuItem(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape('square')
        self.color('#FF1493')