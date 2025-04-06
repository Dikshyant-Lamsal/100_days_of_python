from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=0.9,stretch_wid=0.9)
        self.penup()
        self.dx=12
        self.dy=12
        self.move_speed=0.1
    
    def move(self):
        self.goto(self.xcor()+self.dx,self.ycor()+self.dy)
        
    def detect_collision(self):
        if self.ycor()>=290 or self.ycor()<=-290:
            return True
        return False
    
    def detect_hit(self, paddle):
        if self.distance(paddle) < 50 and abs(self.xcor()) >= 320:
            self.bounce()
            
        if abs(self.xcor() - paddle.xcor()) < 20 and abs(self.ycor() - paddle.ycor()) < 50:
            self.bounce()

        
    def detect_miss(self):
        if self.xcor()>=380:
            return "left"
        elif self.xcor()<=-380:
            return "right"      

        
    def bounce(self):
        self.dx*=-1
        self.move_speed = max(0.03, self.move_speed * 0.9)
        
    def bounce_wall(self):
        if self.detect_collision():
            self.dy *= -1
            
    def reset_position(self):
        self.goto(0,0)
        self.bounce()
        self.move_speed=0.1