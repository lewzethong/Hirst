# import colorgram
#
#
# colors = colorgram.extract('image.jpg', 30)
# rgd_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgd_colors.append(new_color)
#
#
# print(rgd_colors)
import turtle
from turtle import Turtle, Screen
import random

color_list = [(197, 165, 117), (142, 80, 56), (220, 201, 137), (59, 94, 119), (164, 152, 53), (136, 162, 181), (131, 34, 22), (69, 39, 32), (53, 117, 86), (192, 95, 78), (146, 177, 149), (19, 91, 68), (165, 143, 157), (31, 59, 76), (111, 75, 81), (228, 176, 164), (128, 29, 33), (179, 204, 177), (71, 34, 36), (25, 82, 89), (89, 146, 127), (18, 69, 57), (41, 66, 90), (219, 178, 182), (175, 94, 98), (179, 192, 205)]
tim = Turtle()
turtle.colormode(255)
tim.speed('fastest')


tim.pu()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for _ in range(10):
    for _ in range(10):
        tim.pd()
        tim.dot(20, random.choice(color_list))
        tim.pu()
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)
tim.hideturtle()





screen = Screen()
screen.exitonclick()