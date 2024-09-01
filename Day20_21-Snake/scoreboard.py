from turtle import Turtle
FONT = 'Courier'
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,260)
        self.score = 0
        self.print()

    def print(self):
        text = f'Score: {self.score}'
        self.write(arg=text, align=ALIGNMENT, font=(FONT, 24, 'normal'))

    def game_over(self):
        text = 'GAME OVER'
        self.goto(0,0)
        self.write(arg=text, align=ALIGNMENT, font=(FONT, 24, 'normal'))

    def update(self):
        self.score += 1
        self.clear()
        self.print()