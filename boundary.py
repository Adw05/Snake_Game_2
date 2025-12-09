from turtle import Turtle
class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.pensize(10)
        self.penup()
        self.hideturtle()
        self.goto(-270, 270)
        self.setheading(0)
        self.pendown()
    def draw(self):
        for _ in range(4):
            self.forward(540)
            self.right(90)
        self.penup()