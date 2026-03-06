from turtle import Turtle,Screen

class Paddle(Turtle):
    scr=Screen()
    def __init__(self,side,color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
       
        if side.lower()=="right":
            self.setpos(350,0)
            self.scr.listen()
            self.scr.onkeypress(key="Up",fun=self.go_up)
            self.scr.onkeypress(key="Down",fun=self.go_down)
        else:
            self.setpos(-350,0)
            self.scr.listen()
            self.scr.onkeypress(key="w",fun=self.go_up)
            self.scr.onkeypress(key="s",fun=self.go_down)
            self.scr.onkeypress(key="W",fun=self.go_up)
            self.scr.onkeypress(key="S",fun=self.go_down)
    
    def go_up(self):
        self.goto(self.xcor(),self.ycor()+20)
    
    def go_down(self):
        self.goto(self.xcor(),self.ycor()-20)
        
    def out_of_bounds(self):
        return self.ycor()>=290 or self.ycor()<=-290