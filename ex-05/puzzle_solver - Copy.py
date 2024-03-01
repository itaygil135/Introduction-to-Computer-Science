

# nested list of the all 8 directions where the word should be search. 
# each list conatins two elements. the first defines the direction of the row, the second defines the direction of the column
DIRECTIONS = [
               [ 1 ,  0] ,     # d     one row down,         stay at the same column
               [-1 ,  0] ,     # u    one row up,           stay at the same column
               [ 0 ,  1] ,     # r     stay at the same row, one column right
               [ 0 , -1] ,     # l    stay at the same row, one column left
               [ 1 ,  1] ,     #  y     one row down,         one column right
               [ 1 , -1] ,     #  z    one row down,         one column left
               [-1 ,  1] ,     #  w    one row up,           one column right
               [-1 , -1] ]     #  x    one row up,           one column left  


def solve_puzzle(puzzle, word_list):
    """search for a all fiven words in a given puzzle. for each fonded word  copy it to the 'found' board at the same location.
    param in: word_list     -   List of word that should be searched
    param in: puzzle        -   nested list (two dimantion) of letters, to search for the word in it. """
    
    rows = len(puzzle)              # number of rows at the puzzle
    cols = len(puzzle[0])           # number of letters in one row, which is the same as number of columns at the puzzle
    
    found_words = []                 # a board of the founded words. will have the same type and size as the given puzzle. 
                                    #   The board is initiated as spaces, and once a word was found - it will be copied into this board
                                    
    # prepare the blank board of the founded words.          build the found_words as a nested list (two dimantion) of characters at the same size as 'puzzle' and initiate all characters to be spaces.
    for i in range(rows):                               #   loop over all the rows
        found_words.append([" "] * cols)                #   for each rows, add strings that contains one space (" "). the number of the strings to be added is the number of the columns in the puzzle
        
    #find all words
    for word in word_list:
        find_word_in_puzzle (word, puzzle, found_words)
        
    # print the result
    print_board(found_words)
        
        
        
        
        

def find_word_in_puzzle(word, puzzle, found):
    '''
    search for a word in a given puzzle, once found, copy it to the 'found' board at the same location.
    param in: word          -   the word that should be searched   
    param in: puzzle        -   nested list (two dimantion) of letters, to search for the word in it.
    param in: found         -   nested list (two dimantion) of charaters that should be either spaces or letters that are part of founded words
    '''
    for row in range(len(puzzle)):                                          # for all rows at the pazzle
        for col in range(len(puzzle[0])):                                   # for all letter at a row (which is the same as for all columns at the puzzle)
            for direction in DIRECTIONS:                                    # for all 8 direction (up, up+right, right, down+right, down, down+left, left, up+left)
                if find_word_at(word, puzzle, row, col, direction):          # search for the word starting at (row,col) and at this direction.
                    add_word_to_found(found, word, row, col, direction)     # in case the word was found - add it to the 'found' board
                    return  
                    

def find_word_at(word, puzzle, row, col, direction):
    '''
    search for a word in a given puzzle, starting at given row and col, proceed in a given direction.
    param in: word          -   the word that should be searched   
    param in: puzzle        -   nested list (two dimantion) of letters, to search for the word in it.
    param in: direction     -   a list of two integers that define the direction of the word starting at (row, col)
                                direction[0] show if next letter of the word should be at the same row (in case of 0), row above (in case of -1) or row below(in case of +1)
                                direction[1] show if next letter of the word should be at the same col (in case of 0), col at the left at (in case of -1) or col at the right(in case of +1)
    param in: row           -   the row where the word start
    param in: col           -   the coloumn where the word start (the specific letter in the row)
    
    return                  -   True    in case the word was found in the puzlle 
                                False   in case the word was NOT found in the puzlle 
    '''
    # first verify that the search can be done within the puzzle's borders. otherwise the word can not be found starting at this (row,col)
    
    if out_of_range(len(word), puzzle, direction, row, col):
        return False
    # search for the all letters in the word, starting at the (row,col) posiziton, procceding at the given direction
    for i in range(len(word)):
        if word[i] != puzzle[row+i*direction[0]][col+i*direction[1]]:      # [row + i*direction[0]  --->   add i rows to the starting row, at the direction defined by direction[0]
                                                                          # [col + i*direction[1]  --->   add i columns to the starting column, at the direction defined by direction[1]  
            return False        #once one letter does not much, that means the word was not found starting at (row,col) and at this direction
    return True                 # if the search was not stopped before, that means the word was found


def out_of_range(word_len, puzzle, direction, row, col):
    '''
    verify word length , starting at given row and col, proceed in a given direction will not exceed the puzzle borders
    param in: word_len      -   length (number of letters) of the word that should be searched   
    param in: puzzle        -   nested list (two dimantion) of letters, to search for the word in it.
    param in: direction     -   a list of two integers that define the direction of the word starting at (row, col)
                                direction[0] show if next letter of the word should be at the same row (in case of 0), row above (in case of -1) or row below(in case of +1)
                                direction[1] show if next letter of the word should be at the same col (in case of 0), col at the left at (in case of -1) or col at the right(in case of +1)
    param in: row           -   the row where the word start
    param in: col           -   the coloumn where the word start (the specific letter in the row)
    
    return                  -   False in case the search exceed the puzlle borders
                                True in case the search is within the puzzle borders
    '''
    final_row = row + (word_len - 1 ) * direction[0]        # calculate what should be the last row to search the word at (the row of the last letter of word)
    final_col = col + (word_len - 1 ) * direction[1]        # calculate what should be the last column to search the word at (the column of the last letter of word)
    rows = len(puzzle)                                      # total number of rows at the puzzle
    cols = len(puzzle[0])                                      # total number of letters in one row, which is the total number of columns in the puzzle

    # should return True in case of a least one direction is exceeding the puzzle's borders. The cases are:
    # (final_row < 0 )         # not enought rows to search for the word at 'up' directions
    # (final_row >= rows)      # not enought rows to search for the word at 'down' directions
    # (final_col < 0 )         # not enought columns to search for the word at ''left' directions
    # (final col >= cols)      # not enought columns to search for the word at 'right' directions
    return    (final_row < 0 ) or (final_row >= rows) or (final_col < 0 ) or (final_col >= cols) 


def add_word_to_found(found, word, row, col, direction):
    ''' This function adds a founded word to the board of founded words
    param in: board     -   nested list (two dimantion) of characters, which might be either found word or space   
    param in: word      -   the founded word
    param in: row       -   the row where the word start
    param in: col       -   the coloumn where the word start (the specific letter in the row)
    param in: direction -   a list of two integers that define the direction of the word starting at (row, col)
                            direction[0] show if next letter of the word should be at the same row (in case of 0), row above (in case of -1) or row below(in case of +1)
                            direction[1] show if next letter of the word should be at the same col (in case of 0), col at the left at (in case of -1) or col at the right(in case of +1)
    '''
    #loop over all letters of word, and copy each one to its position at the founded board
    for i in range(len(word)):
        found[row+i*direction[0]][col+i*direction[1]] = word[i]         # [row + i*direction[0]  --->   add i rows to the starting row, at the direction defined by direction[0]
                                                                        # [col + i*direction[1]  --->   add i columns to the starting column, at the direction defined by direction[1]  


def print_board(board): 
    ''' This function print the board with the founded words
    param in: board -   nested list (two dimantion) of characters, which might be either found word or space   
    '''
    # loop over all rows in board 
    for row in board:
        #loop over all letters (coluoms) in one row and print them
        for letter in row:
            print (letter, end=" ")
        print ()                            # print new line at the end of the row
        
        