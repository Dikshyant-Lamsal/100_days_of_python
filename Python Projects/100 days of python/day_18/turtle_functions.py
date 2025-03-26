from turtle import Turtle, Screen,colormode
import random
import colorgram

colormode(255)
directions = [0,90,180,270]
colors=[]
frwrd_speed=35
c=colorgram.extract('image.jpg',50)

for i in c:
    colors.append(i.rgb)


class TurtleFunctions:

    def make_square(self,turtle_n):
        self.t_name=turtle_n
        for _ in range(4):
            self.t_name.forward(100)
            self.t_name.left(90)
    
    def make_dashed_square(self,turtle_n):
        self.t_name=turtle_n
        for _ in range(4):
            self.dashed_lines(turtle_n,100)
            self.t_name.left(90)

    def dashed_lines(self,turtle_n,length):
        self.t_name=turtle_n
        for i in range(length):
            if i%2!=0:
                self.t_name.pendown()
            else:
                self.t_name.penup()
            self.t_name.forward(9)
    
    def draw_shapes(self,turtle_n):
        self.t_name=turtle_n
        for i in range(3,10+1):
            angle=360/i
            self.t_name.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
            for _ in range(i):
                self.t_name.forward(100)
                self.t_name.right(angle)

    def random_walk(self,turtle_n,turns):
        self.t_name=turtle_n
        for _ in range(turns):
            self.t_name.color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
            i=random.randint(0,1)
            if i==1:
                self.t_name.left(random.choice(directions))
                # self.t_name.left(random.randint(0,360))
            else:
                self.t_name.right(random.choice(directions))
                # self.t_name.right(random.randint(0,360))
            self.dashed_lines(self.t_name,10)

    def draw_s_graph(self,turtle_n,radius):
        self.t_name=turtle_n
        for _ in range(int(360/radius)):
            self.t_name.color(random.choice(colors))
            self.t_name.circle(100)
            self.t_name.setheading(int(self.t_name.heading())+10)

    def draw_painting(self,turtle_n,l,b):
        self.t_name=turtle_n
        self.t_name.penup()
        for _ in range(l):
            for j in range(2*b):
                if (j%2==0):
                    self.t_name.color(random.choice(colors))
                    self.t_name.dot(20)
                self.t_name.forward(frwrd_speed)
            
            self.t_name.left(90)
            self.t_name.forward(frwrd_speed)
            self.t_name.left(90)
            self.t_name.forward(frwrd_speed*l*2)
            self.t_name.left(180)
            