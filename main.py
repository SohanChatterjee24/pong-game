from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong-Game")
screen.tracer(0)

paddle1 = Paddle()
paddle1.goto(x=350,y=0)

paddle2 = Paddle()
paddle2.goto(x=-350, y=0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(paddle1.paddle_up,"Up")
screen.onkeypress(paddle1.paddle_down,"Down")
screen.onkeypress(paddle2.paddle_up,"w")
screen.onkeypress(paddle2.paddle_down,"s")

is_game_on = True

move_speed = 0.1

while is_game_on:
    time.sleep(move_speed)
    screen.update()
    ball.ball_move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 340 and paddle1.ycor() - 50 < ball.ycor() < paddle1.ycor() + 50:
        ball.setx(340)  # reset x to edge
        angle_difference = ball.ycor() - paddle1.ycor()
        new_angle = 180 - ball.heading() + angle_difference / 5  # calculate bounce angle
        ball.setheading(new_angle)
        move_speed *= 0.9

    if ball.xcor() < -340 and paddle2.ycor() - 50 < ball.ycor() < paddle2.ycor() + 50:
        ball.setx(-340)
        angle_difference = ball.ycor() - paddle2.ycor()
        new_angle = 180 - ball.heading() - angle_difference / 5
        ball.setheading(new_angle)
        move_speed *= 0.9

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.setheading(180)
        scoreboard.l_point()
        move_speed = 0.1

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.setheading(180)
        scoreboard.r_point()
        move_speed = 0.1

screen.exitonclick()