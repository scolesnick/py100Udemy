'''
 Use Turtle to create an etch a sketch

 req.
 W=Forwards
 S=Backwards
 A=Counter-Clockwise
 D=Clockwise
 C=Clear Drawing
'''

import turtle as t

screen = t.Screen()
tim = t.Turtle()

def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def clockwise():
    tim.right(10)
def cclockwise():
    tim.left(10)
def clear_screen():
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=clockwise, key='d')
screen.onkey(fun=cclockwise, key='a')
screen.onkey(fun=clear_screen, key='c')
screen.exitonclick()