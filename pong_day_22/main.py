from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("PONG GAME")
screen.setup(height=600,width=800)
screen.tracer(0)
r_paddle=Paddle("left","red")
l_paddle=Paddle("right","blue")
ball = Ball()
s_b=Scoreboard()
game=True



while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.bounce_wall()
    
    ball.detect_hit(r_paddle)
    ball.detect_hit(l_paddle)
        

    if ball.detect_miss():
        if ball.detect_miss().lower()=="left":
            s_b.increase_score('left')
        elif ball.detect_miss().lower()=="right":
            s_b.increase_score('right')
        ball.reset_position()
        
    
    if s_b.is_game_over():
        ball.goto(0,0)
        s_b.game_over()
        game=False   



screen.exitonclick()
