from turtle import Screen,Turtle
from snake import Snake
from snake_screen import SnakeScreen
import time
from food import Food
from scoreboard import Scoreboard
ALIGHMENT="center"
FONT=("Courier",20,"normal")

screen = Screen()
snake=Snake()
food = Food()
scr=SnakeScreen(snake)
score = Scoreboard()

dis=Turtle()
dis.hideturtle()
dis.color("white")
dis.penup()
dis.goto(0,15)
arg="Press 'space' to start!"
dis.write(arg=arg,align=ALIGHMENT,font=FONT)


def begin_game():
    dis.clear()
    play_game=True
    while(play_game):
        screen.update()
        time.sleep(0.1)
        snake.move_forward(20)
        
        if snake.head.distance(food) < 15:
            food.refresh()
            score.increase_score()
            snake.grow_snake()

        if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
            score.game_over()
            snake.reset()
            play_game=False
        
        for segment in snake.t_list[1:]:
            
            if snake.head.distance(segment)<10:
                score.game_over()
                snake.reset()
                play_game=False
                

    if not play_game:
        dis.penup()
        dis.goto(0,0)
        arg="GAME OVER! Press 'space' to restart!"
        dis.write(arg=arg,align=ALIGHMENT,font=FONT)
    
        
        
screen.onkey(key="space",fun=begin_game)
screen.exitonclick()