

SIZE = 9


def print_board(board):
    for row in board:
        for num in row:
            print (num, end=" ")
        print()
    print()


def ok_to_place(board, value, row, col):
    for x in range(SIZE):
        n  = (row // 3) * 3 + (x // 3)
        m = (col // 3) * 3 + (x % 3)
        if     board[x][col] == value                       \
            or board[row][x] == value                       \
            or board[n][m] == value:
            return False
    return True



def _sudoku_helper(board,ind):
    if ind == SIZE * SIZE:
        print("found solution:")
        print_board(board)
        return

    row, col = ind // SIZE , ind % SIZE

    if board[row][col] != 0:
        _sudoku_helper(board, ind + 1)
        return

    for value in range(1, SIZE + 1):
        if ok_to_place(board, value, row, col):
            board[row][col] = value
            _sudoku_helper(board, ind + 1)
    board[row][col] = 0

def solve_sudoku(board):
    _sudoku_helper(board,0)




if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0, 3, 0, 1, 7],
             [0, 1, 5, 0, 0, 9, 0, 0, 8],
             [0, 6, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 7, 0, 0, 0],
             [0, 0, 9, 0, 0, 0, 2, 0, 0],
             [0, 0, 0, 5, 0, 0, 0, 0, 4],
             [0, 0, 0, 0, 0, 0, 0, 2, 0],
             [5, 0, 0, 6, 0, 0, 3, 4, 0],
             [3, 4, 0, 2, 0, 0, 0, 0, 0]]

    print("original board is:")
    print_board(board)

    solve_sudoku(board)

    print("original board after game:")
    print_board(board)