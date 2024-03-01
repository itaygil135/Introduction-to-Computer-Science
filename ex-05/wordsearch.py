#################################################################
# FILE : wordsearch.py
# WRITER : itai kahana, itaygil135 , 316385962
# EXERCISE : intro2cs2 ex5 2020
# DESCRIPTION: This program find list of words in a given table
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: nothing.
# NOTES: ...
#################################################################
import sys
import os.path

EXPECTED_NUM_OF_PARAMETERS = 5
DELIMITER = ','

# dictionary of the all 8 directions where the word should be searched.
# The keys are the valid letters identifying the directions
# Each value contains two elements: the first defines the direction of the row
#            and the second defines the direction of the column

DIR_DICT = {'d': [1, 0],    # one row down,         stay at the same column
            'u': [-1, 0],   # one row up,           stay at the same column
            'r': [0, 1],    # stay at the same row, one column right
            'l': [0, -1],   # stay at the same row, one column left
            'y': [1, 1],    # one row down,         one column right
            'z': [1, -1],   # one row down,         one column left
            'w': [-1, 1],   # one row up,           one column right
            'x': [-1, -1]}  # one row up,           one column left


def is_valid_directions(directions_str):
    """
    This Function validate the input parameter of selected directions.
    :param directions_str: string of input directions
    :return:
    True in case all input direction are valid
    False in case at least one input direction is not valid
    """
    for letter in directions_str:
        if letter not in DIR_DICT:
            print("at least one of the letter you typed in sys.argv[4] is not"
                  " valid therefore the program will stop")
            return False
    return True


def is_valid_num_of_parameters(num_of_parameters):
    """
    This function verify the number of input parameters
    :param num_of_parameters: number of input parameters
    :Param num_of_parameters: number of parameters provided to the program
    :return:
    True : in case num of parameters are as expected
    False : otherwise.
    """
    if num_of_parameters == EXPECTED_NUM_OF_PARAMETERS:
        return True
    return False


def is_all_files_exist(file1, file2):
    """
    This function verify the two input files are exists, and print a relevant
    error message
    :param file1: First file name to search for (word list)
    :param file2: Second file name to search for (matrix)
    :return:
    True : in case both files exist
    False : in case at least one file does not exist
    """
    if os.path.isfile(file1):
        if os.path.isfile(file2):
            return True
        else:
            print("the file you type for being the mat_filename's parameter is"
                  "not exist therefore the program will stop")
            return False
    else:
        print("the file you type for being the word_lst_filename's parameter is "
              "not exist therefore the program will stop")
        return False


def is_input_valid():
    """
    This function verify all input parameters are valid
    :return:
    """
    if not is_valid_num_of_parameters(len(sys.argv)):
        print("the amount of the parameters isn't 4 and therefore the "
              "program will stop")
        return False
    if not is_all_files_exist(sys.argv[1], sys.argv[2]):
        return False
    if not is_valid_directions(sys.argv[4]):
        return False
    else:
        return True


def get_lines_from_file(file_name):
    """
    This function reads all lines at a given file.
    :param file_name: name of the file to be read
    :return:
    lines_list - list of all lines read from teh file
    """
    lines_list = []
    with open(file_name, 'r') as f:
        for line in f:
            lines_list.append(line[0:len(line) - 1])
        f.close()
    return lines_list


def line_str_to_mat_row(string):
    """
    extract letters from a given line whilst skipping the delimiter and
    return the letters as a list
    :param string: a line read from the mat file
    :return: list of letters only found at the line
    """
    lst_string = []
    for char in string:
        if char != DELIMITER:
            lst_string.append(char)
    return lst_string


def read_matrix(mat_filename):
    """
    This function read all lines from the matrix file, extracts the letters
    at each line and build the matrix
    :param mat_filename: the name of the file contains the matrix data
    :return: two-level nested list that represent the matrix
    """
    mat = []
    lines_list = get_lines_from_file(mat_filename)
    for line in lines_list:
        mat.append(line_str_to_mat_row(line))
    return mat


def create_words_counter(word_list):
    """
    This function create aa dictionary that will be used to count the
    number of each words appearance.
    :param word_list: List of words to search
    :return:
    A dictionary contains all words to be searched with initial counter = 0
    """
    words_counter = {}
    for word in word_list:
        words_counter[word] = 0
    return words_counter


def create_output_list(words_counter):
    """
    This function creates a list of strings to be written to the output file.
    :param words_counter: a dictionary contains a counter of appearance for
    each word.
    :return:
    List of strings, each string contains a word that was found the the number
    of times the word was found
    """
    output_list = []
    for word in words_counter:
        if words_counter[word] != 0:
            my_tuple= word, words_counter[word]
            output_list.append(my_tuple)
    return output_list


