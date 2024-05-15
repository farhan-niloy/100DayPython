from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(500*3, 400*3)
user_bet = screen.textinput("Make your bet", prompt="Which turtle will win the race?")
print(user_bet)

screen.exitonclick()
