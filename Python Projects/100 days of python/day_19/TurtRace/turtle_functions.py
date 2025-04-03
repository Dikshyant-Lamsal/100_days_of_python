from turtle import Turtle, Screen
import random

class TurtFunctions:
    
    def __init__(self,x_cor,y_cor,color):
        self.c=color
        self.t_name = Turtle()
        self.t_name.penup()
        self.t_name.shape('turtle')
        self.t_name.color(color)
        self.t_name.goto(x_cor,y_cor)
    
    def run(self,value):
        self.t_name.forward(value)
    
    def check_coords(self):
        if self.t_name.xcor()>=220:
            return True
        return False
        
       
    