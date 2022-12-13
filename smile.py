# from turtle import *
# from random import randint
# f = 5
# b = 6

# def nopen(x, dir):
#     if dir == 5:
#         penup()
#         forward(x)
#         pendown()
#     elif dir  == 6:
#         penup()
#         backward(x)
#         pendown()

# def circ(x, fill, otl):
#     if fill == True:
#         begin_fill()
#         circle(x)
#         end_fill()
#     elif fill == False:
#         circle(x)
    
#     if otl == True:
#         color("black")
#         circle(x)


# speed(10)
# #The Head
# color("yellow")
# begin_fill()
# circle(100)
# end_fill()

# #Outline of Head
# color("black")
# pensize(5)
# circle(100)

# #First Eye
# color("white")
# left(90)
# nopen(100, f)
# left(90)
# nopen(50, f)
# circ(-30, True, True)

# #Second Eye

# nopen(100, b)
# color("white")
# circ(-30, True, True)


# left(90)
# nopen(15, b)
# left(90)

# color("black")
# circ(10, True, False)

# nopen(100, b)
# circ(10, True, False)

# penup()
# setposition(20,0)
# pendown()

# #Mouth
# color("red")
# left(90)
# nopen(50, f)
# circ(20, True, True)

# input()