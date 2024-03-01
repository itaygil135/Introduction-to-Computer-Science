#################################################################
# FILE : ex3.py
# WRITER : itai kahana, itaygil135 , 316385962
# EXERCISE : intro2cs2 ex3 2020
# DESCRIPTION: A set of mathematical functions
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: nothing.
# NOTES: ...
#################################################################

def input_list():
    """
    This function: read strings from the user (ended by null string),
    convert each string to a number, add all numbers to a list, calculate the
    sum of the numbers and add it as the last element of the list
    :return: the list of the numbers and their sum.
    """
    numbers_list = []
    # read list of numbers from the user
    string_from_user = input()
    while string_from_user != '' and string_from_user != "":
        numbers_list.append(float(string_from_user))
        string_from_user = input()
    # calculate the sum of the numbers
    list_sum = 0
    if len(numbers_list) > 0:
        for number in numbers_list:
            list_sum = list_sum + number
    # append the sum as the last number in the list
    numbers_list.append(list_sum)
    return numbers_list


def inner_product(vec_1, vec_2):
    """
    This function calculate a return the inner product of two given vectors
    :param vec_1: First vector
    :param vec_2: Second vector
    :return:
    None: in case the vectors length is not equal
    0   : in case the vectors are empty (no numbers in the vectors)
    otherwise: the inner product of the vectors
    """
    # Handle edge cases: invalid length of the vectors or an empty vectors
    if len(vec_1) != len(vec_2):
        return None
    if len(vec_1) == 0:
        return 0

    # calculate the inner product of two valid vectors
    product = 0
    for i in range(len(vec_1)):
        product = product + (vec_1[i]*vec_2[i])

    return product


def sequence_monotonicity(sequence):
    """
    This function receive list of numbers and return list of boolean flags
    reflecting if the sequence is monotonic/rising/decreasing.
    :param sequence: List of numbers. The list may be an empty list.
    :return: list of 4 boolean flags:
        flag 0: true in case the sequence is monotonic equal and rising
        flag 1: true in case the sequence is monotonic really rising
        flag 2: true in case the sequence is monotonic equal and decreasing
        flag 3: true in case the sequence is monotonic really decreasing
        In case the input list is empty/ has 1 number, all flags will be True
    """
    # by default, set all flags to be True.
    # Once a sequence found as not match the condition, turn the flat to False
    equal_and_rising = True
    rising = True
    equal_and_decreasing = True
    decreasing = True
    # loop over the sequence and compare each two subsequence elements
    for n in range(1, len(sequence)):
        if sequence[n] > sequence[n-1]:
            equal_and_decreasing = False
            decreasing = False
        elif sequence[n] == sequence[n-1]:
            rising = False
            decreasing = False
        else:
            equal_and_rising = False
            rising = False

    return [equal_and_rising, rising, equal_and_decreasing, decreasing]


def monotonicity_inverse(def_bool):
    """
    This function return a sequence that meet the given 'monotonic sequence'
    conditions.
    :param def_bool: 4 flags of monotonic sequence condition
    (rising, really rising, decreasing, really decreasing)
    :return: A sequence that meet the given 'monotonic sequence' conditions.
    """
    # all valid combinations of flags
    valid_combination_list =\
        [[True, True, False, False], [False, False, True, True],
         [True, False, True, False], [False, False, True, False],
         [True, False, False, False], [False, False, False, False]]
    # List of strings meeting all valid combination, at the flags' order
    solution_list = [[56.5, 57.5, 63, 84], [7.5, 4, 3.141, 0.111],
                     [2, 2, 2, 2], [3, 2, 2, 1], [1, 2, 2, 3], [1, 0, -1, 1]]

    # loop over all valid combinations of flags
    #   in case the input string found as a valid combination
    #       return the associated list of the input flag combination
    for index in range(len(valid_combination_list)):
        if valid_combination_list[index] == def_bool:
            return solution_list[index]
    # in case the input does not much any valid combination - return None.
    return None


def is_prime(number):
    """
    This function return True in case the given number is prime
    :param number: A number
    :return:
    True:  in case the given number is a prime number
    False: in case the given number is not a prime number
    """
    for i in range(2, number):
        if (number % i) == 0:
            return False
        if (i*i) > number:
            break
    return True


def primes_for_asafi(n):
    """
    This function calculate and return a list of the first n prime numbers
    :param n: the size of the required list
    :return: the list of the first n prime numbers
    """
    if n == 0:
        return None
    else:
        prime_list = [2]        # 2 is prime by definition
        i = 3                   # first number to check if it is prime
        while len(prime_list) < n:
            if is_prime(i):
                prime_list.append(i)
            i = i + 1

    return prime_list


def sum_of_vectors(vec_lst):
    """
    This function calculate and return the sum of a given vectors
    :param vec_lst: list of vectors
    :return:
    None    - in case the input list is empty
    0       - in case the vectors are empty
    otherwise - the sum of the vectors
    """
    # handle edge case - an empty input list
    if len(vec_lst) == 0:
        return None
    length = len(vec_lst[0])
    # handle edge case - input vectors are empty
    if length == 0:
        return []
    # calculate the sum of the given vectors
    # loop over the element (i) in the vectors list
    #   loop over all vectors
    #       summarize elements i of all vectors
    #       add the sum of the elements i to the summarizing vector
    sum_vectors_list = []
    for i in range(length):
        sum_element = 0
        for vec in vec_lst:
            sum_element = sum_element + vec[i]
        sum_vectors_list.append(sum_element)

    return sum_vectors_list


def num_of_orthogonal(vectors):
    """
    This function calculate the number of orthogonal vectors in a given list
    of vectors
    :param vectors: List of vectors
    :return: The number of orthogonal vectors in the input list
    """
    num_of_orthogonal_vectors = 0
    num_of_vectors = len(vectors)
    for vec1_index in range(num_of_vectors-1):
        for vec2_index in range(vec1_index + 1, len(vectors)):
            if inner_product(vectors[vec1_index], vectors[vec2_index]) == 0:
                num_of_orthogonal_vectors = num_of_orthogonal_vectors + 1

    return num_of_orthogonal_vectors
