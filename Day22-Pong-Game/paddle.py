from turtle import Turtle, Screen, position

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.goto(position)

    def go_up(self):
       self.sety(self.ycor() + 20)

    def go_down(self):
        self.sety(self.ycor() - 20)


    
