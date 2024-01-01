from turtle import Turtle

class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.hideturtle()
        
    def draw_rectangle(self, R, G, B):
        self.color(R, G, B)
        self.begin_fill()

        for _ in range(2):
            self.forward(80)
            self.right(90)
            self.forward(40)
            self.right(90)
        
        self.end_fill()

# test in next branch
# class Block(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape('square')
#         # self.hideturtle()
#         self.shapesize(2, 1)

#     def change_color(self, R, G, B):
#         self.color(R, G, B)
