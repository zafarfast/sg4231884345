from turtle import Turtle, Screen
import time
import turtle
import random

import random
color = ["red", "blue", "brown", "orange"]
screen = Screen()
screen.colormode(255)
turtle.hideturtle()
turtle.listen()
turtle.penup()
screen.tracer(0)
screen.title("Classic Snake")
snake = [Turtle(shape="square"), Turtle(shape="square"), Turtle(shape="square")]
Screen().bgcolor("black")
snake[0].color("white")
snake[1].color("white")
snake[2].color("white")

def up():
    global snake
    if snake[0].heading() != 270:
        snake[0].setheading(90)



def down():
    global snake
    if snake[0].heading() != 90:
        snake[0].setheading(270)


def right():
    global snake
    if snake[0].heading() != 180:
        snake[0].setheading(0)


def left():
    global snake
    if snake[0].heading() != 0:
        snake[0].setheading(180)


turtle.onkey(key="Up", fun=up)
turtle.onkey(key="Down", fun=down)
turtle.onkey(key="Right", fun=right)
turtle.onkey(key="Left", fun=left)
snake[0].penup()
snake[1].penup()
snake[2].penup()

snake[1].goto(-21, 0)
snake[2].goto(-42, 0)
game_over = False

target = Turtle(shape="circle")
target.penup()
target.color("blue")
target.goto(random.randint(-120, 120), random.randint(-120, 120))

score = Turtle()

score.hideturtle()
score.penup()
score.goto(-50, 200)
score_card = 0
score.write("Score: 0",font=("Arial", 20, "normal"))
score.color("white")

while not game_over:
    positions = []
    screen.update()
    time.sleep(0.1)

    for index_t in range(len(snake)):
        positions.append((snake[index_t].xcor(), snake[index_t].ycor()))

    for index_r in range(1, len(snake)):
        if (snake[0].xcor() > positions[index_r][0] - 20) and snake[0].xcor() < positions[index_r][0]+20:
            if (snake[0].ycor() > positions[index_r][1] - 20) and snake[0].ycor() < positions[index_r][
                1] + 20:
                screen.update()
                game_over = True
                score.goto(-80, 50)
                score.color("yellow")
                score.write("GAME OVER!",font=("Arial", 20, "normal"))


    if (snake[0].xcor() > target.xcor() - 20) and snake[0].xcor() < target.xcor()+20:
        if (snake[0].ycor() > target.ycor() - 20) and snake[0].ycor() < target.ycor() + 20:
            target.goto(random.randint(-120, 120), random.randint(-120, 120))
            score_card += 1
            score.clear()

            score.write(f"Score: {score_card}", font=("Arial", 20, "normal"))

            snake.append(Turtle(shape="square"))
            snake[-1].penup()
            snake[-1].color("white")

    length = len(snake)
    for i in range(length-1, 0, -1):
        snake[i].goto(snake[i - 1].xcor(), snake[i - 1].ycor())
        if snake[0].xcor() < -1*(screen.screensize()[0]):
            snake[0].goto(screen.screensize()[0], snake[0].ycor())

        if snake[0].xcor() > (screen.screensize()[0]):
            snake[0].goto(-1 * screen.screensize()[0], snake[0].ycor())

        if snake[0].ycor() < -1*(screen.screensize()[1]):
            snake[0].goto(snake[0].xcor(), screen.screensize()[1])

        if snake[0].ycor() > (screen.screensize()[1]):
            snake[0].goto(snake[0].xcor(), -1 * screen.screensize()[1])
            screen.update()

    snake[0].forward(20)

screen.exitonclick()

