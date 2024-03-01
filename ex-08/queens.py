

def illegal_placement(board, row, col):
    #note: it is enought to look for the threatening queens in lower columns
    for delta in range (1, col+1):
        #check for qkueen in the same row or in upper diagonal or in lower diagonal
        if  ( board[row][col-delta]   or                                  \
                (row-delta >=0 and board[row-delta][col-delta])  or       \
                (row+delta < len(board) and board[row+delta][col-delta])):
            return True
    return False

def print_board(board):
    for row in board:
        for q in row:
            print ('Q', end = " ") if q else print ('-', end = " ")
        print()


def place_queen_at_col(board, col):
    #base case: we have passed teh last column
    if col == len(board[0]):
        return True
    #iterate over rows until it is okay to place a queen
    for row in range(len(board)):
        if illegal_placement(board,row,col):
            continue
        #place the queen
        board[row][col] = True
        #check  if we can fill up the remaining columns
        if place_queen_at_col(board, col +1):
            return True
        #if not, remove the queen and keep iterating
        board[row][col] = False
    #if no placement works, give up
    return False

def place_queens(board_size):
    board = []
    for i in range(board_size):
        board.append([])
        for j in range(board_size):
            board[i].append(False)

    if place_queen_at_col(board, 0):
        print_board(board)
    else:
        print("no placement found")

if __name__ == '__main__':
    place_queens(8)


