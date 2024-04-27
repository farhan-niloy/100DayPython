from turtle import Turtle, Screen
import random

screen = Screen()

screen.exitonclick


tim = Turtle()

colors = ["black", "red", "green", "blue", "cyan", "magenta", "yellow", "orange", "purple", "brown", "gray", "pink", "turquoise", "gold"]

direction = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random.choice(colors))  # Use color() method to set pen color
    tim.forward(30)
    tim.setheading(random.choice(direction))  # Choose a random direction from the direction list
    tim.speed("fastest")
    tim.width(10)

