from turtle import Turtle, Screen

class TurtFunctions:
    
    def __init__(self):
        self.t_name = Turtle()
        self.s_name= Screen()
        self.s_name.listen()
        self.s_name.onkey(key="w",fun=self.move_frwrd)
        self.s_name.onkey(key="s",fun=self.move_bckwrd)
        self.s_name.onkey(key="a",fun=self.turn_left)
        self.s_name.onkey(key="d",fun=self.turn_right)
        self.s_name.onkey(key="c",fun=self.clear_drawing)
        self.s_name.exitonclick()
        
    def move_frwrd(self):
        self.t_name.forward(10)
    
    def move_bckwrd(self):
        self.t_name.backward(10)
        
    def turn_right(self):
        self.t_name.right(10)
    
    def turn_left(self):
        self.t_name.left(10)
    
    def clear_drawing(self):
        self.t_name.reset()
    
    