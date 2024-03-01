def is_factor(num,factor):
    if num % factor == 0 and str(factor) in str(num):
        return False
    elif num % factor == 0 or str(factor) in str(num):
        return True
    return False



def fizzBuzz_3(num):
    string = num
    if is_factor(num, 3):
        string = "Fizz"
    if is_factor(num, 5):
        string = "Buzz"
    if is_factor(num,3) and is_factor(num,5):
        string = "FizzBuzz"

    return string
