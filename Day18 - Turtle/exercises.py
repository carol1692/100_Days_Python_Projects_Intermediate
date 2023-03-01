#! /usr/bin/env/ python3
import turtle as t 
import random

t.colormode(255)
turt = t.Turtle()
turt.shape('arrow')


points = [3,4,5,6,8,9,10]
coordenates = [0,90,180,270]
colors = ['aquamarine2','DeepPink2','green3','salmon','light sea green','MistyRose2','dark orchid']

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r, g, b)
    return rgb

turt.speed('fastest')
turt.pensize(1)
## drawn spirals with random colors w/ no static colors list
def draw_spiro(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turt.circle(80)
        turt.color(random_color())
        turt.heading()
        turt.right(size_of_gap)
        turt.heading()

draw_spiro(5)

'''## random directions with random colors w/ no static colors list
for run in points:
    turt.pensize(10)
    for _ in range(50):
        turt.color(random_color())
        turt.forward(30)
        turt.setheading(random.choice(coordenates))
        turt.forward(30)'''

'''## random directions with random colors and pensize larger when use this code deactivate colormode
for run in points:
    turt.color(random.choice(colors))
    turt.pensize(10)
    for _ in range(50):
        turt.forward(30)
        turt.setheading(random.choice(coordenates))
        turt.forward(30)'''

## random formats with random colors        
'''for run in points:
    angle = 360/run
    turt.color(random.choice(colors))
    for _ in range(run):
        turt.forward(30)
        turt.right(angle)
        turt.forward(30)
'''        
screen = t.Screen()
screen.exitonclick()