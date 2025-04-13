from turtle import Turtle

ALIGHMENT="center"
FONT=("Courier",20,"normal")
class Scoreboard(Turtle):
    with open("Score.txt",mode="r") as file:    
        content=file.read()
    point=0
    high_score=int(content)
    
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_score()
    
    def update_score(self):
        arg=f"Score:{self.point} High Score:{self.high_score}"
        self.write(arg=arg,align=ALIGHMENT,font=FONT)
        
    def increase_score(self):
        self.point+=1
        self.clear()
        self.update_score()
        
    def game_over(self):
        if self.point > self.high_score:
            self.high_score=self.point
        self.point=0
        
        with open("Score.txt",mode="w") as file:
            file.write(str(self.high_score))
        
        self.clear()
        self.update_score()
        
        