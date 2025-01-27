from turtle import Turtle as t, Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    
    def __init__(self) :
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        
    def create_snake(self):
        x = 0
        y = 0
        for box in range(3):
            box =  t("square")
            box.color("white")
            box.penup()
            box.goto(x,y)
            self.snake_body.append(box)
            x -= 20
    
    def increase_snake(self):
        lastX =  self.snake_body[-1].xcor()
        lastY =  self.snake_body[-1].ycor()
        box =  t("square")
        box.color("white")
        box.penup()
        box.goto(lastX,lastY)
        self.snake_body.append(box)
        
    def move(self):
        for box in range(len(self.snake_body)-1,0,-1):
            new_x = self.snake_body[box-1].xcor()
            new_y = self.snake_body[box-1].ycor()
            self.snake_body[box].goto(new_x,new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)
        
    def reset(self):
        for segments in self.snake_body:
            segments.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()  
        self.head = self.snake_body[0] 
        self.move()
        
        
        
    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)
            
    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)
            
    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)
            
    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)