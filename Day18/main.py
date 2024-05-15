import turtle as t 

import random

turtle = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

turtle.color(random_color())  # Set initial color
turtle.circle(100)
current_heading = turtle.heading()
turtle.setheading(current_heading+10)

screen = t.Screen()
screen.exitonclick()

