from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align = "center" , font = ("Courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align = "center" , font = ("Courier", 40, "normal"))

    def l_score(self):
        self.lscore += 1
        self.update_scoreboard()

    def r_score(self):
        self.rscore += 1
        self.update_scoreboard()