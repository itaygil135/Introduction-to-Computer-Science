from code_3 import *


def test_3():

    assert fizzBuzz_3(3) == 3
    assert fizzBuzz_3(13) == "Fizz"
    assert fizzBuzz_3(6) == "Fizz"
    assert fizzBuzz_3(5) == 5
    assert fizzBuzz_3(52) == "Buzz"
    assert fizzBuzz_3(10) == "Buzz"
    assert fizzBuzz_3(15) == "Fizz"
    assert  fizzBuzz_3(1) == 1
    assert  fizzBuzz_3(1530) == 1530
    assert  fizzBuzz_3(-60) == "FizzBuzz"


if __name__ == '__main__':

    test_3()