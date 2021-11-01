from turtle import Turtle, Screen 
import random 

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput("Bet On It!!", "Enter the turtle color you think will win")
y_positions = [-70, -40, -10, 20, 50, 80]
colors = ["violet", "blue", "green", "yellow", "orange", "red"]
all_turtles = []

for turtles in range(0, 6):
    t1 = Turtle(shape="turtle")
    t1.color(colors[turtles])
    t1.penup()
    t1.goto(-200, y_positions[turtles])
    all_turtles.append(t1)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won!! Yay.. you chose the {winning_color} turtle who is the BOSS")
                is_race_on = False
            else:
                print(f"You lost!! Pfftt.. your {user_bet} turtle was demolished by {winning_color} turtle")
                is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()