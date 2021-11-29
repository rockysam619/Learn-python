from turtle import Turtle
STARTING_POINTS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segment = []
        self.draw_snake()
        self.head = self.segment[0]

    def draw_snake(self):
        for _ in STARTING_POINTS:
            self.add_segment(_)

    def add_segment(self, position):
        new_seg = Turtle(shape = "square")
        new_seg.color("white")
        new_seg.speed("fastest")
        new_seg.penup()
        new_seg.goto(position)
        self.segment.append(new_seg)

    def extend_snake(self):
        self.add_segment(self.segment[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segment) -1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def up(self):     
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)