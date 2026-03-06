from turtle import Turtle
import random

COLORS = ["red", "orange", "green", "blue", "purple"]

class Car():
    speed = 15
    
    def __init__(self):
        self.cars = []
    
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.setpos(x=300, y=random.randint(-230, 230))  
            car.setheading(180)
            self.cars.append(car)

    def move_forward(self):
        for car in self.cars:
            car.forward(self.speed)

            if car.xcor()==-300:
                car.setpos(x=300, y=random.randint(-230, 230)) 
        
    def check_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False