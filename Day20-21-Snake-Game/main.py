import time
from turtle import Screen, Turtle
from snake import Snake 
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_points = [(-40, 0), (-20, 0), (0, 0)]
segment = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.inc_score()
        snake.extend_snake()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_running = False
        scoreboard.game_over()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_is_running = False
            scoreboard.game_over()

screen.exitonclick()