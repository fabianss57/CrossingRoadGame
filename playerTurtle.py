from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(1)
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.setheading(90)

    def moveUp(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def startingPosition(self):
        self.goto(0,-280)