import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
cars = CarManager()
scoreboard = Scoreboard()
scoreboard.print()

screen.listen()
screen.onkeypress(fun=player.move, key='w')

sleep_time = 0.1
time_increase = 0.8
game_is_on = True
while game_is_on:
    time.sleep(sleep_time)

    # Generate and move cars
    cars.car_generator()
    cars.move_cars()

    # Check if turtle reached finish line
    if player.finish():
        scoreboard.update()
        player.reset_pos()
        sleep_time *= time_increase

    # Check if turtle collided with car
    if cars.check_collision(player.xcor(), player.ycor()):
        game_is_on = False
        scoreboard.game_over()


    screen.update()


screen.exitonclick()