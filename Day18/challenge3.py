from turtle import Turtle, Screen 
import random
timmy = Turtle()
colors = colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_polygon(sides):
    angle = int(360/sides)
    for i in range(sides):
        timmy.forward(100)
        timmy.left(angle)

for side in range(3, 11):
    timmy.color(random.choice(colors))
    draw_polygon(side)

