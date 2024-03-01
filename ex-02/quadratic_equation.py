#################################################################
# FILE : quadratic_equation.py
# WRITER : itai kahana, itaygil135 , 316385962
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A simple program that calcualte quadratic equation.
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: nothing.
# NOTES: ...
#################################################################

import math

def quadratic_equation(a,b,c):
    """ This function calculate the solutions of a quadratic equation.
        The function return the solution(s) of the equations, or None in case
        there are no solutions."""
    quadratic_sqrt = (b*b) - (4*a*c)
    if quadratic_sqrt < 0:
        sol1,sol2 = None,None

    elif quadratic_sqrt == 0:
        sol1 = ((-b)/ (2*a))
        sol2 = None

    else:
        sqrt = math.sqrt(quadratic_sqrt)
        sol1 = ((-b + sqrt) / (2*a))
        sol2 = ((-b - sqrt)/(2*a))


    return (sol1,sol2)


def quadratic_equation_user_input():
    """ This function calculate a quadratic equation based on user input.
        The function receive from the user the coefficients of the equation,
        validate them and calculate the equation."""
    a,b,c = input("Insert coefficients a, b, and c: ").split()
    a = float(a)
    b = float(b)
    c = float(c)

    if a == 0:
        print("The parameter 'a' may not equal 0")
    else:
        x,y = quadratic_equation(a,b,c)
        if x == None:
            print("The equation has no solutions")
        elif y == None:
            print("The equation has 1 solution:" ,x)
        else:
            print("The equation has 2 solutions:", x ,"and",y)

