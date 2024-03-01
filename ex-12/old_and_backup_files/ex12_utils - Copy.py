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
    with open( file_path,'r') as f:
        words_dict = dict()
        for line in f:
            our_list = line.replace("\n", "")
            if our_list not in words_dict:
                words_dict[our_list] = True



        return words_dict




def is_valid_path(board, path, words):
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
            if not(0 <= coordinate <BOARD_SIZE):
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
        return  None

    return word


def find_length_n_words(n, board, words):

    word_search = set()
    for item in words:
        if len(item) == n:
            word_search.add(item)

    all_milim= []
    for row in range(len(board)):
        for col in range(len(board[row])):
                coordinate = (row,col)
                if find_length_n_words_helper(n,board,word_search,all_milim,[],coordinate):
                    return all_milim

    return all_milim

def find_length_n_words_helper(n,board,word_search,list_of_tuples,mooving_list,coordinate):
    if len(word_search) == 0:
        return True
    mooving_list.append(coordinate)
    word = ""
    for item in mooving_list:
        word = word + board[item[0]][item[1]]

    if len(word) < n:
            for move in POSSIBLE_MOVES:
                if is_legal_step(board,coordinate,move,word,word_search):
                    coordinate = (coordinate[0] + move[0], coordinate[1] + move[1])
                    find_length_n_words_helper(n,board,word_search,list_of_tuples,mooving_list,coordinate)
                    coordinate = (coordinate[0] - move[0], coordinate[1] - move[1])
    else:
        if word in word_search:
            verify = set(mooving_list)
            if len(verify) == len(mooving_list):
                add = copy.deepcopy(mooving_list)
                tuple_temp = (word,add)
                list_of_tuples.append(tuple_temp)
                word_search.remove(word)
                verify = set()
    mooving_list.pop()
    if len(mooving_list) == 0:
        return False

    return






def is_legal_step(board, coordinate, step,word,word_search):
    check = (coordinate[0] + step[0],coordinate[1] + step[1])
    for i in range(len(check)):
        if not (0 <= check[i] < BOARD_SIZE):
            return False
    for item in word_search:
        if item[0:len(word)] == word:
            return True

    return False

if __name__== "__main__":
    words_dict = load_words_dict("boggle_dict.txt")
    board = boggle_board_randomizer.randomize_board()
    for item in board:
        print(item)
    listt = find_length_n_words(10, board, words_dict)
    print(listt)

