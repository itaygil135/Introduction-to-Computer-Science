#################################################################
# FILE : largest_and_smallest.py
# WRITER : itai kahana, itaygil135 , 316385962
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A simple program that find the minimal and maximal of given
#               three numbers
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: nothing.
# NOTES: ...
#   the input list (1,1,1) was choosen since all numbers are equal
#   the input list (5,4,3) was choosen since the number are sorted in 
#   decreasing order
#################################################################

def largest_and_smallest(a,b,c):
    """ This function find the minimal and maximal numbers of a given three
    numbers.
    The function recevie three numbers.
    The function return two values, first first the minimal, then the maximal
    of the input number."""
    min_val = a
    max_val = a
    if b > max_val:
         max_val = b
    if c > max_val:
      max_val = c
    if b < min_val:
         min_val = b
    if c < min_val:
        min_val = c

    return (max_val, min_val)



def check_largest_and_smallest():
    """ This function test and validate the function largest_and_smallest.
        The function return True in case all tests passed.
        The function return False in case any test failed"""
    max_val , min_val = largest_and_smallest(17,1,6)
    if min_val != 1 or max_val != 17:
        return  False
    max_val , min_val = largest_and_smallest(1,17,6)
    if min_val != 1 or max_val != 17:
        return  False
    max_val , min_val = largest_and_smallest(1,1,2)
    if min_val != 1 or max_val != 2:
        return  False
    max_val , min_val = largest_and_smallest(1,1,1)
    if min_val != 1 or max_val != 1:
        return False
    max_val , min_val = largest_and_smallest(5,4,3)
    if min_val != 3 or max_val != 5:
        return False

    return True

