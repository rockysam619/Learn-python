import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(width = 800, height = 600)
screen.tracer(0)

r_paddle = Paddle((355, 0))
l_paddle = Paddle((-355, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_running = True
while game_is_running:
    time.sleep(ball.move_speed)
    ball.move() 
    screen.update()

    #Collision detection
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    #Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    #Collision with left wall
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score()   
        
    #Collision with right wall
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score()

screen.exitonclick()