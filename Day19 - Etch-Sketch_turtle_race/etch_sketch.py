#! usr/bin/env python3

from turtle import Turtle, Screen 

tuga = Turtle()
screen = Screen()


def move_forwards():
    tuga.forward(10)

def move_backwards():
    tuga.backward(10)

def move_counter_clockwise():
    tuga.left(25)
    
def move_clockwise():
    tuga.right(25)
    
def move_clear():
    screen.resetscreen()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=move_counter_clockwise)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='c', fun=move_clear)
screen.exitonclick()