import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.color("black")
pen.pensize(3)

pen.begin_fill()

for i in range(4):
    pen.forward(100)
    pen.right(90)

pen.end_fill()

turtle.done()