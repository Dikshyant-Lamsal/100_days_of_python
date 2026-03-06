from turtle import Screen

class SnakeScreen:
    
    def __init__(self,snake):
        screen = Screen()
        screen.setup(height=600,width=600)
        screen.bgcolor('black')
        screen.title("SNAKE GAME")
        screen.tracer(0)
        screen.listen()
        screen.onkey(key="w",fun=snake.turn_up)
        screen.onkey(key="s",fun=snake.turn_down)
        screen.onkey(key="a",fun=snake.turn_left)
        screen.onkey(key="d",fun=snake.turn_right)
        screen.onkey(key="Up",fun=snake.turn_up)
        screen.onkey(key="Down",fun=snake.turn_down)
        screen.onkey(key="Left",fun=snake.turn_left)
        screen.onkey(key="Right",fun=snake.turn_right)
        
