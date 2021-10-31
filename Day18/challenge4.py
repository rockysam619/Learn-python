from turtle import Turtle, Screen 
import random
timmy = Turtle()
colors = colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]


for _ in range(300):
    timmy.color(random.choice(colors))
    timmy.speed("fastest")
    timmy.pensize(10)
    timmy.forward(20)
    timmy.setheading(random.choice(direction))