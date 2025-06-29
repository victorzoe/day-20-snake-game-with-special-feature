import random
from turtle import Turtle
color_list = [
    "red", "orange", "yellow", "green", "blue", "purple", "pink", "brown",
    "white", "gray", "cyan", "magenta", "lime", "indigo", "maroon",
    "navy", "olive", "teal", "turquoise", "gold", "silver", "coral", "salmon",
    "chocolate", "tan", "lavender", "aqua", "plum", "orchid"
]

class Colorchangeturtle(Turtle):
    def __init__(self):
        super().__init__()
    
    def change_color(self):
        new_color = random.choice(color_list)
        self.color(new_color)
        self.screen.ontimer(self.change_color, 500)