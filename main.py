from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
#____
screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.bgcolor("black")
screen.title("SUPER DUPER JUEGO SNAKE :v")
screen.tracer(0)
#____
my_snake = Snake()
blue_dot = Food()
score_board = ScoreBoard()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")
screen.update()
game_continues = True
while game_continues:
    screen.update()
    time.sleep(0.1)
    my_snake.move()
    #Consume el alimento
    if my_snake.head.distance(blue_dot) < 15:
        blue_dot.refresh()
        score_board.increase_score()
        my_snake.extend_tail()
    #Muere al chocar el muro
    if my_snake.head.xcor() > 290 or my_snake.head.xcor() < -290 or my_snake.head.ycor() > 290 or my_snake.head.ycor() < -290:
        score_board.reset()
        my_snake.reset()
    #Muere al tocar su propio cuerpo
    for i in my_snake.segments[1:]:
        if my_snake.head.distance(i) < 10:
            score_board.reset()
            my_snake.reset()

screen.exitonclick()

