import boggle_board_randomizer
import copy
BOARD_SIZE = 4
POSSIBLE_MOVES = [(0, 1),
                  (0, -1),
                  (1, 0),
                  (-1, 0),
                  (1, 1),
                  (1, -1),
                  (-1, -1),
                  (-1, 1)]


def load_words_dict(file_path):
    """
    tis function get a file which contain a words read it and make a dictionary
    that the words are the keys and True is the values
    :param file_path:
    :return: the prepared dictionary
    """
    with open(file_path, 'r') as f:
        words_dict = dict()
        for line in f:
            our_line = line.replace("\n", "")
            if our_line not in words_dict:
                words_dict[our_line] = True
        return words_dict


def is_valid_path(board, path, words):
    """
    this function checks if the given path is a valid one
    a valid path is a path which create an word on the board which each
    coordinate is not out of range and "neighbour" of each over and
    if it is also verify if this word in the dictionary.
    :param board: random board which given from the boggle_board_randomizer
    :param path: a list of tuples (each tuple contain a coordinate)
    :param words: a dictionary
    :return: if word is valid return the word else: None
    """
    if not (0 < len(path) <= BOARD_SIZE**2):
        return None
    word = ""
    tuple_holder = set()
    ind = 0
    for item in path:
        # verify tuple include 2 values exactly
        if len(item) != 2:
            return None
        # verify each value at the tuple is within the board size
        for coordinate in item:
            if not(0 <= coordinate < BOARD_SIZE):
                return None
        if item in tuple_holder:
            return None
        tuple_holder.add(item)
        # verify each two subsequence tuples are neighbors
        if 0 < ind:
            if abs(path[ind][0] - path[ind-1][0]) > 1:
                return None
            if abs(path[ind][1] - path[ind - 1][1]) > 1:
                return None
        word = word + board[path[ind][0]][path[ind][1]]
        ind += 1
    if word not in words:
        return None

    return word


def find_length_n_words(n, board, words):
    """
    this function get the board and the dictionary (which contains all the
    valid words) and a number and returns all the valid words which its
    length is the given number and which are located on the board
    :param n: the needed length of the word
    :param board: the game board
    :param words: the words dictionary
    :return: a list of tuples (each tuple contain two index,
     on the first - the word, on the next - the path)
    """

    # ignore words/path shorter than 3 or longer than 16
    if n > 16:
        return []

    # create set of words to search, based on their length
    word_search_set = set()
    for item in words:
        if len(item) == n:
            word_search_set.add(item)
    # search all words in the board and add them to all_found_words
    all_found_words = list()
    for word_to_search in word_search_set:
        find_length_n_one_word(n, board, word_to_search, all_found_words)
    return list(all_found_words)


def find_length_n_one_word(n, board, word_to_search, all_found_words):
    """
    this function get from its caller the same parameters and
    in addition a set of all the valid (by length) words
    which whe are looking to search and checking one by one if its on the board
    and how much and returns the prepared list of tuples to it caller
    :param n: the needed lengths of the words
    :param board: the game board
    :param word_to_search: all the valid word in the needed length
    :param all_found_words: the list of tuples which will return at the end
    :return: None
    """
    # start looking for the word a each of the board's cube
    for row in range(len(board)):
        for col in range(len(board[row])):
            coordinate = (row, col)
            # search for the word. if found- add it to all_found_words

            find_length_n_words_helper(n,    # length of word
                                       board,
                                       "",   # word found until now
                                       word_to_search,
                                       all_found_words,
                                       [],   # path to the word found until now
                                       coordinate)


def find_length_n_words_helper(n, board, word_found, word_to_search,
                               all_found_words, mooving_list, coordinate):
    """
    this function it is an helper function which goes recursively
    and find the match word on the board and
    append a tuple of the word and its coordinate path to the list
    :param n: the needed length
    :param board: the game board
    :param word_found: the word which found so far
    :param word_to_search: a valid word which we are looking for on the board
    :param all_found_words: the final list which will include at the end tuples
    of all the valid words in the needed lengths on the table and its paths
    :param mooving_list: a temporary list which will contain the path each moment
    :param coordinate: tuple of row and col
    :return: None (its just update the final list)
    """

    if coordinate in mooving_list:
        return

    # using "temp_word" so in case it is not a legal step, the
    #       word_found will not be impacted and there will be no
    #       need to remove the last letter/s from it
    temp_word = word_found + board[coordinate[0]][coordinate[1]]
    if temp_word == word_to_search:
        mooving_list.append(coordinate)
        add = copy.deepcopy(mooving_list)
        tuple_temp = (temp_word, add)
        print("adding", tuple_temp)
        all_found_words.append(tuple_temp)
        mooving_list.pop()
        return

    if len(temp_word) > len(word_to_search):
        return

    for index in range(len(temp_word)):
        if temp_word[index] != word_to_search[index]:
            return
    # from here i know: temp_word 'abc'   word_search = 'abcde'
    mooving_list.append(coordinate)
    word_found = word_found + board[coordinate[0]][coordinate[1]]
    for move in POSSIBLE_MOVES:
        if is_legal_step(coordinate, move):
            coordinate = (coordinate[0] + move[0], coordinate[1] + move[1])
            find_length_n_words_helper(n, board, word_found, word_to_search,
                                       all_found_words, mooving_list,
                                       coordinate)
            coordinate = (coordinate[0] - move[0], coordinate[1] - move[1])

    num_of_chars_to_delete = (-1)*len(board[coordinate[0]][coordinate[1]])
    word_found = word_found[0:num_of_chars_to_delete]
    mooving_list.pop()


def is_legal_step(coordinate, step):
    """
    this function checks if the given future step
    which we wants to do is a legal one and if it is not we will not do it
    :param coordinate: a tuple of row and col
    :param step: a tuple of the possible move
    :return: True or False
    """
    check = (coordinate[0] + step[0], coordinate[1] + step[1])
    for i in range(len(check)):
        if not (0 <= check[i] < BOARD_SIZE):
            return False
    return True


if __name__ == "__main__":
    test_words_dict = load_words_dict("boggle_dict.txt")

    my_board = [["A", "B", "CD", "D"],
                ["B", "C", "H", "G"],
                ["C", "D", "K", "L"],
                ["M", "C", "B", "A"]]

    my_words_dict = {"ABCDD": True, "ABCDHK": True, "AFKT": True,
                     "ABFE": True, "ABC": True, "ABCHGLKDCMNOT": True,
                     "KLKLK": True, "KLLK": True, "ABCDN": True}
    test_board = boggle_board_randomizer.randomize_board()
    test_n = 5
    test_list = find_length_n_words(test_n, test_board, test_words_dict)

    for word_item in test_words_dict:
        if len(word_item) == test_n:
            print(word_item)
    for word_item in test_board:
        print(word_item)
    print("found words:")
    for word_item in test_list:
        print(word_item)
    if len(test_list) == 0:
        print(test_list)
