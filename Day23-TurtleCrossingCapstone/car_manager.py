from turtle import Turtle
import random as rand

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_CARS = 4


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_rate = 6
        self.fill_board()

    def fill_board(self):
        for c in range(STARTING_CARS):
            self.create_car()
        for car in self.cars:
            new_x = rand.randint(-250,250)
            new_y = car.ycor()
            car.goto(x=new_x,y=new_y)

    def create_car(self):
        car = Turtle(shape='square')
        car.color(rand.choice(COLORS))
        car.penup()
        car.setheading(180)
        car.shapesize(stretch_wid=1,stretch_len=2)
        x_start = 300
        y_start = rand.randint(-260,260)
        car.goto(x=x_start, y=y_start)
        self.cars.append(car)

    def move_cars(self):
        for i in range(len(self.cars)):
            new_x = self.cars[i].xcor() - MOVE_INCREMENT
            new_y = self.cars[i].ycor()
            self.cars[i].goto(x=new_x, y=new_y)

    def car_generator(self):
        num = rand.randint(1,6)
        if num == 1:
            self.create_car()

    def check_collision(self, x, y):
        for c in self.cars:
            if c.xcor() + 30 > x > c.xcor() - 30 and c.ycor() + 20 > y > c.ycor() - 20:
                return True
        return False