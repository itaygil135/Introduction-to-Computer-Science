#################################################################
# FILE : nonogram.py
# WRITER : itai kahana, itaygil135 , 316385962
#        : Ilana Gelman , ilana315061945 , 315061945
# EXERCISE : intro2cs2 ex8 2020
# DESCRIPTION: This file implement nonngram in backtracking method
# STUDENTS I DISCUSSED THE EXERCISE WITH: no one.
# WEB PAGES I USED: nothing.
# NOTES: ...
# at function intersection_row we decided to mark cells that are not equal at
# all rows with the value -1, so they can be assigned and checked recursively
# while searching for all possible solutions.
#################################################################
import copy


def is_valid_list(blocks, lst):
    """
    This function verify that a given list meet the constrains at the given
    blocks
    :param blocks:  the constrains
    :param lst:     the list to verify
    :return:    True: in case the list meet the constrains
                False: otherwise
    """
    n = len(lst)
    found_block = find_blocks(lst, n)
    if blocks == found_block:
        return True
    return False


def find_blocks(lst, n):
    """
    This function find the blocks at the first n cells in a given list
    :param lst:  the list to find the blocks in it.
    :param n:    the number of cells to search for the blocks
    :return:     nested list of the found blocks
    """
    found_block = []
    index_1 = 0
    # scan the first n cells in the list
    while index_1 < n:
        # find the next cell that contain "1"
        while index_1 < n and lst[index_1] == 0:
            index_1 = index_1 + 1
        # the following cell contains "0"
        index_0 = index_1 + 1
        # find the first cell after the sequence of "0" that contains "1"
        while index_0 < n and lst[index_0] == 1:
            index_0 = index_0 + 1
        # here, index_1 point to the beginning of the block, and index_0
        # point to the end of of blocks.
        # (it might be the indexes exceed the list)
        # in case the block start in the list, calculate its size and update
        # the output list.
        if index_1 < n:
            block_len = index_0 - index_1
            found_block.append(block_len)
        index_1 = index_0
    return found_block


def constraint_satisfactions(n, blocks):
    """
    This function find all the lists of size n that meets the given constrains
    by calling an helper function
    :param n:      the size of the lsits
    :param blocks: the constrains
    :return:  List of possible lists
    """
    option_lst = []
    constraint_helper(option_lst, [], n, blocks)
    return option_lst


def constraint_helper(final_lst, lst, n, blocks):
    """
    this function actually find all list of length n that meet the constrains
    :param final_lst: list of lists
    :param lst:       current list to be verified
    :param n:         length of list
    :param blocks:    constrains
    :return:   list of list that meet the constrains
    """
    if len(lst) == n:
        if is_valid_list(blocks, lst):
            final_lst.append(lst[:])
        return
    black_or_white = [0, 1]
    for item in black_or_white:
        lst.append(item)
        constraint_helper(final_lst, lst, n, blocks)
        lst.pop()
    return


def is_possible_until_now(blocks, lst, n):
    """
    this function verify that the first n cells at a given list do not break
    the given constrains
    :param blocks: the constrains
    :param lst:    the list to be verified
    :param n:      the number of cells to be verified.
    :return:       True: in case the n first cells do not break the constrains
                   False: otherwise
    """
    found_block = find_blocks(lst, n)
    if len(found_block) > len(blocks):
        return False
    if n == len(lst) and found_block != blocks:
        return False
    num_of_found_blocks = len(found_block)
    for i in range(num_of_found_blocks):
        if i == num_of_found_blocks - 1:
            if found_block[i] > blocks[i]:
                return False
            elif found_block[i] < blocks[i] and lst[n - 1] != 1:
                return False
        elif found_block[i] != blocks[i]:
            return False
    return True


def row_variations_helper(option_lst, lst, i, blocks):
    """
    This function actually find all possible rows that are based on a given
    row and meet the constrains.
    :param option_lst: list of all lists that meet the constrains
    :param lst:    current list to be verified
    :param i:      current cell to be assigned and tested
    :param blocks: the constrains
    :return:       updated option_lst (list of lists that meet the constrains)
    """
    if i == len(lst):
        option_lst.append(lst[:])
        return
    # if current step is done- verify it is valid and call recursively for
    #   next cell
    if lst[i] != -1:
        if is_possible_until_now(blocks,lst,i+1):
            row_variations_helper(option_lst, lst, i + 1, blocks)
        return
    # in case cell was not marked - mark it with different options and
    # try to fill in the rest of the list recursively
    black_or_white = [0, 1]
    for item in black_or_white:
        lst[i] = item
        if is_possible_until_now(blocks, lst, i + 1):
            row_variations_helper(option_lst, lst, i + 1, blocks)
    lst[i] = -1
    return


def row_variations(row, blocks):
    """
    this function find all possible rows that are based on a given row
    and meet the constrains.
    This function is using an helper function
    :param row:     given row that contains marked and unmarked cells
    :param blocks:  constrains
    :return:        list of rows that are based on the given row and meet
                    the constrains.
                    in case no row can meet the constrains, return an empty
                    list
    """
    option_lst = []
    row_variations_helper(option_lst, row, 0, blocks)
    return option_lst


