# import colorgram
#
# color = []
#
#
# def rgb(color_info):
#     r = color_info.r
#     g = color_info.g
#     b = color_info.b
#     rgb_color = (r, g, b)
#     return rgb_color
#
#
# palate = colorgram.extract("image.jpg", 30)
#
# for item in palate:
#     color.append(rgb(item.rgb))
#
# print(color)

# import turtle
# from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)

clifford = t.Turtle()

# “fastest”: 0
# “fast”: 10
# “normal”: 6
# “slow”: 3
# “slowest”: 1
clifford.speed(10)
color_list = [(0, 0, 0), (229, 228, 226), (224, 222, 224), (199, 175, 117), (125, 36, 24), (170, 106, 56), (187, 158, 51), (5, 57, 83), (200, 215, 205), (222, 223, 225), (108, 67, 86), (88, 142, 56), (110, 160, 175), (20, 122, 176), (76, 39, 48), (63, 153, 138), (9, 68, 47), (134, 41, 43), (183, 97, 79), (179, 201, 186), (208, 199, 126), (149, 174, 162), (172, 165, 167), (26, 79, 60), (93, 141, 156), (211, 184, 176), (20, 78, 97), (195, 189, 191), (137, 123, 127), (184, 192, 201)]

def random_color():
    color = random.choice(color_list)
    return color

#hirstcircle
def draw_hirstgraph(max_length):

    for dot in range(0, max_length):
        dot += 1
        color = random_color()
        clifford.dot(20, color)
        clifford.color(color)
        if dot % 10 == 0 and dot != max_length:
            clifford.left(90)
            clifford.forward(50)
            clifford.left(90)
            clifford.forward(450)
            clifford.setheading(0)
        elif dot != max_length:
            clifford.forward(50)
        # clifford.right(angle)
        # clifford.circle(5)
        # clifford.fillcolor()


clifford.penup()
clifford.hideturtle()
clifford.setheading(220)
clifford.forward(600)
clifford.setheading(0)
number_of_dots = 100
draw_hirstgraph(100)


# #random walk
# clifford.shapesize(0.5)
# clifford.pensize(width=10)
# clifford.width(width=10)
# for _ in range(1000):
#     angle = random.choice(angles)
#     color = random_color()
#     clifford.color(color)
#     clifford.setheading(angle)
#     # clifford.right(angle)
#     clifford.forward(20)

# # shapes with random color
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         clifford.forward(100)
#         clifford.right(angle)
#
# for i in range(3, 11):
#     clifford.color(random.choice(colors))
#     draw_shape(i)


# #square
# for i in range(4):
#     clifford.right(90)
#     clifford.forward(90)

# #dashline
# for i in range(20):
#     clifford.forward(10)
#     clifford.penup()
#     clifford.forward(10)
#     clifford.pendown()

# #import prettytable
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
#
# print(table)

my_screen = t.Screen()
my_screen.exitonclick()
