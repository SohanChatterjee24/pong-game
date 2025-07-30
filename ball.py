from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.75,stretch_len=0.75)
        start_heading = random.randint(153,207)
        self.setheading(start_heading)

    def ball_move(self):
        self.forward(20)

    def bounce(self):
        new_heading = 360 - self.heading()
        self.setheading(new_heading)


