from random import *
from turtle import Turtle, Screen



class MyTurtle(Turtle):

    # def rancol(self):
    #     hex = ["a", "b", "c", "d", "e", "f", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    #     col = ["#"]
    #     for i in range(6):
    #         col.append(choice(hex))
    #         strr = "".join(col)

    def ranshape(self, x, y):
        self.penup()
        self.setposition(randint(-200,200), randint(-200,200))
        self.pendown()
        self.circle(50, steps=randint(1,5))

    def __init__(self) -> None:
        super().__init__()
        self.ranshape(0, 0)
        self.onclick(self.ranshape)






x = MyTurtle()
y = MyTurtle()

x.forward(100)
y.backward(100)

screen = Screen()
screen.mainloop()


