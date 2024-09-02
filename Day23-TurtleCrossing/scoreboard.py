from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-200, 250)
        self.level = 1
        self.print()

    def print(self):
        text = f'Level: {self.level}'
        self.write(arg=text, align=ALIGNMENT, font=FONT)

    def game_over(self):
        text = 'GAME OVER'
        self.goto(0,0)
        self.write(arg=text, align=ALIGNMENT, font=FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.print()