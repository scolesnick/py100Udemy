# from turtle import Turtle, Screen
# # import another_module as am
#
# # print(am.another_variable)
#
# timmy = Turtle()
# my_screen = Screen()
#
# timmy.shape("turtle")
# timmy.color("chartreuse")
# timmy.forward(100)
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"], "c")
table.add_column("Type", ["Electric","Water","Fire"], "c")

table.align = "l"

print(table)