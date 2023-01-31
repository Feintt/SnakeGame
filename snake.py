from turtle import Turtle
from time import sleep
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        # This is where we will store the body parts of the snake
        self.snake_body = []
        # We create the first 3 body parts of the snake
        self.create_snake()
        self.head = self.snake_body[0]
        self.snake_body[-1].color("red")
        # We change the color of the head and the tail of the snake
        # to make it easier to see
        self.head.color("green")

    def create_snake(self):
        """
        As the square is 20x20 pixels, we need to move the turtles 20 pixels apart from each other.
        We will create the first 3 body parts of the snake with a for loop, which will move the
        turtles 20 pixels apart from each other to the left.
        """
        for i in range(0, 60, 20):
            """ 
            We call the function to create the 3 objects and their properties.
            This function will use 2 parameters, the x and y coordinates.
            The y will always be 0, because we want the snake to be in the middle of the screen,
            and the x will be the value of the variable i, which will be 0, 20 and 40.
            """
            self.turtle_body_part(-i, 0)

    def turtle_body_part(self, x_coordinate: int, y_coordinate: int) -> None:
        # We create an instance of the turtle, and we will use it to create the body parts of the snake
        head = Turtle()
        head.shape("square")
        head.color("white")
        head.penup()
        head.goto(x_coordinate, y_coordinate)
        # We add the turtle to the list of body parts
        self.snake_body.append(head)

    def move(self, screen: object):

        sleep(0.1)
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].goto(self.snake_body[i - 1].xcor(), self.snake_body[i - 1].ycor())
        self.head.forward(MOVING_DISTANCE)
        screen.update()

    def extend(self):
        self.snake_body[-1].color("white")
        self.turtle_body_part(self.snake_body[-1].xcor(), self.snake_body[-1].ycor())
        self.snake_body[-1].color("red")

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
