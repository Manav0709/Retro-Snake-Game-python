from turtle import Turtle
from random import randint


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()
        
    
    def refresh(self):
        randomX = randint(-280,280)
        randomY = randint(-280,280)
        self.goto(randomX,randomY)
        