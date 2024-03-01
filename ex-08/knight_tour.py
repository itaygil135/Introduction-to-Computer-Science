BOARD_SIZE = 7
POSSIBLE_MOVES = [( 1,  2),
                  ( 2,  1),
                  (-1,  2),
                  (-2,  1),
                  ( 1, -2),
                  ( 2, -1),
                  (-1, -2),
                  (-2, -1)]

def print_board(board):
    for row in board:
        for cell in row:
            print(str(cell).center(2), end=" ")
        print()
    print()

def is_legal_step(board, row, col):
    return          0 <= row < BOARD_SIZE                           \
            and     0 <= col < BOARD_SIZE                           \
            and     board[row][col] == 0

def _tour_helper(board,start_row, start_col, step_num):
    if step_num > BOARD_SIZE ** 2:
        print_board((board))
        return True

    if not is_legal_step (board, start_row, start_col):
        return False

    board[start_row][start_col] = step_num
    for move in POSSIBLE_MOVES:
        if _tour_helper(board,
                        start_row + move[0] ,
                        start_col + move[1],
                        step_num + 1):
            return True
    board[start_row][start_col] = 0
    return False



def find_knight_tour(start_row, start_col):
    board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    b_was_found = _tour_helper(board, start_row, start_col, 1)
    print("b_was_found = ", b_was_found)


if __name__ == '__main__':
    find_knight_tour(0,0)
