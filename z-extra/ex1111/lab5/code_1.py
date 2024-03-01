

def fizzBuzz_1(num):
    string  = num
    if num % 3 ==0 and num % 5 == 0:
        string = "FizzBuzz"
    elif num % 3 == 0:
        string = "Fizz"
    elif num % 5 == 0:
        string = "Buzz"

    return (string)