from turtle import Turtle
from random import randint
from color_list import Colorchangeturtle

class Food(Colorchangeturtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.change_color()
        self.speed('fastest')
        self.shapesize(0.5, 0.5)
        self.new_place()
       
        
    def new_place(self):
        x_coordinate = randint(-280, 280)
        y_coordinate = randint(-280, 280)
        self.goto(x_coordinate, y_coordinate)
        