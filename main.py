

from turtle import Turtle
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
directions = [0,90,180,270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

tim.pensize(8)
tim.speed("fastest")
for _ in range(200):
    angle = random.choice(directions)
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(angle)




# ########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0,90,180,270]
#
# for _ in range(200):
#     angle = random.choice(directions)
#     color = random.choice(colours)
#     tim.pensize(8)
#     tim.pencolor(color)
#     tim.speed("fastest")
#     tim.setheading(angle)
#     tim.forward(30)





