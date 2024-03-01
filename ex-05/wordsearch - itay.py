#################################################################
# FILE : ex5.py
# WRITER : itai kahana, itaygil135 , 316385962
# EXERCISE : intro2cs2 ex5 2020
# DESCRIPTION: This program find list of words in a given table
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: nothing.
# NOTES: ...
#################################################################
import sys
import os.path
from pathlib import Path

DELIMETER = ','

# dictionary of the all 8 directions where the word should be searched.
# The keys are the valid letters identifying the directions
# Each value contains two elements: the first defines the direction of the row
#            and the second defines the direction of the column

DIR_DICT = {'d':[1,0],   # one row down,         stay at the same column
            'u':[-1,0],  # one row up,           stay at the same colum
            'r':[0,1],   # stay at the same row, one column right
            'l':[0,-1],  # stay at the same row, one column left
            'y':[1,1],   # one row down,         one column right
            'z':[1,-1],  # one row down,         one column left
            'w':[-1,1],  # one row up,           one column right
            'x':[-1,-1]} # one row up,           one column left


def is_valid_directions():
    for letter in sys.argv[4]:
        if letter in DIR_DICT:
            pass
        else:
            print("at least one of the letter you typed in sys.argv[4] is not"
                  " valid therefore the program will stop")
            return False
    return True

def is_num_of_par_valid():
    if len(sys.argv) == 5:
        return True
    else:
        return  False

def is_all_files_exist():
    if os.path.isfile(sys.argv[1]):
        if os.path.isfile(sys.argv[2]):
            return True
        else:
            print("the file you type for being the mat_filename's parameter is "
            "not excict therefore the program will stop")
            return False
    else:
        print("the file you type for being the word_lst_filename's parameter is "
              "not exist therefore the program will stop")
        return False

def is_input_valid():
    if not is_num_of_par_valid():
        print("the amount of the parameters isn't 4 and therefore the "
                "program will stop")
        return False
    if not is_all_files_exist():
        return False
    if not is_valid_directions():
        return False
    else:
        return True








def get_list_from_file(list_name,file_name):
    #TODO hundle the case the input fileis not exice
    #TODO if os.path.exists(filename)
    with open(file_name, 'r') as f:
        for line in f:
            list_name.append(line[0:len(line) - 1])
        f.close()

def str_to_list(string):
    lst_string = []
    for char in string:
        if char != DELIMETER:
            lst_string.append(char)
    return lst_string


def read_matrix(mat_filename):
    mat = []
    row_list = []
    get_list_from_file(row_list,mat_filename)
    for row in row_list:
        mat.append(str_to_list(row))
    return mat



def find_words(word_list,matrix,directions):
    '''
      search for a word in a given matrix, once found, add value 1 to the key dict called milon in item word.
      param in: word          -   the word that should be searched
      param in: matrix        -   nested list (two dimantion) of letters, to search for the word in it.

      for row in range(len(matrix)):  # for all rows at the matrix
          for col in range(len(matrix[0])):  # for all letter at a row (which is the same as for all columns at the puzzle)
              for direction in DIRECTIONS:  # for all given direction which could be max (up, up+right, right, down+right, down, down+left, left, up+left)
                  if find_word_at(word, matrix, row, col,
                                  direction):  # search for the word starting at (row,col) and at this direction.
                      add_word_to_found the value of found word in milon when word is the key'''
    rows = len(matrix)
    cols = len(matrix[0])
    milon  = {}
    for word in word_list:
        milon[word] = 0
    output_list =[]
    for word in word_list:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                for key in directions:
                     if find_word_at(word, matrix, row, col, key):
                         milon[word] = milon[word] + 1

    for item in milon:
        if milon[item] != 0:
            output_list.append(item +DELIMETER + str(milon[item]))
    return output_list

