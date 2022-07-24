# from turtle import *
# import prettytable
# color('red')
# bgcolor('black')
# speed(11)
# hideturtle()
# b = 0
# while b < 200:
#     right(b)
#     forward(b * 1)
#     b = b + 1
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.align = "r"
print(table)

