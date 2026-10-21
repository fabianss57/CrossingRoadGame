from turtle import Turtle,Screen
from playerTurtle import Player
from car import Car

import time

#Initializing variables
timmy = Player()
screen = Screen()

#Create screen
screen.setup(width=600,height=600)
screen.tracer(0)

#Have screen listen for player input
screen.listen()
screen.onkey(timmy.moveUp,"Up")

#Set turtle to bottom of screen
timmy.startingPosition()

car = Car()






#Get the game to start running
game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()
    car.startDrive()

    #If the turtle reaches the other side reset the player to the bottom of the screen
    if timmy.ycor() > 280:
        timmy.startingPosition()

    if car.xcor() < -280:
        car.removeCar()









screen.exitonclick()
