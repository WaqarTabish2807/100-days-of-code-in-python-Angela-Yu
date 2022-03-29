import random
from tkinter import Y
from turtle import Turtle, Screen
import turtle 

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0,6):
    shiw = Turtle(shape="turtle")
    shiw.color(colors[turtle_index])
    shiw.penup()
    shiw.goto(x=-230, y= y_positions[turtle_index])
    all_turtles.append(shiw)

if user_bet: 
    is_race_on = True

while is_race_on: 
    for turtle in all_turtles: 
        if turtle.xcor() > 220: 
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else: 
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()