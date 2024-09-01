#Draw a random walk
#each walk uses a different color
#speed up the turtle
#increase the thickness of the lines drawn
import time
import turtle as t
import random as rand

def changeColor():
    r = rand.randint(0,255)
    g = rand.randint(0, 255)
    b = rand.randint(0, 255)
    return (r,g,b)

def randRotate():
    r = rand.randint(1,4)
    return r*90

tim = t.Turtle()
tim.screen.colormode(255)
tim.width(10)
tim.speed(0)

steps = 150

for _ in range(steps):
    tim.color(changeColor())
    tim.forward(50)
    tim.right(randRotate())

time.sleep(2)