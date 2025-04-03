from turtle_functions import TurtFunctions # type: ignore
from turtle import Turtle,Screen
import random

s_name= Screen()
s_name.setup(width=500,height=400)
colors=["blue","green","black","orange","red"]

user_bet=s_name.textinput('Turlte Race!!!','Who wins?').upper()

race_on=False

turt_list=[]

i_y=-150
t_list=[]

for c in colors:
    i_y+=50
    t_name = TurtFunctions(-240,i_y,c)
    t_list.append(t_name)


  
winner=""
def race():
    global user_bet
    if user_bet:
        race_on=True
        
    while(race_on):
        for turt in t_list:
            if turt.check_coords():
                winner=(turt.c).upper()
                if winner==user_bet:
                    print(f"You Won! The winning color is {winner}")
                else:
                    print(f"You lost!\nUser chose:{user_bet}. Winner is: {winner}")
                race_on=False
            else:
                rand_dist=random.randint(0,10)
                turt.run(rand_dist)

s_name.listen()
s_name.onkey(key="space",fun=race) 

s_name.exitonclick()