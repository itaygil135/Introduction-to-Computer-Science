#################################################################
# FILE : shapes.py
# WRITER : itai kahana, itaygil135 , 316385962
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A simple program that calculate shape's area
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: nothing.
# NOTES: ...
#################################################################
import  math

def circle_area():
    """ calcuate area of a circle """
    r = float(input())
    s_circle = (math.pi) * (r ** 2)
    return s_circle

def rectangle_area():
    """ calculate area of a rectangle"""
    a = float(input())
    b = float(input())
    return (a * b)

def triangle_area():
    """ calculate area of a triangle"""
    a = float(input())
    s_triangle = (math.sqrt(3) * (a * a)) / 4
    return s_triangle

def shape_area():
    """ This function calculate the area of a shape.
        The function receive from the user the choosen shape and its size.
        The function return the calculated area."""
    choosen = input("Choose shape (1=circle, 2=rectangle, 3=triangle): " )
    if choosen == "1":
        return(circle_area())
    elif choosen == "2":
        return (rectangle_area())
    elif choosen == "3":
        return (triangle_area())

