from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(500*2, 400*2)
user_bet = screen.textinput("Make your bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x = -230*2, y = y_position[turtle_index]*2)

screen.exitonclick()