def intersection_row(rows):
    """
    This function create one row that contains the common cells at a list
    of given rows
    :param rows: list of rows with marked cells
    :return:     one row that only the common cells are marked.
    """
    combined_list = []
    for i in range(len(rows[0])):
        is_different = False
        for item in rows:
            if rows[0][i] != item[i]:
                combined_list.append(-1)
                is_different = True
                break
        if not is_different:
            combined_list.append(rows[0][i])
    return combined_list


def is_completed_board(board):
    """
    This function check if a given board is completed
    :param board: board to check
    :return: True: if all cells at the board are marked
             False: if there is any cell at the board that is not marked
    """
    completed_board = True
    for item in board:
        if -1 in item:
            completed_board = False
            break
    return completed_board


def helper_solve_easy(constraints, constrains_ind, board):
    """
    This function actually try to solve the nonogram based on the given
    constrains, without guessing  any cell.
    :param constraints:  the constrains of the game
    :param constrains_ind: indication if the rows or cols constrains should
                           be verified
    :param board: board that all mandatory cells are marked
    :return: None: in case there is no board that can meet the constrains
             board: in case there might be boards that can meet the
                    constrains
    """
    for ind in range(len(board)):
        rows_options = row_variations(board[ind],
                                      constraints[constrains_ind][ind])
        if not rows_options:
            return
        board[ind] = intersection_row(rows_options)
    lst = board
    return lst


def solve_easy_nonogram(constraints):
    """
    This function try to solve the nonogram based on the given constrains,
    without guessing  any cell.
    This function is using an helper fucntion
    :param constraints: the constrains of the game
    :return: board with cells that are marked based on the constrains.
             in case no board can meet the constrains, the function will
             return None
    """
    NUM_OF_COLS___LENGH_OF_ROWS = len(constraints[1])
    NUM_OF_ROWS___LENGH_OF_COLES = len(constraints[0])
    row_board = [[-1] * NUM_OF_COLS___LENGH_OF_ROWS] * NUM_OF_ROWS___LENGH_OF_COLES
    completed_board = False
    while not completed_board:
        row_board = helper_solve_easy(constraints, 0 , row_board)
        if row_board == None:
            return
        col_board = [[row_board[j][i] for j in range(len(row_board))] for i in
                     range(len(row_board[0]))]
        holder_lst = copy.deepcopy(col_board)
        col_board = helper_solve_easy(constraints, 1, col_board)
        if col_board is None:
            return
        if holder_lst == col_board:
            row_board = [[col_board[j][i] for j in range(len(col_board))] for i
                         in range(len(col_board[0]))]
            return row_board
        row_board = [[col_board[j][i] for j in range(len(col_board))] for i in
                     range(len(col_board[0]))]

        completed_board = is_completed_board(row_board)
    return row_board


def solve_nonogram(constraints):
    """
    This function provide all possible solution for nonogram game.
    This function is using an helper function
    :param constraints: the game constrains
    :return: list of all possible solutions. in case there is no solution,
             the function will return an empty list
    """
    all_options = []
    board = solve_easy_nonogram(constraints)
    if board == None:
        return all_options

    completed_board = is_completed_board(board)
    if completed_board:
        all_options.append(board)
        return all_options

    solve_nonogram_helper(constraints, board, 0, all_options)
    return all_options


def solve_nonogram_helper(constraints, board, ind, all_options):
    """
    This function provide all possible solution for nonogram game.
    :param constraints: the game constrains
    :param board:       the full/partial board to be verified
    :param ind:         the cell index at the board that the board should be
                        verifed up to it.
    :param all_options: list of boards that meet the constrains
    :return:            the list of boards that meet the constrains.
                        in case there is no such board, return an empty list
    """
    if ind == len(board) * len(board[0]):
        all_options.append(copy.deepcopy(board))
        return
    row, col = ind // len(board[0]), ind % len(board[0])
    if board[row][col] != -1:
        if is_possible_step(constraints, board, ind,row,col):
            solve_nonogram_helper(constraints, board, ind + 1, all_options)
        return
    black_or_white = [0, 1]
    for value in black_or_white:
        board[row][col] = value
        if is_possible_step(constraints, board, ind,row,col):
            solve_nonogram_helper(constraints, board, ind + 1, all_options)
    board[row][col] = -1


def is_possible_step(constraints, board, ind,row,col):
    """
    This function check if a possible marking of cell at a given board will
    not break the constrains
    :param constraints: the game constrains
    :param board:       the board to be verified
    :param ind:         index of the cell that is now marked
    :param row:         row of the cell that is now marked
    :param col:         col of the cell that is now marked
    :return:            True in case the marking will not break the constrains
                        False otherwise
    """
    valid_row=is_possible_until_now(constraints[0][row],board[row],col+1)
    if not valid_row:
        return False
    temp_col=[]
    for i in range(len(board)):
        temp_col.append(board[i][col])
    valid_col=is_possible_until_now(constraints[1][col],temp_col,row+1)
    if not valid_col:
        return False
    return True

