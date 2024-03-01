#################################################################
# FILE : hello_turtle.py
# WRITER : itai kahana, itaygil135 , 316385962
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A simple program that draw three flowers by using turtle.
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: nothing.
# NOTES: ...
#################################################################

import turtle

def draw_petal():
    """This function draw a single petal."""
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)

def draw_flower():
    """This function draw a single flower by calling draw_petal couple of
    times."""
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)

def draw_flower_and_advance():
    """This function draw a single flower by calling draw_flower and set
    the turtle to some point in right of it which the turtle located.
    this point is the position where next flower should be drew."""
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()

def draw_flower_bed():
    """This function draw a three flower by calling draw_flower_and_advance
    three times."""
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()

############################################################################
# program starting point
############################################################################
if __name__ == "__main__":
    draw_flower_bed()
    turtle.done()