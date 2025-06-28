from turtle import Turtle
segment = ['part_1', 'part_2', 'part_3']
class Snake :
    def __init__(self):
        self.snake_part = []
        self.connect_part()
        
    def connect_part(self):
        n = 0
        for part in segment:
            part = Turtle(shape = 'square')
            part.penup()
            part.color('white')
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
        
 