from turtle import Turtle
from color_list import Colorchangeturtle
segment1 = ['part_1', 'part_2', 'part_3']
class Snake(Colorchangeturtle) :
    def __init__(self):
        super().__init__()
        self.snake_part = []
        self.connect_part(segment1)
        
        
    
    
    def new_snake(self):
        part = Colorchangeturtle()
        part.shape('square')
        part.change_color()
        part.penup()
     
        self.snake_part.append(part)
        
    
    
    def connect_part(self, segment):
        n = 0
        for part in segment:
            part = Colorchangeturtle()
            part.change_color()
            part.shape('square')
            part.change_color()
            part.penup()
            
            x_position = 0 - 20 * n
            part.goto(x = x_position, y = 0)
            n += 1
            self.snake_part.append(part)
                
    def move(self):
        for part in range(len(self.snake_part) - 1, 0, -1):
            new_x_coordinate = self.snake_part[part - 1].xcor()
            new_y_coordinate = self.snake_part[part - 1].ycor()
            self.snake_part[part].goto(new_x_coordinate, new_y_coordinate)
    
        self.snake_part[0].forward(20)
        
        
   
    def left(self):
        self.snake_part[0].setheading(self.snake_part[0].heading() + 90)
        
    def right(self):
        self.snake_part[0].setheading(self.snake_part[0].heading() - 90) 
        
 