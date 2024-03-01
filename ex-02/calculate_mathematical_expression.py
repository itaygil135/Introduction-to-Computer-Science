#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : itai kahana, itaygil135 , 316385962
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A simple program that calculate a mathematical expression.
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: nothing.
# NOTES: ...
#################################################################
def calculate_mathematical_expression(num1 ,num2, act):
    """ This function calculate a mathematical expression based on two numbers
        and an operator.
        The function receive two numbers and mathematical operation.
        The function return the value of the mathematical expression. In case
        of invalid input (invalid operator or division by zero, the function
        return None"""
    if (act == ":"):
        if num2 == 0:
            result = None
        else:
            result = (num1 / num2)
    elif act == "*":
            result = (num1 * num2)
    elif act == "-":
            result = (num1 - num2)
    elif act == "+":
            result = (num1 + num2)
    else:
        result = None

    return (result)



def calculate_from_string(expreesion_str):
    """ This function calculate a mathematical expression based on an given
        string.
        The function split the string to numbers and operators and calculate 
        the expression.
        The function return the calculated value."""
    expreesion_list = expreesion_str.split()
    num1 = float(expreesion_list[0])
    num2 = float(expreesion_list[2])
    act = expreesion_list[1]
    return calculate_mathematical_expression(num1,num2,act)

