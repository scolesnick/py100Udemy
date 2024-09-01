#draw a spirograph

import turtle as t
import time
import random as rand

def changeColor():
    r = rand.randint(0,255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    return (r,g,b)

tim = t.Turtle()
tim.screen.colormode(255)
tim.speed(10)

radius = 100
angle = 45
rotations = int(360 / angle)

for _ in range(rotations):
    tim.color(changeColor())
    tim.right(angle)
    tim.circle(radius)

time.sleep(1.5)