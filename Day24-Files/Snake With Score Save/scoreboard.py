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
        self.high_score = 0
        self.get_high()
        self.print()

    def get_high(self):
        with open(file='highscore.txt') as file:
            val = file.read()
        self.high_score = int(val)

    def print(self):
        self.clear()
        text = f'Score: {self.score} High Score: {self.high_score}'
        self.write(arg=text, align=ALIGNMENT, font=(FONT, 24, 'normal'))

    # def game_over(self):
    #     text = 'GAME OVER'
    #     self.goto(0,0)
    #     self.write(arg=text, align=ALIGNMENT, font=(FONT, 24, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file='highscore.txt', mode='w') as file:
                file.write(str(self.score))
        self.score = 0
        self.print()

    def update(self):
        self.score += 1
        self.print()