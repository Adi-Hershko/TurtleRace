from turtle import Turtle, Screen
from random import randint
import random

# Etch-A-Sketch

# t = Turtle()
s = Screen()


# def forward():
#     t.forward(15)
#
#
# def backwards():
#     t.back(15)
#
#
# def left():
#     t.left(15)
#
#
# def right():
#     t.right(15)
#
#
# def clear():
#     t.penup()
#     t.clear()
#     t.home()
#     t.pendown()
#
#
# t.pensize(10)
# t.speed(3)
# s.listen()
# s.onkey(key='w', fun=forward)
# s.onkey(key='s', fun=backwards)
# s.onkey(key='a', fun=left)
# s.onkey(key='d', fun=right)
# s.onkey(key='c', fun=clear)
# s.exitonclick()

# Turtle Race
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
s.setup(width=500, height=400)
user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
list_of_turtles = []

for i in range(len(colors)):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=-100 + i*30)
    list_of_turtles.append(t)

is_race_on = True
while is_race_on:
    for a_turtle in list_of_turtles:
        if a_turtle.xcor() >= 230:
            is_race_on = False
            if user_bet == a_turtle.pencolor():
                print(f"You've won! The {a_turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost! The {a_turtle.pencolor()} turtle is the winner!")
        a_turtle.forward(randint(0, 10))

s.exitonclick()
