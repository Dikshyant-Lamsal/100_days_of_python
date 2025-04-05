from turtle import Screen
from snake import Snake
from snake_screen import SnakeScreen
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()
snake=Snake()
food = Food()
scr=SnakeScreen(snake)
score = Scoreboard()
 
def begin_game():
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
            play_game=False
            score.game_over()
        
        for segment in snake.t_list[1:]:
            
            if snake.head.distance(segment)<10:
                play_game=False
                score.game_over() 
        
        
        
screen.onkey(key="space",fun=begin_game)
screen.exitonclick()