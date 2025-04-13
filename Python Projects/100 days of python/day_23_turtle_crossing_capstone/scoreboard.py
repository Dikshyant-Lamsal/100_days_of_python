from turtle import Turtle
ALIGHMENT="center"
FONT=("Courier",15,"normal")

class Scoreboard(Turtle):
    
    level=0
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.setpos(-250,250)
        self.update_score()
        
    def update_score(self):
        self.clear()
        arg=f"Level: {self.level}"
        self.write(arg=arg,align=ALIGHMENT,font=FONT)
        
    def game_over(self):
        self.clear()
        self.setpos(0,0)
        arg=f"GAME OVER!! Final Score: {self.level}"
        self.write(arg=arg,align=ALIGHMENT,font=("Courier",20,"normal"))