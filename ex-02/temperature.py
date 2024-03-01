#################################################################
# FILE : temperature.py
# WRITER : itai kahana, itaygil135 , 316385962
# EXERCISE : intro2cs2 ex2 2020
# DESCRIPTION: A simple program that check if a  given temperature is 
#              sufficient. 
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: nothing.
# NOTES: ...
#################################################################

def is_it_summer_yet(temperature,      \
                     temperature_day1, \
                     temperature_day2, \
                     temperature_day3):
    """ This function compare the sufficient temperature to the temperature of
        previous days and return True in case it is higher than at least two
        of the previous days. otherwise it return False."""
    if (temperature < temperature_day1 and temperature < temperature_day2) \
        or (temperature < temperature_day1 and temperature <temperature_day3)\
        or (temperature < temperature_day2 and temperature <temperature_day3):
        return True
    return  False




