from turtle import Turtle, Screen
import random
import turtle

ran = random.randint(1, 2)

def ran_return():
    if(ran == 1):
        return True
    else:
        return False


direction = ran_return()

screen = Screen()

forward = 0

while screen.exitonclick:
    turtle.forward(forward)
    forward += 1
    if direction:
        turtle.right(90)
    else:
        turtle.right(90)



















