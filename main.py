from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# We create an instance of the Screen class
Screen = Screen()

# We create an instance of the Snake class
snake = Snake()

# We create an instance of the Food class
food = Food()

# We create an instance of the ScoreBoard class
scoreboard = ScoreBoard()


def main() -> None:
    # We call the function to set the properties of the window
    window_properties()

    Screen.listen()
    Screen.onkey(snake.up, "Up")
    Screen.onkey(snake.down, "Down")
    Screen.onkey(snake.right, "Right")
    Screen.onkey(snake.left, "Left")

    game_is_on = True
    while game_is_on:
        """
        We call the method to move the snake, and we pass the Screen object as a parameter,
        because we need to update the screen whenever we move the snake, we will use the method update()
        from the Screen class.
        """
        snake.move(Screen)

        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()
            Screen.update()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        for segment in snake.snake_body[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    # We call the method to keep the window open until we click on it
    Screen.exitonclick()


def window_properties() -> None:
    Screen.setup(width=600, height=600)
    Screen.bgcolor("black")
    Screen.title("Snake Game")
    # We will deactivate the animation of the turtle, so we can use the method update()
    # to update the screen when we want
    Screen.tracer(0)


if __name__ == "__main__":
    main()
