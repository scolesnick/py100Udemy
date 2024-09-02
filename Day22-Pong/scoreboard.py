from turtle import Turtle
FONT = 'Courier'
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.print()

    def print(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=str(self.l_score), align=ALIGNMENT, font=(FONT, 80, 'normal'))
        self.goto(100, 200)
        self.write(arg=str(self.r_score), align=ALIGNMENT, font=(FONT, 80, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.print()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.print()