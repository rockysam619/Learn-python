from turtle import Turtle, Screen 
import random
timmy = Turtle()
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

direction = [0, 90, 180, 270]


for _ in range(300):
    timmy.pencolor(random_color())
    timmy.speed("fastest")
    timmy.pensize(10)
    timmy.forward(20)
    timmy.setheading(random.choice(direction))