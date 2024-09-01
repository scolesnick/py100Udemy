import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ['red','orange','yellow','blue','green', 'purple']

turtles = []

for c in colors:
    t = Turtle(shape='turtle')
    t.penup()
    t.color(c)
    y_pos = colors.index(c)*30-75
    t.goto(x=-230,y=y_pos)
    turtles.append(t)

if user_bet:
    is_race_on = True

# Turtles will move a random amount of spaces at a time, from 0 to 10 spaces
while is_race_on:

    for turt in turtles:
        if turt.xcor() > 230:
            winning_color = turt.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost. The {winning_color} turtle is the winner.")
            is_race_on = False
            break
        else:
            rand_distance = random.randint(0,10)
            turt.forward(rand_distance)

screen.exitonclick()