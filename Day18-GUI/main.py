import turtle as t
from turtle import Turtle, Screen
import random
timmy = Turtle()
t.colormode(255)
# timmy.pensize(5)
timmy.speed("fastest")
direction = [0, 90, 180, 270]
screen = t.Screen()
screen.bgcolor("black")



# Random Color function
def random_color():
    """This function generate and return different RGB color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# Different Shapes
# for i in range(3, 11):
#     for j in range(i):
#         timmy.color(random_color())
#         timmy.forward(100)
#         timmy.right(360/i)

# Random Walk
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))


# Circles
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(2)

screen.exitonclick()