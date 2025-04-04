from turtle import Screen, Turtle
from snake import Snake
from snake_screen import SnakeScreen
import time

screen = Screen()
snake=Snake()
scr=SnakeScreen(snake)

def begin_game():
    play_game=True
    while(play_game):
        screen.update()
        time.sleep(0.1)
        snake.move_forward(20)
        
    
screen.onkey(key="space",fun=begin_game)
screen.exitonclick()