#################################################################
# FILE : wordsearch.py
# WRITER : itai kahana, itaygil135 , 316385962
# EXERCISE : intro2cs2 ex7 2020
# DESCRIPTION: This file implement recursive functions
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: nothing.
# NOTES: ...
#################################################################
from typing import List, Tuple, Set, Any


def print_to_n(n: int) -> None:
    """
    This function prints akk the numbers from 1 to n.
    :param n: the number to start print from
    :return: None
    """
    if n < 1:
        return
    print_to_n(n-1)
    print(n)


def digit_sum(n: int) -> int:
    """
    This function return the sum of all digits at a given number
    :param n: the number to summarize it digits
    :return: the sum of the digits
    """
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)


def is_prime(n: int) -> bool:
    """
    This function check if a given number is a prime number
    :param n: the number to check
    :return:  True  - in case the given number is a prime number.
              False - in case the given number is not a prime number.
    """
    if n < 1:
        return False
    if not has_divisor_smaller_than(n, n - 1):
        return True
    return False


def has_divisor_smaller_than(n: int, i: int) -> bool:
    """
    This function check if for a given number (n), there is a divisor smaller
    than given potential max divisor (i)
    :param n: The number to check if is has smaller division
    :param i: the potential max divisor
    :return:  True  - if the number (n) has any divisor smaller or equal to i
              False - otherwise.
    """
    if i < 2:
        return False
    if n % i == 0:
        return True
    return has_divisor_smaller_than(n, i - 1)


def play_hanoi(hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> None:
    """
    This function move n disks from the source tower to the destination tower
    according to "hanoi game rules"
    :param hanoi:
    :param n:    the number of disks to move
    :param src:  the source tower
    :param dst:  the destination tower
    :param temp: additional tower to be used
    :return: None
    """
    if n < 1:
        return
    if n == 1:
        hanoi.move(src, dst)
    else:
        play_hanoi(hanoi, n-1, src, temp, dst)
        hanoi.move(src, dst)
        play_hanoi(hanoi, n-1, temp, dst, src)


def _print_sequences_helper(lst: List[str], n: int, cur_seq: str) -> None:
    """
    this function print all possible permutations of length n from a given
    list by calling itself recursively
    :param lst:     list of characters
    :param n:       the required length of the permutations
    :param cur_seq: the current sequence till now
    :return:        None
    """
    if n == 0:
        print(cur_seq)
        return
    for item in lst:
        _print_sequences_helper(lst, n-1, cur_seq + item)


def print_sequences(char_list: List[str], n: int) -> None:
    """
    this function print all possible permutations of sub-strings, of length n
    from a given list, by calling helper function.
    Note that each character may appear more than once.
    :param char_list: list of characters
    :param n:         the required length of the sub-strings
    :return:          None
    """
    if n < 1:
        return
    _print_sequences_helper(char_list, n, '')


def _print_no_rep_sequences_helper(lst: List[str],
                                   item: str,
                                   n: int,
                                   cur_seq: str) -> None:
    """
    this function print all possible permutations of sub-strings, of length n
    from a given list, avoid including the same character twice.
    The function call itself recursively.
    :param lst:     list of characters
    :param item:    a character from the list that was already included at the
                    sequence and therefore should be omitted from the current
                    list of characters
    :param n:       the required length of the sub-strings
    :param cur_seq: the current sequence till now
    :return:        None
    """
    if n == 0:
        print(cur_seq)
        return
    if len(lst) > 0:
        lst.remove(item)
    for item in lst:
        _print_no_rep_sequences_helper(lst[:], item, n-1, cur_seq + item)


def print_no_repetition_sequences(char_list: List[str], n: int) -> None:
    """
    this function print all possible permutations of sub-strings, of length n
    from a given list, avoid including the same character twice.
    The function call an helper function.
    :param char_list:  list of characters
    :param n:          the required length of the sub-strings
    :return:        None
    """
    if n < 1:
        return
    char_list.append("")
    _print_no_rep_sequences_helper(char_list, "", n, '')


def _parentheses_helper(n: int) -> Set[str]:
    """
    This function return all valid sequences of parentheses of a given length.
    The function uses the type SET in order to avoid adding the same sequence
    twice
    :param n:  The length of required sequences
    :return:   A set of all valid sequences.
    """
    parentheses_set = set()
    if n == 1:
        parentheses_set.add("()")
        return parentheses_set
    for item in _parentheses_helper(n-1):
        parentheses_set.add("()" + item)
        parentheses_set.add(item + "()")
        parentheses_set.add("(" + item + ")")
    return parentheses_set


def parentheses(n: int) -> List[str]:
    """
    This function return list of all valid sequences of parentheses of a
    given length. The function calls an helper function.
    :param n:
    :return: List of valid sequences
    """
    parentheses_set_list = []
    if n > 0:
        for item in _parentheses_helper(n):
            parentheses_set_list.append(item)
    return parentheses_set_list


def flood_fill(image: List[List[str]], start: Tuple[int, int]) -> None:
    """
    This function fill an empty cells in a given image. The function will not
    fill cells that are blocked by already filled cells.
    :param image: matrix implemented by two dimension nested list.
    :param start: first cell to start fill the image from. The cell is
                  implemented by a tuple of two integers, for row and col
    :return:     None. the original image will be modified.
    """
    if image[start[0]][start[1]] == '*':
        return
    image[start[0]][start[1]] = '*'
    new_list = [(start[0]+1, start[1]), (start[0], start[1] + 1),
                (start[0] - 1, start[1]), (start[0], start[1] - 1)]
    for i in new_list:
        flood_fill(image, i)

all[2, 9, 3, 23, 0, None, 1, -1, True]
