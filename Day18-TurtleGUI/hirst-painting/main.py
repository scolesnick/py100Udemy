'''
This challenge creates a dot painting, like those made by Damien Hirst.
It collects color samples from a Hirst painting and uses them to create a new one.

req.
The painting must have 10x10 dots
The dots should be r=10, spaced apart by 50
'''


#Req
DOT_SIZE = 20.0
SPACING = 50.0
MARGIN = SPACING/2
DOT_X_COUNT = 10.0
DOT_Y_COUNT = 10.0
SCREEN_WIDTH = DOT_X_COUNT * SPACING
SCREEN_HEIGHT = DOT_Y_COUNT * SPACING

import colorgram
import turtle as t
import time
import random as rand

# Grab Colors
colors = colorgram.extract('image.jpg',30)
col_list = []
for c in colors:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    col_list.append((r,g,b))


#Turtle Setup
tim = t.Turtle()
tim.penup()
tim.speed(9)

#Screen Setup
tim.screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
tim.screen.colormode(255)
start_pos_x = -SCREEN_WIDTH/2
start_pos_y = -SCREEN_HEIGHT/2
tim.setposition(start_pos_x, start_pos_y)
end_position = (SCREEN_WIDTH, SCREEN_HEIGHT)


#Move and place random dots until the turtle has reached the end position
y_pos = int(tim.pos()[1])
while y_pos < SCREEN_HEIGHT/2-SPACING:
    tim.dot(20, rand.choice(col_list))
    x_pos = int(tim.pos()[0])
    y_pos = int(tim.pos()[1])
    while x_pos < SCREEN_WIDTH/2-SPACING:
        tim.forward(SPACING)
        tim.dot(20,rand.choice(col_list))
        x_pos = int(tim.pos()[0])
    tim.goto(start_pos_x, y_pos+SPACING)
