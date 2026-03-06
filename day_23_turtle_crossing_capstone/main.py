from turtle import Screen
from turtle_functions import TurtleFunctions
from scoreboard import Scoreboard
from cars import Car
import time


screen=Screen()
screen.setup(width=600,height=600)
sb=Scoreboard()
screen.tracer(0)
t_name=TurtleFunctions()
playGame=True

car_m = Car()
        
def reach_end():
    if t_name.ycor()>=250:
        sb.level+=1
        sb.update_score()
        t_name.setpos(x=0,y=-280)
        car_m.speed+=2
        screen.update()
   

while(playGame):
    
    if car_m.check_collision(t_name):
        print("GAME OVER")
        playGame=False
        sb.game_over()
        
    time.sleep(0.1)
    screen.update()

    car_m.create_car()
    car_m.move_forward()
    
    reach_end()
    
    
    
screen.exitonclick()