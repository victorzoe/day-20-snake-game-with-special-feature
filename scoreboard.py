from turtle import Turtle
from color_list import Colorchangeturtle
class Scoreboard(Colorchangeturtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.change_color()
        self.hideturtle()
        self.goto(0, 270)
        self.refreshscoreboard()
  
    def refreshscoreboard(self):
        self.change_color()
        self.write(f"Score Board: {self.score}", move = False, align = 'center', font = ('Arial', 20, 'normal'))
        
   
    
    def updatescoreboard(self):
        self.clear()
        self.score += 1
        self.change_color()
        self.hideturtle()
        self.goto(0, 270)
        self.refreshscoreboard()
      
        
    def game_over(self):
        self.goto(0,0)
        self.change_color()
        self.write("Game Over", move = False, align = 'center', font = ('Arial', 25, 'normal'))
   