def find_word_at(word, matrix, row, col, key):
    '''
    search for a word in a given matrix, starting at given row and col, proceed in a given direction.
    param in: word          -   the word that should be searched
    param in: matrix        -   nested list (two dimantion) of letters, to search for the word in it.
    param in: direction     -   a list of two integers that define the direction of the word starting at (row, col)
                                direction[0] show if next letter of the word should be at the same row (in case of 0), row above (in case of -1) or row below(in case of +1)
                                direction[1] show if next letter of the word should be at the same col (in case of 0), col at the left at (in case of -1) or col at the right(in case of +1)
    param in: row           -   the row where the word start
    param in: col           -   the coloumn where the word start (the specific letter in the row)

    return                  -   True    in case the word was found in the matrix
                                False   in case the word was NOT found in the matrix
    '''
    # first verify that the search can be done within the matrix's borders. otherwise the word can not be found starting at this (row,col)

    if out_of_range(len(word), matrix, key, row, col):
        return False
    # search for the all letters in the word, starting at the (row,col) posiziton, procceding at the given direction
    for i in range(len(word)):
        if word[i] != matrix[row + i * DIR_DICT[key][0]][col + i * DIR_DICT[key][1]]:  # [row + i*direction[0]  --->   add i rows to the starting row, at the direction defined by direction[0]
            # [col + i*direction[1]  --->   add i columns to the starting column, at the direction defined by direction[1]
            return False  # once one letter does not much, that means the word was not found starting at (row,col) and at this direction
    return True  # if the search was not stopped before, that means the word was found


def out_of_range(word_len, puzzle, key, row, col):
    '''
    verify word length , starting at given row and col, proceed in a given direction will not exceed the puzzle borders
    param in: word_len      -   length (number of letters) of the word that should be searched
    param in: puzzele       -   nested list (two dimantion) of letters, to search for the word in it.
    param in: direction     -   a list of two integers that define the direction of the word starting at (row, col)
                                direction[0] show if next letter of the word should be at the same row (in case of 0), row above (in case of -1) or row below(in case of +1)
                                direction[1] show if next letter of the word should be at the same col (in case of 0), col at the left at (in case of -1) or col at the right(in case of +1)
    param in: row           -   the row where the word start
    param in: col           -   the coloumn where the word start (the specific letter in the row)

    return                  -   False in case the search exceed the puzlle borders
                                True in case the search is within the puzzle borders
    '''
    final_row = row + (word_len - 1) * DIR_DICT[key][0]  # calculate what should be the last row to search the word at (the row of the last letter of word)
    final_col = col + (word_len - 1) * DIR_DICT[key][1]  # calculate what should be the last column to search the word at (the column of the last letter of word)
    rows = len(puzzle)  # total number of rows at the puzzle
    cols = len(puzzle[0])  # total number of letters in one row, which is the total number of columns in the puzzle

    # should return True in case of a least one direction is exceeding the puzzle's borders. The cases are:
    # (final_row < 0 )         # not enought rows to search for the word at 'up' directions
    # (final_row >= rows)      # not enought rows to search for the word at 'down' directions
    # (final_col < 0 )         # not enought columns to search for the word at ''left' directions
    # (final col >= cols)      # not enought columns to search for the word at 'right' directions
    return (final_row < 0) or (final_row >= rows) or (final_col < 0) or (final_col >= cols)










def write_output(results,filename):
    with open(filename, 'w') as f:
        for item in results:
            f.write(item)
            f.write("\n")
        f.close()  # TODO cheking if works withot close

def read_wordlist(word_lst_filename):
    words = []
    get_list_from_file(words, word_lst_filename)
    return words



def main():
    if not is_input_valid():
        return 'stop'
    word_lst_filename = sys.argv[1]
    mat_filename = sys.argv[2]
    output_filename = sys.argv[3]
    directions_str = sys.argv[4]
    directions_set = set()
    for letter in directions_str:
        directions_set.add(letter)

    #TODO all argumenus has value, the direction_str contains only valid char
    #TODO idnore a valid letter which appear more than one in directions_str

    look_for_word_lst = read_wordlist(word_lst_filename)
    #TODO hundle the case the input fileis not exice
    mat = read_matrix(mat_filename)
    #TODO hundle the case the input fileis not exice


    output_list = find_words(look_for_word_lst,mat,directions_set)
    print(output_list)
    write_output(output_list,output_filename)


if __name__ == '__main__':
    main()
