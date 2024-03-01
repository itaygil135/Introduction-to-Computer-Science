from code_2 import *


def test_2():
    assert fizzBuzz_2(3) == "Fizz"
    assert fizzBuzz_2(13) == "Fizz"
    assert fizzBuzz_2(31) == "Fizz"
    assert fizzBuzz_2(5) == "Buzz"
    assert fizzBuzz_2(52) == "Buzz"
    assert fizzBuzz_2(15) == "FizzBuzz"
    assert fizzBuzz_2(523) == "FizzBuzz"
    assert  fizzBuzz_2(1) == 1

if __name__ == '__main__':
    test_2()




