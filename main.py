from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from color_list import Colorchangeturtle
screen = Screen()
scoreboard = Scoreboard()
food = Food()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('My snake game')

screen.tracer(0)



snake = Snake()
screen.listen()
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')



is_game_on = True
while is_game_on:
    screen.update() 
    time.sleep(0.1)
    snake.move()
    
    if snake.snake_part[0].distance(food) < 20 :
        food.new_place()
        scoreboard.change_color()
        scoreboard.updatescoreboard()
        snake.new_snake()
    
    
    
    if snake.snake_part[0].xcor() > 280 or snake.snake_part[0].xcor() < -280 or snake.snake_part[0].ycor() > 280 or snake.snake_part[0].ycor() < -280  :
        is_game_on = False
        scoreboard.game_over()
    for part in range(1, len(snake.snake_part)):
        if snake.snake_part[0].position() == snake.snake_part[part]:
            is_game_on = False
            scoreboard.game_over()
            


screen.exitonclick()