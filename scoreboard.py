from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 18, "normal")
FONT2 = ("Arial", 18, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        with open("high_score.txt") as read_highscore:
            self.high_score = int(read_highscore.read())
        self.goto(0, 230)
        self.pencolor("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move= False, align= ALIGMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode= "w") as highscore:
                highscore.write(str(self.high_score))
        self.score = 0
        self.update_score()


    def game_over(self):
        self.goto(0, 0)
        self.write("G A M E  O V E R", move= False, align=ALIGMENT, font= FONT)
