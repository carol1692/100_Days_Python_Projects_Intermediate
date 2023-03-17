#! usr/ben/env python3

from turtle import Turtle, Screen
from random import randint

is_race_on = False
tuga = Turtle()
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bet', prompt='which turtle will win the race? Enter a color: ')
colors = ['red','orange','yellow','green','blue','purple']
position = [ 150, 100, 50, 0, -50, -100]
all_turtles = []


def createcompetitor(color, y_position):
    new_tuga = Turtle(shape='turtle')
    new_tuga.color(color)
    new_tuga.penup()
    new_tuga.goto(x=-200,y=y_position)
    all_turtles.append(new_tuga)

for contador in range(len(position)):
    createcompetitor(colors[contador], position[contador])
    print(all_turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:    
        if turtle.xcor() > 220:
            winning_color = turtle.pencolor() 
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
                is_race_on = False
            else:
                print(f"You've lost! The {winning_color} turtle is the winner ")
                is_race_on = False

        random_distance = randint(0,10)
        turtle.forward(random_distance)   




screen.exitonclick()