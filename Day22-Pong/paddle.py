from turtle import Turtle

MOVE_DISTANCE = 10

class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=.75)
        self.goto(pos)
        self.move_direction = 0

    def go_up(self):
        self.move_direction = 1
    def go_down(self):
        self.move_direction = -1
    def stop(self):
        self.move_direction = 0

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE*self.move_direction
        x = self.xcor()
        self.goto(x, new_y)