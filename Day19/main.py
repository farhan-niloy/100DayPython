from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10);

def move_backward():
    tim.backward(10);

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_forward, "s")
screen.onkey(move_forward, "a")
screen.onkey(move_forward, "d")

screen.exitonclick()
