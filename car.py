from turtle import Turtle
import random

#Colors of the cars
COLORS = ["BlueViolet", "DarkBlue", "Black", "aquamarine4", "chartreuse4", "DarkCyan", "DarkGreen", "DarkRed", "DarkSlateGrey",
          "DeepPink4", "firebrick4", "gray0", ]

#The window size for where the cars can spawn (-270 to 270) on the y axis
MIN_ROW = -270
MAX_ROW = 270

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(270)
        self.speed(1)
        self.setposition(270, random.randint(MIN_ROW, MAX_ROW))
        self.shape("square")
        self.shapesize(2, 1)


    def startDrive(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    def removeCar(self):
        self.hideturtle()
        self.stopDrive()

    def stopDrive(self):
        self.setpos(self.xcor(), self.ycor())
