def is_factor(num,factor):
    if num % factor == 0 or str(factor) in str(num):
        return True
    return False



def fizzBuzz_2(num):
    string = num
    if is_factor(num,3) and is_factor(num,5):
        string = "FizzBuzz"
    elif is_factor(num,3):
        string = "Fizz"
    elif is_factor(num, 5):
        string = "Buzz"

    return string