from turtle import Turtle,Screen

class TurtleFunctions(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.scr = Screen()
        self.shape("turtle")
        self.setpos(x=0,y=-280)
        self.setheading(90)
        self.scr.listen()
        self.screen.onkeypress(key="w",fun=self.move_up)
        self.screen.onkeypress(key="Up",fun=self.move_up)
        self.screen.onkeypress(key="s",fun=self.move_down)
        self.screen.onkeypress(key="Down",fun=self.move_down)
        
        
    def move_up(self):
        self.forward(10)
    
    def move_down(self):
        self.backward(10)