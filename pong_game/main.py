from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to Pong game")

screen.tracer(0)
screen.listen()
game_is_on = True

time.sleep(0.1)
r_position = (350, 0)
l_position = (-350, 0)
r_paddle = Paddle(r_position)
l_paddle = Paddle(l_position)
score = Scoreboard()

ball = Ball()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_right()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        score.increase_l_score()
        ball.reset_position()

    if ball.xcor() < -380:
        score.increase_r_score()
        ball.reset_position()

screen.exitonclick()
