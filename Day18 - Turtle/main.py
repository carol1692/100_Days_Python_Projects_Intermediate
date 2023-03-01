#! /usr/bin/env python3

import colorgram
import turtle as t
import random

t.colormode(255)
tuga = t.Turtle()
screen = t.Screen()

## work to extract the color from image and create a rgb list
color_palette = []

palette = colorgram.extract('Day18 - Turtle\src\image.jpg',12)

def create_palette_list(number):
    r = palette[number].rgb.r
    g = palette[number].rgb.g
    b = palette[number].rgb.b
    rgb = (r,g,b)
    return rgb

for num in range(len(palette)):
    color_palette.append(create_palette_list(number=num))

#chose random color from palette
def random_color(color_palette):
    color = random.choice(color_palette)
    return color

#paint line with 10 dots
def paint_dot():
    for i in range(10):
        tuga.dot(20,random_color(color_palette))
        tuga.fd(50)
        
#calculate position next line
def next_line(x,y):
    new_y_position = y + 50
    tuga.goto(x,new_y_position)
    
#####CODE EXECUTION#####
tuga.shape('arrow')
tuga.speed('fastest')
tuga.penup()
tuga.setheading(225)
tuga.fd(225)
tuga.right(225)
x = tuga.xcor()
for i in range(10):
    y = tuga.ycor()
    paint_dot()
    next_line(x,y)



#tuga.fd(50)
    #x,y_position = paint_dot()
    #print(f'x:{x}, y:{y_position}')
    #next_line(x,y_position)"""

screen.exitonclick()