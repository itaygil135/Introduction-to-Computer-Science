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

    word_search_set = set()
    for item in words:
        if len(item) == n:
            word_search_set.add(item)

    print("all words are\n",word_search_set)
    all_found_words= []
    for word_to_search in word_search_set:
        b_word_found = False
        for row in range(len(board)):
            for col in range(len(board[row])):
                coordinate = (row,col)
                if find_length_n_words_helper(n,  # length of word
                                              board,
                                              "", # word found until now
                                              word_to_search,
                                              all_found_words,
                                              [],#path to the word found until now
                                              coordinate):
                    b_word_found = True
                    break
            if b_word_found:
                break
    return all_found_words

def find_length_n_one_word



def find_length_n_words_helper(n,board,word_found,word_to_search,all_found_words,mooving_list,coordinate):
    #if len(word_search) == 0:
    #    return True

    if coordinate in mooving_list:
        return False

    temp_word = word_found + board[coordinate[0]][coordinate[1]]
    if temp_word == word_to_search:
        mooving_list.append(coordinate)
        add = copy.deepcopy(mooving_list)
        tuple_temp = (temp_word, add)
        all_found_words.append(tuple_temp)
        return True

    if len(temp_word) > len(word_to_search):
         return False

    for index in range(len(temp_word)):
        if temp_word[index] != word_to_search[index]:
            return False
    # from here i know: temp_word 'abc'   word_search = 'abcde'
    mooving_list.append(coordinate)
    word_found = word_found + board[coordinate[0]][coordinate[1]]
    for move in POSSIBLE_MOVES:
        if is_legal_step(board, coordinate, move, word_found, word_to_search):
            coordinate = (coordinate[0] + move[0], coordinate[1] + move[1])
            if find_length_n_words_helper(n, board, word_found, word_to_search, all_found_words, mooving_list, coordinate):
                return True
            else:
                coordinate = (coordinate[0] - move[0], coordinate[1] - move[1])

    num_of_chars_to_delete = len(board[coordinate[0]][coordinate[1]])
    if num_of_chars_to_delete == 2:
        print(num_of_chars_to_delete, " " , board[coordinate[0]][coordinate[1]])
    num_of_chars_to_delete = -1 *num_of_chars_to_delete
    word_found = word_found[0:num_of_chars_to_delete]
    mooving_list.pop()

    return False


def is_legal_step(board, coordinate, step,word,word_search):
    check = (coordinate[0] + step[0],coordinate[1] + step[1])
    for i in range(len(check)):
        if not (0 <= check[i] < BOARD_SIZE):
            return False
    return True

if __name__== "__main__":
    words_dict = load_words_dict("boggle_dict.txt")

    my_board = [["A","B","CD","D"],
                ["E","C","H","G"],
                ["I","D","K","L"],
                ["M","N","O","T"]]
    #my_words_dict = {"BFJN":True}

    my_words_dict = {"BFJN":True,"EFHG":True,"AFKT":True,"ABFE":True,
                     "DHGL":True,"KLKLK":True,"KLLK":True,"ABCDN":True}
    board = boggle_board_randomizer.randomize_board()

    listt = find_length_n_words(5, my_board, my_words_dict)
    for item in my_board:
        print(item)
    print("found words:")
    for item in listt:
        print(item)
    if len(listt) == 0:
        print(listt)



