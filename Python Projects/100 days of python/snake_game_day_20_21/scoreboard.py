from turtle import Turtle

ALIGHMENT="center"
FONT=("Courier",20,"normal")
class Scoreboard(Turtle):

    point=0

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update_score()
    
    def update_score(self):
        arg=f"Score:{self.point}"
        self.write(arg=arg,align=ALIGHMENT,font=FONT)
        
    def increase_score(self):
        self.point+=1
        self.clear()
        self.update_score()
        
    def game_over(self):
        txt = Turtle()
        self.clear()
        text=f"GAME OVER!!\nFINAL SCORE:{self.point}"
        txt.color("white")
        txt.write(arg=text,align=ALIGHMENT,font=FONT)
        