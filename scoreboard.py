from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.goto(0, 270)
        self.score= 0 
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align= "center", font=("Comic Sans MS", 20, "normal"))
        


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", align= "center", font=("Comic Sans MS", 20, "normal"))