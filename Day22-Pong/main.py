import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

p1 = Paddle((-350,0))
p2 = Paddle((350,0))
b = Ball()
scoreboard = Scoreboard()
screen.update()
game_is_on = True

screen.listen()
screen.onkeypress(fun=p1.go_up,key='w')
screen.onkeypress(fun=p1.go_down, key='s')
screen.onkeyrelease(fun=p1.stop, key='w')
screen.onkeyrelease(fun=p1.stop, key='s')

screen.onkeypress(fun=p2.go_up,key='Up')
screen.onkeypress(fun=p2.go_down, key='Down')
screen.onkeyrelease(fun=p2.stop, key='Up')
screen.onkeyrelease(fun=p2.stop, key='Down')

while game_is_on:
    screen.update()
    time.sleep(b.move_speed)
    p1.move()
    p2.move()
    b.paddle_collision(p1)
    b.paddle_collision(p2)
    b.move()

    if b.xcor() > 390:
        print('Left Side Wins!')
        time.sleep(1)
        b.restart()
        scoreboard.l_point()
    elif b.xcor() < -390:
        print('Right Side Wins!')
        time.sleep(1)
        b.restart()
        scoreboard.r_point()

screen.exitonclick()