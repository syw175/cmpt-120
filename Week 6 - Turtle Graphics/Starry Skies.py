# Course: CMPT120
# Program: Turtle Graphics: Starry Skies
# Author: Steven Wong
# Date: March 2, 2022

import turtle
import random


# Draw stars using two parameters: size and color
def star(col, size):
    kay.fillcolor(col)
    kay.pencolor(col)
    kay.begin_fill()
    for k in range(5):
        kay.forward(size)
        kay.right(144)
    kay.end_fill()


# Draw a house using one parameter: size
def house(size):
    kay.begin_fill()
    for k in range(4):
        kay.forward(size)
        kay.right(90)
    kay.left(60)
    kay.forward(size)
    kay.right(120)
    kay.forward(size)


# Draw my initials followed by the last 2 digits of my student ID (DONEISH)
def signature():
    # Draw chr 'S'
    kay.circle(20, 180)
    kay.circle(-20, 180)
    kay.penup()
    kay.forward(125)
    kay.right(90)
    kay.pendown()

    # Draw chr 'W'
    for turns in range(2):
        kay.forward(50)
        kay.right(135)
        kay.forward(50)
        kay.left(135)

    # Draw char '2'
    kay.penup()
    kay.right(250)
    kay.forward(125)
    kay.right(90)
    kay.pendown()
    kay.right(180)
    kay.circle(-25, 180)
    kay.right(45)
    kay.forward(80)
    kay.left(135)
    kay.forward(55)

    # Draw char '7'
    kay.penup()
    kay.forward(75)
    kay.left(70)
    kay.pendown()
    kay.forward(80)
    kay.left(120)
    kay.forward(50)


kay = turtle.Turtle()
kay.speed(7)
turtle.colormode(255)
turtle.screensize(500, 300, 'black')

# Draw 10 stars with random locations and random colors
for i in range(10):
    kay.penup()
    kay.goto(random.randint(-600, 600), random.randint(350, 500))
    kay.pendown()
    star((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 75)

# Draw a lone house on the left side of the screen
kay.penup()
kay.pencolor(245, 66, 66)
kay.goto(-550, -200)
kay.pendown()
house(300)

# Draw my initials by executing the signature function
kay.penup()
kay.goto(250, -450)
kay.pendown()
kay.right(-90)
signature()

turtle.exitonclick()

