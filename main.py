import random
from turtle import Turtle, Screen
from random import randint

tim = Turtle()
tim.shape("turtle")
tim.color("red")
screen = Screen()
screen.colormode(255)
directions = [0,90,180,270]


# Challenge 1
def draw_square(turtle_object):
    turtle_object.forward(100)
    turtle_object.right(90)
    turtle_object.forward(100)
    turtle_object.right(90)
    turtle_object.forward(100)
    turtle_object.right(90)
    turtle_object.forward(100)
    screen.exitonclick()


# Challenge 2
def draw_dashedline(turtle_object, length):
    for x in range(length):
        turtle_object.forward(1)
        turtle_object.penup()
        turtle_object.forward(1)
        turtle_object.pendown()
    screen.exitonclick()


# Challenge 3
def draw_shapes(turtle_object, length):
    # range represents the number of sides(triangle to decagon)

    for x in range(3, 11):
        for y in range(x - 1):
            turtle_object.right(360 / x)
            turtle_object.forward(length)
        turtle_object.home()
        turtle_object.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    screen.exitonclick()

#Challenge 4
def draw_randomwalk(turtle_object, length, line_length):
    turtle_object.width(10)
    for x in range(length):
        turtle_object.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        turtle_object.setheading(random.choice(directions))
        turtle_object.forward(line_length)
    screen.exitonclick()

#Challenge 5
def draw_spirograph(turtle_object,radius,numCircles):
    for x in range(numCircles):
        turtle_object.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        turtle_object.speed(100)
        turtle_object.circle(radius)
        turtle_object.right(x)
        turtle_object.forward(1)
    screen.exitonclick()

# draw_square(tim)
# draw_dashedline(tim,100)
# draw_shapes(tim,100)
#draw_randomwalk(tim, 60, 15)
draw_spirograph(tim,50,100)
