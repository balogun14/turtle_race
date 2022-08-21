import random
import turtle
from turtle import *
is_race_on = False
screen = Screen()
screen.title("turtle racing")
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make Your Bet", prompt="Which Turtle did you think will win : Enter a color ")
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)


if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"you\'ve won {winning_color} turtle is the winner !")

            else:
                print(f"you\'ve lost the {winning_color} turtle is the winner !")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
# tom = Turtle(shape="turtle")
# tom.penup()
# tom.goto(x=-230, y=-80)
#
# tum = Turtle(shape="turtle")
# tum.penup()
# tum.goto(x=-230, y=-40)
#
# tin = Turtle(shape="turtle")
# tin.penup()
# tin.goto(x=-230, y=40)
#
# lim = Turtle(shape="turtle")
# lim.penup()
# lim.goto(x=-230, y=60)
#
# mim = Turtle(shape="turtle")
# mim.penup()
# mim.goto(x=-230, y=90)
screen.exitonclick()
