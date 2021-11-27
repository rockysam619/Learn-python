import time
from turtle import Screen, Turtle
from snake import Snake 

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_points = [(-40, 0), (-20, 0), (0, 0)]
segment = []

snake = Snake()
screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_running = True
while game_is_running:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

screen.exitonclick()