from turtle import Turtle

class Intro_Screen(Turtle):
    def __init__(self):
        super().__init__()
        self.title()
        self.play_button()

    def title(self):
        padding = 10
        text = 'Welcome'
        text_font = ('Arial', 24, 'normal')
        text_color = 'white'

        screen = self.getscreen()
        text_width = screen.canvwidth
        print(text_width)
        text_height = screen.canvheight * 0.15

        # Calculate the box dimensions
        box_width = text_width + 2 * padding
        box_height = text_height + 2 * padding

        # Position the turtle and draw the box
        self.penup()
        self.hideturtle()
        self.goto(-box_width / 2, -box_height / 2)
        self.pendown()
        self.color('red')
        self.begin_fill()
        for _ in range(2):
            self.forward(box_width)
            self.left(90)
            self.forward(box_height)
            self.left(90)
        self.end_fill()
        self.penup()

        # Write the text on top of the box
        self.goto(0, 0)
        self.color(text_color)
        self.write(text, align='center', font=text_font)

    def play_button(self):
        self.penup()
        self.hideturtle()
        self.goto(300, 0)
        self.color('white')
        self.write('Play now', align='center', font=('Arial', 24, 'normal'))

