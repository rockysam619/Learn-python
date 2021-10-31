from turtle import Turtle, Screen 
import random
timmy = Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

screen = Screen()
screen.colormode(255)

color_list = [(108, 110, 127), (214, 153, 89), (140, 141, 152), (196, 59, 24), (227, 214, 103), (234, 217, 226), (225, 235, 227), (180, 159, 39), (99, 108, 177), (211, 145, 178), (29, 46, 27), (27, 26, 70), (199, 18, 5), (37, 40, 18), (227, 167, 198), (221, 81, 52), (43, 45, 106), (126, 84, 96), (217, 75, 99), (232, 173, 161), (87, 100, 90), (182, 184, 213), (188, 14, 21), (153, 165, 157), (222, 206, 23), (48, 27, 50), (73, 72, 38), (51, 72, 53)]

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for dot_count in range(1, 101):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    if dot_count%10 == 0:        
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen.exitonclick()