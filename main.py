from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time 

def screen_setup():
    screen = Screen()
    screen.setup(width=600,height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    return screen


new_screen = screen_setup()
snake = Snake()
food = Food()
scoreboard = Scoreboard()


new_screen.listen()
new_screen.onkey(snake.up,"Up")
new_screen.onkey(snake.down,"Down")
new_screen.onkey(snake.right,"Right")
new_screen.onkey(snake.left,"Left")


is_game_on = True
while is_game_on:
        new_screen.update()
        time.sleep(0.1)
        snake.move()
        
        if snake.head.distance(food) < 15:
            snake.increase_snake()
            scoreboard.increase_score()
            scoreboard.update()
            food.refresh()

        if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.reset()
            snake.reset()
            

        for segment in snake.snake_body[1:]:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
               scoreboard.reset()
               snake.reset()
            
                

new_screen.exitonclick()