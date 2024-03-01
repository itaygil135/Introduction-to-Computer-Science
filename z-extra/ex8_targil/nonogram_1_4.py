import copy
def is_valid_list(blocks ,lst):
    i = 0;
    n = len(lst)
    found_block =[]
    index_1 = 0
    index_0 = 0
    while (index_1 < n):
        while index_1 < n and lst[index_1] == 0:
            index_1 = index_1 + 1
        index_0 = index_1 + 1
        while index_0 < n and lst[index_0] == 1:
            index_0 = index_0 + 1
        if index_1 < n:
            block_len = index_0 - index_1
            found_block.append(block_len)
        index_1 = index_0
    if blocks == found_block:
        return True
    return False


def constraint_satisfactions(n, blocks):
    option_lst = []
    constraint_helper(option_lst, [], n, blocks)
    return option_lst


def constraint_helper(final_lst, lst, n, blocks):
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




def is_possible_until_now(blocks ,lst, n):
    found_block =[]
    index_1 = 0 ;
    index_0 = 0 ;
    while (index_1 < n):
        while index_1 < n and lst[index_1] == 0:
            index_1 = index_1 + 1
        index_0 = index_1 + 1
        while index_0 < n and lst[index_0] == 1:
            index_0 = index_0 + 1
        if index_1 < n:
            block_len = index_0 - index_1
            found_block.append(block_len)
        index_1 = index_0

    if len(found_block) > len(blocks):
        return False

    if n == len(lst) and found_block != blocks:
        return False

    num_of_found_blocks = len(found_block)
    for i in range(num_of_found_blocks):
        if i == num_of_found_blocks -1:
            if found_block[i] > blocks[i]:
                return False
            elif found_block[i] < blocks[i] and lst[ n -1] != 1:
                return False
        elif found_block[i] != blocks[i]:
            return False
    return True



def row_variations(row, blocks):
    option_lst = []
    row_variations_helper(option_lst ,row, 0, blocks)
    return option_lst


def row_variations_helper(final_lst, lst,  i, blocks):
    if i == len(lst):
        if is_valid_list(blocks, lst):
            final_lst.append(lst[:])
        return
        # if current step is done - call recursivly for the n-1
    if lst[i] != -1:
        row_variations_helper(final_lst ,lst, i+ 1, blocks)
        return

    black_or_white = [0, 1]
    for item in black_or_white:
        lst[i] = item
        if is_possible_until_now(blocks, lst, i + 1):
            row_variations_helper(final_lst, lst, i + 1, blocks)
            lst[i] = -1
    lst[i] = -1
    return

def intersection_row(rows):
    outcum_list = []
    for i in range(len(rows[0])):
        flag = "="
        for item in rows:
            if rows[0][i] != item[i]:
                outcum_list.append(-1)
                flag = "!="
                break
        if flag == "=":
            outcum_list.append(rows[0][i])


    return outcum_list

def helper_solve_easy(constraints,tuple):
    for ind in range(len(tuple[0])):
        rows_options = row_variations(tuple[0][ind], constraints[tuple[1]][ind])
        if rows_options == []:
            print("this is not possible data/board")
            return
        tuple[0][ind] = intersection_row(rows_options)
    lst = tuple[0]
    return lst







def solve_easy_nonogram(constraints):
    flag = "go on"
    NUM_OF_COLS___LENGH_OF_ROWS = len(constraints[1])
    NUM_OF_ROWS___LENGH_OF_COLES = len(constraints[0])
    row_board = [[-1] * NUM_OF_COLS___LENGH_OF_ROWS] * NUM_OF_ROWS___LENGH_OF_COLES
    while flag == "go on":
        flag = "stop"
        tuple_row = (row_board,0)
        row_board = helper_solve_easy(constraints,tuple_row)
        if row_board == None:
            return
        col_board = [[row_board[j][i] for j in range(len(row_board))] for i in range(len(row_board[0]))]
        tuple_col = (col_board,1)
        holder_lst = copy.deepcopy(col_board)
        col_board = helper_solve_easy(constraints,tuple_col)
        if col_board == None:
            return
        if holder_lst == col_board:
            row_board = [[col_board[j][i] for j in range(len(col_board))] for i in range(len(col_board[0]))]
            return row_board
        row_board = [[col_board[j][i] for j in range(len(col_board))] for i in range(len(col_board[0]))]

        for item in row_board:
            if -1 in item:
                flag = "go on"

    return row_board




print(solve_easy_nonogram([[[],[4],[6],[2, 2],[1, 3]],[[],[2],[1],[2, 2],[2, 2]]]))
















