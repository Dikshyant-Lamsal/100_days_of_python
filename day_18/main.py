from turtle import Screen, Turtle
import turtle_functions as tf

t_name = Turtle()
t_func = tf.TurtleFunctions()

t_name.speed(0)
t_name.hideturtle()
t_func.draw_painting(t_name,10,10)


s_name = Screen()
s_name.exitonclick()
