from turtle import Turtle

ALIGNMENT = "center"
FONT = "courier"
FONT_SIZE = 15



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            highscore = int(file.read())
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.highscore = highscore
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(
            f"SCORE : {self.score} HIGH SCORE : {self.highscore} ",
            move=False,
            align="center",
            font=(FONT, FONT_SIZE, "normal"),
        )

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            
            with open("data.txt",mode = "w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update()
        
