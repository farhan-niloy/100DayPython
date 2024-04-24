from turtle import Turtle, Screen
import prettytable

table = prettytable.PrettyTable()

timmy = Turtle()

my_screen = Screen()

print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(round(my_screen.canvwidth/2, 0))

print(my_screen)
print(my_screen.canvheight)
my_screen.exitonclick()