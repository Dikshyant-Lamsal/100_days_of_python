from turtle import Turtle,Screen
import time

class Snake:
    t_list=[]
    x_cor=0
    
    def __init__(self):
        self.create_initial_snake()

    def create_initial_snake(self):
        for _ in range(3):
            self.t_name = Turtle(shape='square')
            self.t_name.color('white')
            self.t_name.penup()
            self.t_name.goto(self.x_cor,0)
            self.t_list.append(self.t_name)
            self.x_cor-=20
            
    def move_forward(self,speed):
        for seg_num in range(len(self.t_list)-1,0,-1):
            self.t_list[seg_num].goto(self.t_list[seg_num-1].xcor(),self.t_list[seg_num-1].ycor())
        self.t_list[0].forward(speed) 
    
    def turn_left(self):
        for seg_num in range(len(self.t_list)-1,0,-1):
            self.t_list[seg_num].goto(self.t_list[seg_num-1].xcor(),self.t_list[seg_num-1].ycor())
        if (self.t_list[0].heading()!=0):
            self.t_list[0].setheading(180)
            
    def turn_right(self):
        for seg_num in range(len(self.t_list)-1,0,-1):
            self.t_list[seg_num].goto(self.t_list[seg_num-1].xcor(),self.t_list[seg_num-1].ycor())
        if (self.t_list[0].heading()!=180):
            self.t_list[0].setheading(0)
    
    def turn_up(self):
        for seg_num in range(len(self.t_list)-1,0,-1):
            self.t_list[seg_num].goto(self.t_list[seg_num-1].xcor(),self.t_list[seg_num-1].ycor())
        if (self.t_list[0].heading()!=270):
            self.t_list[0].setheading(90)
    
    def turn_down(self): 
        for seg_num in range(len(self.t_list)-1,0,-1):
            self.t_list[seg_num].goto(self.t_list[seg_num-1].xcor(),self.t_list[seg_num-1].ycor())
        if (self.t_list[0].heading()!=90):
            self.t_list[0].setheading(270)