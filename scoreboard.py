from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', move=False, align='center', font=('Arial', 18, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align='center', font=('Arial', 18, 'normal'))
