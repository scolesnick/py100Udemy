# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
# Each shape is a random color
# Each side is length of 100
# all shapes overlayed onto eachother, sharing one side
# drawn in sequence

import turtle as t
import time
import random as r

tim = t.Turtle()
tim.screen.colormode(255)
# turn angle will be the same as the angle of each side
# 360 / n = a, where n is the number of sides and a is the angle

for n in range(3,11):
    tim.color((r.randint(0,255),r.randint(0,255),r.randint(0,255)))
    a = 360 / n
    for _ in range(n):
        tim.forward(100)
        tim.right(a)

time.sleep(1.5)