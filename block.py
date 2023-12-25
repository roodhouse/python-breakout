from turtle import Turtle

class Block(Turtle):
    # def __init__(self, color='red'):
    def __init__(self):
        super().__init__()
        self.shape('square')
        # self.draw_rectangle(color)
        
    def draw_rectangle(self, color):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.color(color)
        self.begin_fill()

        for _ in range(2):
            self.forward(20)
            self.right(90)
            self.forward(10)
            self.right(90)
        
        self.end_fill()