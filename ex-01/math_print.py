#################################################################
# FILE : math_print.py
# WRITER : itai kahana, itaygil135 , 316385962
# EXERCISE : intro2cs2 ex1 2020
# DESCRIPTION: A simple program that resolve a math problems.
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: nothing.
# NOTES: ...
#################################################################

import math

def golden_ratio():
    """This function print the golden ratio."""
    print((1+math.sqrt(5))/2)

def six_squared():
    """This function print the square of 6."""
    print(math.pow(6,2))

def hypotenuse():
    """This function print the hypotenuse of of a given triangular"""
    print(math.hypot(12,5))

def pi():
    """This function print the value of pi"""
    print(math.pi)

def e():
    """This function print the mathematical value of e"""
    print(math.e)

def squares_area():
    """This function print the are of given squares"""
    print(1**2,2**2,3**2,4**2,5**2,6**2,7**2,8**2,9**2,10**2)


# starting point program
if __name__ == "__main__":
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()