from turtle import Turtle,Screen

ALIGHMENT="center"
FONT=("Courier",50,"normal")
MAX_POINTS=10

class Scoreboard(Turtle):

    l_point=0
    r_point=0
    winner=""
    s=Screen()

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,200)
        self.update_score()
    
    def update_score(self):
        arg=f"{self.l_point}    {self.r_point}"
        self.write(arg=arg,align=ALIGHMENT,font=FONT)
        
        
    def increase_score(self,paddle):
        if paddle.lower()=='left':
            self.l_point+=1
        elif paddle.lower()=='right':
            self.r_point+=1
        self.clear()
        self.update_score()
    
    def is_game_over(self):
        if self.l_point>=MAX_POINTS or self.r_point>=MAX_POINTS:
            if self.l_point>self.r_point:
                self.winner="LEFT"
            else:
                self.winner="RIGHT"
            return True
        return False
    
    def game_over(self):
        txt = Turtle()
        self.clear()
        text=f"GAME OVER!! Winner:{self.winner}"
        self.update_score()
        txt.color("white")
        txt.write(arg=text,align=ALIGHMENT,font=FONT)
        