

def all_option(n):
    return all_options_helper(3,0)

def all_options_helper(n,i):
    if i >= n:
        return [""]
    all_options = []
    for option in all_options_helper(n, i + 1):
        all_options += ["0" + option]
        all_options += ["1" + option]

    return all_options

print(all_option(3))


def all_options_filtered_helper(n):
    return all_options_filtered_helper(n,0)

def all_options_filtered_helper(n,i):
    if i >= n:
        return [""]
    all_option = []






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