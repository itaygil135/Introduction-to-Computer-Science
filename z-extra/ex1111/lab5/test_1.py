from code_1 import *

def test_1():
    assert fizzBuzz_1(3) == "Fizz"
    assert fizzBuzz_1(5) == "Buzz"
    assert fizzBuzz_1(15) == "FizzBuzz"
    assert fizzBuzz_1(1) == 1
    assert fizzBuzz_1(-3) == "Fizz"

if __name__ == '__main__':
    test_1()
