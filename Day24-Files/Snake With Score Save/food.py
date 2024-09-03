from turtle import Turtle
import random

BOUNDARY = 270

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=.5,stretch_len=.5)
        self.color('blue')
        self.speed('fastest')
        random_x = random.randint(-BOUNDARY,BOUNDARY)
        random_y = random.randint(-BOUNDARY, BOUNDARY)
        self.goto(random_x,random_y)

    def refresh(self):
        random_x = random.randint(-BOUNDARY, BOUNDARY)
        random_y = random.randint(-BOUNDARY, BOUNDARY)
        self.goto(random_x, random_y)