def find_words(word_list, matrix, directions):
    """
    Search for all words appearance in a given matrix. The search should be
    done at all given directions.
    The function first create a dictionary that will count the
    appearance of each word. Then, for each word, the function will scan all
    cubes at the matrix and search for the word starting at that cube, at all
    given directions. in case the word found, its counter will be increased.
    Once all searches completed, the function will create an output list from
    the word_counter dictionary and will return it
    :param word_list: List of words to be searched
    :param matrix: the matrix to search for the words in it.
    :param directions: directions to search the word
    :return:
    """
    words_counter = create_words_counter(word_list)

    for word in word_list:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                for key in directions:
                    if find_word_at(word, matrix, row, col, key):
                        words_counter[word] = words_counter[word] + 1

    output_list = create_output_list(words_counter)

    return output_list


def find_word_at(word, matrix, row, col, key):
    """
    search for a word in a given matrix, starting at given row and col,
    proceed in a given direction.
    param in: word      -   the word that should be searched
    param in: matrix    -   a matrix to search for the word in it.
    param in: direction -   a direction to look at
    param in: row       -   the row where the word start
    param in: col       -   the column where the word start
    return      -   True    in case the word was found in the matrix
                 False   in case the word was NOT found in the matrix
    """
    # first verify that the search can be done within the matrix's borders.
    # # otherwise the word can not be found starting at this (row,col)
    if out_of_range(len(word), matrix, key, row, col):
        return False

    # search for the all letters in the word, starting at (row,col) position,
    # proceeding at the given direction
    for i in range(len(word)):
        # [row + i*direction[0] --->  add i rows to the starting row,
        # at the direction defined by direction[0]
        next_row = row + i * DIR_DICT[key][0]
        # [col + i*direction[1]  --->   add i columns to the starting column,
        # at the direction defined by direction[1]
        next_col = col + i * DIR_DICT[key][1]
        if word[i] != matrix[next_row][next_col]:
            return False
    return True


def out_of_range(word_len, matrix, key, row, col):
    """
    verify word length , starting at given row and col, proceed in a given
    direction will not exceed the matrix borders
    param in: word_len:  length of the word that should be searched
    param in: matrix:    a matrix to search for the word in it.
    param in: direction: direction to search at.
    param in: row : the row where the word start
    param in: col : the column where the word start

    return   -   False in case the search exceed the matrix borders
             -   True in case the search is within the matrix borders
    """
    # calculate what should be the last row to search the word at
    final_row = row + (word_len - 1) * DIR_DICT[key][0]
    # calculate what should be the last column to search the word at
    final_col = col + (word_len - 1) * DIR_DICT[key][1]

    rows = len(matrix)     # number of rows at the matrix
    cols = len(matrix[0])  # number of letters in one row,

    # should return True in case of at least one direction is exceeding the
    # matrix's borders. The cases are:
    # (final_row < 0 )    - not enough rows to search for the word  'up'
    # (final_row >= rows) - not enough rows to search for the word  'down'
    # (final_col < 0 )    - not enough columns to search for the word 'left'
    # (final col >= cols) - not enough columns to search for the word 'right'
    return (final_row < 0) or (final_row >= rows) or \
           (final_col < 0) or (final_col >= cols)


def write_output(results, filename):
    """
    this function write the list of found words to a given output file
    :param results: list of found words
    :param filename: name of the output file
    :return:
    """
    with open(filename, 'w') as f:
        for item in results:
            # output_list.append(word + DELIMITER + str(words_counter[word]))
            f.write(item[0]+DELIMITER + str(item[1]) )
            f.write("\n")
        f.close()


def read_wordlist(word_lst_filename):
    """
    This function read the list of words to  search for from a given file
    :param word_lst_filename: the name of the file contains the words
    :return:
    List of words to search
    """
    words = get_lines_from_file(word_lst_filename)
    return words


def create_direction_set(directions_str):
    """
    This function remove duplication of letters appears at the requested
    direction
    :param directions_str: input requested directions as given by the user
    :return:
    a set of directions to search for, when each direction appears only once.
    """
    directions_set = set()
    for letter in directions_str:
        directions_set.add(letter)
    return directions_set


def main():
    """
    Main function of the program
    1) validate input parameters
    2) read the list of words to search
    3) read the matrix to search in
    4) create a set of directions to search
    5) search for all words at all directions at the matrix
    6) write the found words to the output file.
    :return:
    """
    if is_input_valid():
        word_lst_filename = sys.argv[1]
        mat_filename = sys.argv[2]
        output_filename = sys.argv[3]
        directions_str = sys.argv[4]
        look_for_word_lst = read_wordlist(word_lst_filename)
        mat = read_matrix(mat_filename)
        directions_set = create_direction_set(directions_str)
        output_list = find_words(look_for_word_lst, mat, directions_set)
        write_output(output_list, output_filename)


if __name__ == '__main__':
    main()
