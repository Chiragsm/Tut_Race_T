from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.title("Turtle Race")
user_in = screen.textinput(title="Make your bet", prompt="Which color will win")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_tur = Turtle(shape="turtle")
    new_tur.color(colors[turtle_index])
    new_tur.penup()
    new_tur.goto(x=-280, y=y_pos[turtle_index])
    all_turtles.append(new_tur)

if user_in:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 250:
            is_race_on = False
            winning_c = turtle.pencolor()

            if winning_c == user_in:
                print(f"You won ! {winning_c} is the winning color")
            else:
                print(f"You loose! {winning_c} is the winning color")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
